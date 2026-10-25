"""Gestion des enregistrements de la zone DNS clixite.be chez OVH, par l'API (clé limitée à /domain/zone/clixite.be/*).

Usage :
  python3 scripts/ovh_dns.py list
  python3 scripts/ovh_dns.py upsert charte A 1.2.3.4
  python3 scripts/ovh_dns.py upsert charte CNAME clixite.be.
  python3 scripts/ovh_dns.py delete charte A

Variables d'environnement : OVH_ENDPOINT (ovh-eu), OVH_APP_KEY, OVH_APP_SECRET, OVH_CONSUMER_KEY, OVH_ZONE (clixite.be).
"""
import os, sys
import ovh

ZONE = os.environ.get("OVH_ZONE", "clixite.be")
client = ovh.Client(endpoint=os.environ.get("OVH_ENDPOINT", "ovh-eu"), application_key=os.environ["OVH_APP_KEY"],
                    application_secret=os.environ["OVH_APP_SECRET"], consumer_key=os.environ["OVH_CONSUMER_KEY"])

def records(sub=None, ftype=None):
    q = {}
    if sub is not None: q["subDomain"] = sub
    if ftype: q["fieldType"] = ftype
    return [client.get(f"/domain/zone/{ZONE}/record/{i}") for i in client.get(f"/domain/zone/{ZONE}/record", **q)]

cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
if cmd == "list":
    for r in sorted(records(), key=lambda r: (r["subDomain"], r["fieldType"])):
        print(f'{r["subDomain"] or "@":<20} {r["fieldType"]:<6} {r["target"]:<40} ttl={r["ttl"]} id={r["id"]}')
elif cmd == "upsert":
    sub, ftype, target = sys.argv[2], sys.argv[3].upper(), sys.argv[4]
    existing = records(sub, ftype)
    if existing:
        client.put(f'/domain/zone/{ZONE}/record/{existing[0]["id"]}', target=target)
        print(f"mis à jour : {sub} {ftype} -> {target} (id {existing[0]['id']})")
    else:
        r = client.post(f"/domain/zone/{ZONE}/record", fieldType=ftype, subDomain=sub, target=target, ttl=0)
        print(f"créé : {sub} {ftype} -> {target} (id {r['id']})")
    client.post(f"/domain/zone/{ZONE}/refresh"); print("zone rafraîchie")
elif cmd == "delete":
    sub, ftype = sys.argv[2], sys.argv[3].upper()
    for r in records(sub, ftype):
        client.delete(f'/domain/zone/{ZONE}/record/{r["id"]}'); print(f"supprimé : {sub} {ftype} (id {r['id']})")
    client.post(f"/domain/zone/{ZONE}/refresh"); print("zone rafraîchie")
else:
    sys.exit(__doc__)
