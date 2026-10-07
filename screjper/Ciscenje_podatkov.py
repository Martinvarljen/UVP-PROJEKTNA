def ocisti_podatek(besedilo):
    if besedilo == "-" or besedilo == "":
        return None

    besedilo = besedilo.replace(",", "")

    if besedilo.endswith("%"):
        return float(besedilo[:-1])
    if besedilo.endswith("T"):
        return float(besedilo[:-1]) * 1e12
    if besedilo.endswith("B"):
        return float(besedilo[:-1]) * 1e9
    if besedilo.endswith("M"):
        return float(besedilo[:-1]) * 1e6

    return float(besedilo)