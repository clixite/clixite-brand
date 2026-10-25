"""Modèles Word Clixite : papier à lettre et modèle d'offre."""
from docx import Document
from docx.shared import Pt, Cm, RGBColor, Emu
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_BREAK
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.enum.section import WD_SECTION
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

L = "charte/downloads/logo"
INK = RGBColor(0x0B, 0x22, 0x39); SLATE = RGBColor(0x4B, 0x5A, 0x6B); TURQ_T = RGBColor(0x0C, 0x78, 0x93); MIST = "CDD5DD"; PAPER = "F6F5F0"

def set_cell_bg(cell, hexcolor):
    tcPr = cell._tc.get_or_add_tcPr(); shd = OxmlElement("w:shd")
    shd.set(qn("w:val"), "clear"); shd.set(qn("w:color"), "auto"); shd.set(qn("w:fill"), hexcolor); tcPr.append(shd)

def set_table_borders(table, color=MIST, sz=4):
    tbl = table._tbl; tblPr = tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "left", "bottom", "right", "insideH", "insideV"):
        el = OxmlElement(f"w:{edge}"); el.set(qn("w:val"), "single"); el.set(qn("w:sz"), str(sz)); el.set(qn("w:space"), "0"); el.set(qn("w:color"), color); borders.append(el)
    tblPr.append(borders)

def base_document():
    doc = Document()
    sec = doc.sections[0]
    sec.page_width = Cm(21); sec.page_height = Cm(29.7)
    sec.left_margin = sec.right_margin = Cm(2.2); sec.top_margin = Cm(3.2); sec.bottom_margin = Cm(2.6)
    sec.header_distance = Cm(1.0); sec.footer_distance = Cm(1.0)
    st = doc.styles
    normal = st["Normal"]; normal.font.name = "Inter"; normal.font.size = Pt(10.5); normal.font.color.rgb = INK
    normal.element.rPr.rFonts.set(qn("w:eastAsia"), "Inter")
    normal.paragraph_format.space_after = Pt(8); normal.paragraph_format.line_spacing = 1.3
    for name, size, color, before in (("Heading 1", 22, INK, 18), ("Heading 2", 15, INK, 14), ("Heading 3", 12, TURQ_T, 10)):
        h = st[name]; h.font.name = "Space Grotesk"; h.font.size = Pt(size); h.font.bold = True; h.font.color.rgb = color
        h.element.rPr.rFonts.set(qn("w:eastAsia"), "Space Grotesk"); h.element.rPr.rFonts.set(qn("w:ascii"), "Space Grotesk"); h.element.rPr.rFonts.set(qn("w:hAnsi"), "Space Grotesk")
        h.paragraph_format.space_before = Pt(before); h.paragraph_format.space_after = Pt(6)
    t = st["Title"]; t.font.name = "Space Grotesk"; t.font.size = Pt(30); t.font.bold = True; t.font.color.rgb = INK
    t.element.rPr.rFonts.set(qn("w:ascii"), "Space Grotesk"); t.element.rPr.rFonts.set(qn("w:hAnsi"), "Space Grotesk")
    pPr = t.element.get_or_add_pPr()
    for bd in pPr.findall(qn("w:pBdr")): pPr.remove(bd)
    # styles nommés propres à la charte
    from docx.enum.style import WD_STYLE_TYPE
    if "Étiquette Clixite" not in [x.name for x in st]:
        e = st.add_style("Étiquette Clixite", WD_STYLE_TYPE.PARAGRAPH); e.base_style = st["Normal"]
        e.font.name = "JetBrains Mono"; e.font.size = Pt(8); e.font.bold = True; e.font.color.rgb = TURQ_T; e.font.all_caps = True
        e.element.rPr.rFonts.set(qn("w:ascii"), "JetBrains Mono"); e.element.rPr.rFonts.set(qn("w:hAnsi"), "JetBrains Mono")
        e.paragraph_format.space_after = Pt(2); e.paragraph_format.space_before = Pt(12)
    if "Citation Clixite" not in [x.name for x in st]:
        q = st.add_style("Citation Clixite", WD_STYLE_TYPE.PARAGRAPH); q.base_style = st["Normal"]
        q.font.name = "Fraunces"; q.font.size = Pt(15); q.font.italic = True; q.font.color.rgb = INK
        q.element.rPr.rFonts.set(qn("w:ascii"), "Fraunces"); q.element.rPr.rFonts.set(qn("w:hAnsi"), "Fraunces")
        q.paragraph_format.space_before = Pt(12); q.paragraph_format.space_after = Pt(12); q.paragraph_format.left_indent = Cm(0.8)
    if "Chiffre Clixite" not in [x.name for x in st]:
        c = st.add_style("Chiffre Clixite", WD_STYLE_TYPE.PARAGRAPH); c.base_style = st["Normal"]
        c.font.name = "Space Grotesk"; c.font.size = Pt(28); c.font.bold = True; c.font.color.rgb = INK
        c.element.rPr.rFonts.set(qn("w:ascii"), "Space Grotesk"); c.element.rPr.rFonts.set(qn("w:hAnsi"), "Space Grotesk")
        c.paragraph_format.space_after = Pt(0)
    # header: logo left, descriptor right
    header = sec.header; hp = header.paragraphs[0]; hp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    hp.add_run().add_picture(os.path.join(L, "clixite-relief-color-transparent-1600px.png"), width=Cm(4.2))
    # footer: company line
    footer = sec.footer; fp = footer.paragraphs[0]; fp.alignment = WD_ALIGN_PARAGRAPH.LEFT
    r = fp.add_run("Clixite SRL · Avenue Reine Astrid 53, 1300 Wavre · BE 0871.430.776 · nicolas@clixite.be · clixite.be"); r.font.size = Pt(8); r.font.color.rgb = SLATE; r.font.name = "Inter"
    fp2 = footer.add_paragraph(); r2 = fp2.add_run("ENTERPRISE & SOLUTION ARCHITECTURE"); r2.font.size = Pt(7.5); r2.font.color.rgb = TURQ_T; r2.font.name = "Space Grotesk"; r2.font.bold = True
    return doc

def add_label(doc, text):
    p = doc.add_paragraph(text, style="Étiquette Clixite")
    return p

# ---------------------------------------------------------------- letter
doc = base_document()
add_label(doc, "Wavre, le [date]")
p = doc.add_paragraph(); r = p.add_run("[Prénom Nom]\n[Fonction]\n[Société]\n[Adresse]"); r.font.color.rgb = SLATE
p.paragraph_format.space_after = Pt(18)
h = doc.add_paragraph(); r = h.add_run("Objet : [objet de la lettre]"); r.bold = True
doc.add_paragraph("Madame, Monsieur,")
doc.add_paragraph("[Premier paragraphe : le contexte en deux phrases. Les faits avant les adjectifs.]")
doc.add_paragraph("[Deuxième paragraphe : ce que nous proposons, avec un chiffre ou une échéance concrète.]")
doc.add_paragraph("[Troisième paragraphe : la prochaine étape, qui fait quoi et quand.]")
doc.add_paragraph("Je reste à votre disposition pour en parler de vive voix.")
doc.add_paragraph("Bien à vous,")
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(24); r = p.add_run("Nicolas Simon"); r.bold = True; r.font.name = "Space Grotesk"
p = doc.add_paragraph(); r = p.add_run("Solutions & Enterprise Architect · Clixite SRL\n+32 (0)4xx xx xx xx · nicolas@clixite.be"); r.font.color.rgb = SLATE; r.font.size = Pt(9.5)
doc.save("charte/downloads/office/Clixite-papier-a-lettre.docx")

# ---------------------------------------------------------------- offer
doc = base_document()
# cover
cov = doc.add_paragraph(); cov.paragraph_format.space_before = Pt(60)
cov.add_run().add_picture(os.path.join(L, "x-relief-color-transparent-1024px.png"), width=Cm(4.5))
add_label(doc, "Proposition de services")
t = doc.add_paragraph(style="Title"); t.add_run("[Titre de la mission]")
p = doc.add_paragraph(); r = p.add_run("[Client] · [date] · version 1.0"); r.font.color.rgb = SLATE; r.font.size = Pt(12)
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(120); r = p.add_run("Préparée par Nicolas Simon, Clixite SRL\nDocument confidentiel, à l'attention de [Prénom Nom]"); r.font.color.rgb = SLATE; r.font.size = Pt(9.5)
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

doc.add_heading("Sommaire", level=1)
for i, s in enumerate(["Contexte et enjeu", "Ce que nous proposons", "Livrables", "Planning", "Équipe", "Budget", "Conditions"], 1):
    p = doc.add_paragraph(f"{i}.  {s}"); p.paragraph_format.space_after = Pt(2)
doc.add_paragraph().add_run().add_break(WD_BREAK.PAGE)

doc.add_heading("1. Contexte et enjeu", level=1)
doc.add_paragraph("[Trois à cinq phrases : la situation du client, le x à résoudre, ce qui se passe si rien ne change. Chiffres et faits.]")
doc.add_paragraph("« [Une phrase du client, telle qu'il l'a dite, qui résume l'enjeu.] »", style="Citation Clixite")
doc.add_heading("Ce que nous avons compris", level=2)
for b in ["[Enjeu 1, formulé du point de vue du client]", "[Enjeu 2]", "[Enjeu 3]"]:
    doc.add_paragraph(b, style="List Bullet")
doc.add_heading("2. Ce que nous proposons", level=1)
doc.add_paragraph("[La proposition en une phrase, puis l'approche en trois étapes.]")
for i, (nm, d) in enumerate([("Cadrer", "[Audit, périmètre, critères de succès]"), ("Construire", "[Architecture, outils, playbooks]"), ("Livrer", "[Mise en production, formation, transfert]")], 1):
    doc.add_heading(f"Étape {i} · {nm}", level=3); doc.add_paragraph(d)
doc.add_heading("3. Livrables", level=1)
tbl = doc.add_table(rows=4, cols=3); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER; set_table_borders(tbl)
hdr = ["Livrable", "Format", "Échéance"]
for i, h in enumerate(hdr):
    c = tbl.rows[0].cells[i]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.name = "Space Grotesk"; set_cell_bg(c, PAPER)
for ri, row in enumerate([["[Livrable 1]", "[Doc, outil, atelier]", "[Semaine 2]"], ["[Livrable 2]", "", "[Semaine 6]"], ["[Livrable 3]", "", "[Semaine 12]"]], 1):
    for ci, v in enumerate(row): tbl.rows[ri].cells[ci].text = v
doc.add_heading("4. Planning", level=1)
doc.add_paragraph("[Durée totale, jalons, réunions de pilotage. Un planning simple vaut mieux qu'un Gantt.]")
doc.add_heading("5. Équipe", level=1)
doc.add_paragraph("Nicolas Simon, Solutions & Enterprise Architect. Plus de quinze ans en banque, télécom et assurance (KBC, Proximus, P&V) et en PME en croissance. Certifié PMP, PRINCE2, SAFe, ITIL.")
doc.add_heading("6. Budget", level=1)
tbl = doc.add_table(rows=4, cols=4); tbl.alignment = WD_TABLE_ALIGNMENT.CENTER; set_table_borders(tbl)
for i, h in enumerate(["Poste", "Jours", "Tarif journalier", "Total HTVA"]):
    c = tbl.rows[0].cells[i]; c.text = ""; r = c.paragraphs[0].add_run(h); r.bold = True; r.font.name = "Space Grotesk"; set_cell_bg(c, PAPER)
for ri, row in enumerate([["[Étape 1]", "[x]", "[xxx €]", "[x xxx €]"], ["[Étape 2]", "[x]", "[xxx €]", "[x xxx €]"], ["Total", "", "", "[xx xxx €]"]], 1):
    for ci, v in enumerate(row):
        tbl.rows[ri].cells[ci].text = v
        if ri == 3: tbl.rows[ri].cells[ci].paragraphs[0].runs[0].bold = True
doc.add_paragraph("Prix hors TVA, facturation mensuelle à 30 jours. Frais de déplacement inclus en Belgique.")
doc.add_heading("7. Conditions", level=1)
doc.add_paragraph("[Durée, engagement, préavis, propriété des livrables, confidentialité. Renvoyer au contrat de services Clixite.]")
p = doc.add_paragraph(); p.paragraph_format.space_before = Pt(30); r = p.add_run("Pour accord, le [date]\n\n\n\nNicolas Simon, Clixite SRL                                        [Nom], [Société]"); r.font.color.rgb = SLATE
doc.save("charte/downloads/office/Clixite-modele-offre.docx")
print("docx ok")
