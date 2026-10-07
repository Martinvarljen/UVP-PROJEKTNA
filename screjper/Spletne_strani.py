import os 
import time
import requests

MAPA_PODATKI = "PODATKI"

MAPA_HTML = os.path.join(MAPA_PODATKI, "SPLETNE_STRANI")



def prenesi_strani(stevilo_strani=50):
    prvi_url = "https://finviz.com/screener.ashx?v=152&f=cap_midover,fa_div_pos&o=-dividendyield&c=0,1,2,3,4,5,6,75,14,67,65"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    os.makedirs(MAPA_HTML, exist_ok=True)
    
    for stran in range(1, stevilo_strani + 1):
        if stran == 1:
            url = prvi_url
        else:
            zacetek = 1 + (stran - 1) * 20
            url = f"{prvi_url}&r={zacetek}"

        pot = os.path.join(MAPA_HTML, f"stran_{stran:02d}.html")
        
        if os.path.exists(pot):
            print(f"Stran {stran} že obstaja, preskočim.")
            continue

        odgovor = requests.get(url, headers=headers)

        if odgovor.status_code != 200:
            print(f"Napaka ({odgovor.status_code}) na strani {stran}")
            continue

        with open(pot, "w", encoding="utf-8") as f:
            f.write(odgovor.text)
        print(f"Shranjena stran {stran}/{stevilo_strani}")
    
        time.sleep(1)