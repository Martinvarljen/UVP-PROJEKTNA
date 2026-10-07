from bs4 import BeautifulSoup
from Ciscenje_podatkov import ocisti_podatek   




def izlusci_delnice(pot):
    with open(pot, encoding="utf-8") as f:
        vsebina = f.read()

    soup = BeautifulSoup(vsebina, "html.parser")

    vrstice = soup.find_all("tr", class_="styled-row")
    
    delnice = []                                    

    for vrstica in vrstice:
        celice = [td.get_text(strip=True) for td in vrstica.find_all("td")]


        celica_oznaka = vrstica.find("td", attrs={"data-boxover-ticker": True})
        oznaka = celica_oznaka["data-boxover-ticker"]


        delnica = {
            "oznaka": oznaka,
            "podjetje": celice[2],
            "sektor": celice[3],
            "panoga": celice[4],
            "drzava": celice[5],
            "trzna_kapitalizacija": ocisti_podatek(celice[6]),
            "dividenda": ocisti_podatek(celice[7]),
            "donos": ocisti_podatek(celice[8]),
            "obseg": ocisti_podatek(celice[9]),
            "cena": ocisti_podatek(celice[10]),
        }

        delnice.append(delnica)                
    return delnice
