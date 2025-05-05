import os
import requests

seccions = [
    "home", "internacional", "politica", "vida", "deportes", "economia", "opinion",
    "cultura", "gente", "sucesos", "lacontra", "natural", "bigvang", "salud",
    "tecnologia", "television", "series", "viajes", "motor", "magazine", "vivo",
    "mascotas", "mamas-y-papas", "comer"
]

output_dir = os.path.join("rss", "lavanguardia")
os.makedirs(output_dir, exist_ok=True)

for seccio in seccions:
    url = f"https://www.lavanguardia.com/rss/{seccio}.xml"
    desti = os.path.join(output_dir, f"{seccio}.xml")
    try:
        print(f"📥 Descarregant {seccio}...")
        resposta = requests.get(url, timeout=10)
        resposta.raise_for_status()
        with open(desti, "wb") as f:
            f.write(resposta.content)
        print(f"✅ Guardat a {desti}")
    except Exception as e:
        print(f"❌ Error amb la secció '{seccio}': {e}")