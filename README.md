# Analiza dividendnih delnic (Finviz)

Projektna naloga pri predmetu Uvod v programiranje. Program zajame podatke o 1000 delnicah z najvišjim dividendnim donosom s spletne strani [Finviz](https://finviz.com/screener.ashx) (oznaka, podjetje, sektor, panoga, država, tržna kapitalizacija, dividenda, dividendni donos, obseg trgovanja, cena). Upoštevana so le podjetja, ki izplačujejo dividendo in imajo tržno kapitalizacijo nad 2 milijardi USD. Nato izvede analizo in vizualizacijo podatkov.

## Struktura projekta

- `screjper/Spletne_strani.py` – Prenese HTML strani s Finviza in jih shrani v `PODATKI/SPLETNE_STRANI/`.
- `screjper/Izlusci.py` – Iz shranjenih HTML strani izlušči podatke o delnicah.
- `screjper/Ciscenje_podatkov.py` – Pretvori vrednosti, kot so `4.78B`, `29.73%` in `30,904`, v števila.
- `screjper/Naredi_csv.py` – Zapiše izluščene podatke v `PODATKI/delnice.csv`.
- `screjper/Main.py` – Glavna skripta, ki požene celoten postopek.
- `analiza.ipynb` – Jupyter notebook z analizo in grafi.
- `PODATKI/` – Mapa s shranjenimi HTML stranmi (`SPLETNE_STRANI/`) in končno CSV datoteko (`delnice.csv`).

## Namestitev

1. **Ustvarite in aktivirajte virtualno okolje:**
```bash
   python3 -m venv .venv
   source .venv/bin/activate
```
   (na Windows: `.venv\Scripts\activate`)

2. **Namestite potrebne knjižnice:**
```bash
   pip install requests beautifulsoup4 pandas matplotlib jupyter
```

## Zagon

Celoten postopek (prenos HTML strani → izluščenje podatkov → shranjevanje v CSV) poženete iz glavne mape projekta z:

```bash
python screjper/Main.py
```

Privzeto se prenese 50 strani (1000 delnic). Strani, ki so že shranjene v `PODATKI/SPLETNE_STRANI/`, program preskoči, zato se ob ponovnem zagonu ne prenašajo znova. Med prenosi program počaka 1 sekundo, da Finviz ne blokira dostopa.

Ko je `PODATKI/delnice.csv` ustvarjen, odprite `analiza.ipynb` (npr. v VS Code ali Jupyterju) in poženite celice od zgoraj navzdol. Notebook je že izveden, zato so grafi vidni tudi brez ponovnega zagona.

