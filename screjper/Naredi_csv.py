import csv
import os


def zapisi_csv(delnice, pot):
    os.makedirs(os.path.dirname(pot), exist_ok=True)

    stolpci = delnice[0].keys()

    with open(pot, "w", encoding="utf-8", newline="") as f:
        pisec = csv.DictWriter(f, fieldnames=stolpci)
        pisec.writeheader()
        pisec.writerows(delnice)

