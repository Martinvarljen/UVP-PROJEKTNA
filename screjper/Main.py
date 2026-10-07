import os

from Spletne_strani import prenesi_strani, MAPA_PODATKI, MAPA_HTML
from Izlusci import izlusci_delnice
from Naredi_csv import zapisi_csv


def main():

    prenesi_strani(60)


    vse_delnice = []
    for ime_datoteke in sorted(os.listdir(MAPA_HTML)):
        if ime_datoteke.endswith(".html"):
            pot = os.path.join(MAPA_HTML, ime_datoteke)
            vse_delnice.extend(izlusci_delnice(pot))


    zapisi_csv(vse_delnice, os.path.join(MAPA_PODATKI, "delnice.csv"))


if __name__ == "__main__":
    main()