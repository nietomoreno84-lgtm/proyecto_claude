"""Combina los CSV mensuales de una carpeta de ventas en un único archivo,
añadiendo una columna 'mes_origen' con el nombre del archivo de procedencia."""

import csv
import sys
from pathlib import Path


def combinar_csv(carpeta_entrada: str, archivo_salida: str) -> int:
    carpeta = Path(carpeta_entrada)
    if not carpeta.is_dir():
        raise FileNotFoundError(f"No existe la carpeta de entrada: {carpeta}")

    archivos_csv = sorted(
        p for p in carpeta.glob("*.csv") if p.resolve() != Path(archivo_salida).resolve()
    )
    if not archivos_csv:
        raise FileNotFoundError(f"No se encontraron archivos .csv en: {carpeta}")

    filas_combinadas = []
    columnas = None

    for archivo in archivos_csv:
        with archivo.open(newline="", encoding="utf-8") as f:
            lector = csv.DictReader(f)
            if lector.fieldnames and "mes_origen" in lector.fieldnames:
                # Salida generada previamente por este script (p. ej. una ejecución
                # anterior con otra ruta de salida dejó el archivo en esta carpeta).
                # No es un CSV de origen, así que se ignora en vez de tratarlo como uno.
                continue
            if columnas is None:
                columnas = lector.fieldnames
            elif lector.fieldnames != columnas:
                raise ValueError(
                    f"Las columnas de {archivo.name} ({lector.fieldnames}) "
                    f"no coinciden con las del primer archivo ({columnas})"
                )
            mes_origen = archivo.stem
            for fila in lector:
                fila["mes_origen"] = mes_origen
                filas_combinadas.append(fila)

    if columnas is None:
        raise FileNotFoundError(
            f"No se encontraron archivos .csv de origen en: {carpeta} "
            "(solo se hallaron salidas generadas previamente)"
        )

    columnas_salida = list(columnas) + ["mes_origen"]
    ruta_salida = Path(archivo_salida)
    ruta_salida.parent.mkdir(parents=True, exist_ok=True)
    with ruta_salida.open("w", newline="", encoding="utf-8") as f:
        escritor = csv.DictWriter(f, fieldnames=columnas_salida)
        escritor.writeheader()
        escritor.writerows(filas_combinadas)

    return len(filas_combinadas)


if __name__ == "__main__":
    carpeta_entrada = sys.argv[1] if len(sys.argv) > 1 else "ventas"
    archivo_salida = sys.argv[2] if len(sys.argv) > 2 else str(Path(carpeta_entrada) / "ventas_combinado.csv")

    try:
        total_filas = combinar_csv(carpeta_entrada, archivo_salida)
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)

    print(f"Combinados {total_filas} filas en: {archivo_salida}")
