"""Boucle de fond pour le hero de www.clixite.be : les quatre plans du film, sans titres ni logo, sans son.
Même décision de montage que le film (edit.json : variantes, points d'entrée, cadrage, étalonnage).
Jonction invisible : les L dernières secondes du plan 4 se fondent dans les L premières du plan 1,
et le fichier commence juste après ce fondu ; en lecture en boucle, on ne voit jamais la coupe.
Usage : python3 build_film.py est indépendant ; ici : python3 hero_loop.py <dossier_sortie>
"""
import json, os, subprocess, sys
FPS = 24
E = json.load(open("edit.json"))
RUSHES = next(p for p in ("rushes", "../assets/rushes") if os.path.isdir(p))
OUT = sys.argv[1] if len(sys.argv) > 1 else "hero"
L = 0.5                      # durée du fondu de jonction (s)
XF = E["fondu_1_2"] / FPS     # fondu enchaîné plan 1 vers plan 2, comme dans le film

# nom, largeur, hauteur, format de cadrage (edit.json), qualité
VARIANTES = [
    ("hero-1920", 1920, 1080, "16x9", 22),
    ("hero-1280", 1280, 720, "16x9", 23),
    ("hero-720x1280", 720, 1280, "9x16", 23),
]

def plan(i, start, dur, W, H, fmt, label):
    s = E["plans"][i]; g = s["etalonnage"]
    if fmt == "16x9":
        geo = f"scale={W}:{H}:flags=lanczos"
    else:
        cx = s["cadrage"].get(fmt, 0.5)
        if isinstance(cx, list):
            cx = f"({cx[0]}+({cx[1]}-{cx[0]})*min(1\\,t/{dur:.4f}))"
        geo = f"scale=-2:{H}:flags=lanczos,crop={W}:{H}:(in_w-{W})*{cx}:0"
    return (f"[{i}:v]trim=start={start:.4f}:duration={dur:.4f},setpts=PTS-STARTPTS,format=yuv444p10le,"
            f"colorbalance=rs={g['rs']}:gs={g['gs']}:bs={g['bs']}:rm={g['rm']}:bm={g['bm']}:rh={g.get('rh',0)}:bh={g.get('bh',0)},"
            f"eq=contrast={g['contraste']}:saturation={g['saturation']}:brightness={g.get('luminosite',0)}:gamma={g.get('gamma',1)},"
            f"{geo},fps={FPS},format=yuv420p,setsar=1,settb=1/24[{label}]")

def build(name, W, H, fmt, crf):
    p = E["plans"]
    inputs = []
    for s in p:
        inputs += ["-i", f"{RUSHES}/{s['fichier']}"]
    inputs += ["-i", f"{RUSHES}/{p[0]['fichier']}"]                         # 4 : tête du plan 1 pour la jonction
    fc = [
        plan(0, p[0]["entree"] + L, 3.0 - L + XF / 2, W, H, fmt, "a"),     # plan 1 sans sa tête
        plan(1, p[1]["entree"] - XF / 2, 3.0 + XF / 2, W, H, fmt, "b"),
        plan(2, p[2]["entree"], 3.0, W, H, fmt, "c"),
        plan(3, p[3]["entree"], 3.0, W, H, fmt, "d"),
        plan(0, p[0]["entree"], L, W, H, fmt, "h").replace("[0:v]", "[4:v]", 1),
        f"[a][b]xfade=transition=fade:duration={XF:.4f}:offset={3.0 - L - XF / 2:.4f}[ab]",
        "[ab][c][d]concat=n=3:v=1:a=0,settb=1/24[abcd]",
        f"[abcd][h]xfade=transition=fade:duration={L:.4f}:offset={12.0 - L - L:.4f},format=yuv420p[v]",
    ]
    master = f"{OUT}/{name}-master.mkv"     # intermédiaire quasi sans perte, d'où partent les deux encodages
    subprocess.run(["ffmpeg", "-v", "error", "-y", *inputs, "-filter_complex", ";".join(fc), "-map", "[v]", "-an",
                    "-r", str(FPS), "-c:v", "libx264", "-preset", "medium", "-crf", "8", "-pix_fmt", "yuv420p", master], check=True)
    col = ["-color_primaries", "bt709", "-color_trc", "bt709", "-colorspace", "bt709"]
    out = f"{OUT}/{name}.mp4"              # H.264 : Safari, Chrome, Edge, Firefox
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", master, "-c:v", "libx264", "-preset", "slower", "-crf", str(crf),
                    "-profile:v", "high", "-pix_fmt", "yuv420p", "-g", "48", *col, "-movflags", "+faststart", out], check=True)
    webm = f"{OUT}/{name}.webm"            # VP9 : navigateurs sans H.264 (Chromium libre)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", master, "-c:v", "libvpx-vp9", "-crf", str(crf + 9), "-b:v", "0",
                    "-deadline", "good", "-cpu-used", "2", "-row-mt", "1", "-g", "48", "-pix_fmt", "yuv420p", *col, webm], check=True)
    os.remove(master)
    # affiche : l'image du volume de lignes posé sur le papier (3,8 s), nette et dans la marque, en WebP
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", "3.8", "-i", out, "-frames:v", "1", "-c:v", "libwebp", "-quality", "84",
                    f"{OUT}/{name}.webp"], check=True)
    print("ok", out)

if __name__ == "__main__":
    os.makedirs(OUT, exist_ok=True)
    for v in VARIANTES:
        build(*v)
