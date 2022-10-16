import pandas as pd

def ingest_data():

    df = pd.read_fwf(
        "clusters_report.txt", widths = [9, 16, 16, 80], header = None,
        names = ["cluster","cantidad_de_palabras_clave","porcentaje_de_palabras_clave", "-"],
        skip_blank_lines = False, converters = {"porcentaje_de_palabras_clave": 
        lambda x: x.rstrip(" %").replace(",",".")}).drop([0,1,2,3], axis=0)

    col4 = df["-"]
    df = df[df["cluster"].notna()].drop("-", axis=1)
    df = df.astype({ "cluster": int, "cantidad_de_palabras_clave": int, "porcentaje_de_palabras_clave": float})

    col4Proc = []
    text = ""
    for lin in col4:
        if isinstance(lin, str): text += lin+" "
        else:
            text = ", ".join([" ".join(x.split()) for x in text.split(",")])
            col4Proc.append(text.rstrip("."))
            text = ""
            continue

    df["principales_palabras_clave"] = col4Proc

    return df
