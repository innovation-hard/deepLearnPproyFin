# Importación del guión de película a Df y limpieza
# Entrada: Jerry.Maguire.1996.Blu-ray.1080p.x264.HDBRiSe.SPA.srt
# Salida: subtítulos.csv

import pandas as pd
import re


# Ruta del archivo de subtítulos
ruta_archivo = "Jerry.Maguire.1996.Blu-ray.1080p.x264.HDBRiSe.SPA.srt"


# Cargar el archivo de subtítulos
with open(ruta_archivo, "r", encoding="latin-1") as f:
    contenido = f.read()

# Dividir el contenido en bloques separados por líneas en blanco
bloques = contenido.strip().split("\n\n")

# Listas para almacenar los datos
inicio = []
fin = []
subtitulos = []

# Procesar cada bloque
for bloque in bloques:
    lineas = bloque.split("\n")
    if len(lineas) < 3:
        continue  # Saltar bloques incompletos

    # Extraer el rango de tiempo
    tiempo = lineas[1]
    tiempo_match = re.match(r"(\d{2}:\d{2}:\d{2},\d{3}) --> (\d{2}:\d{2}:\d{2},\d{3})", tiempo)
    if tiempo_match:
        inicio.append(tiempo_match.group(1))
        fin.append(tiempo_match.group(2))
    else:
        inicio.append(None)
        fin.append(None)

    # Unir las líneas de texto del subtítulo
    texto = " ".join(lineas[2:]).strip()
    # Eliminar etiquetas como <i> o </i>
    texto_limpio = re.sub(r"<.*?>", "", texto)
    subtitulos.append(texto_limpio)

# Crear el DataFrame
df = pd.DataFrame({
    "inicio": inicio,
    "fin": fin,
    "subtitulo": subtitulos
})

print(df.sample(5))

df.to_csv("subtitulos.csv", index=False, encoding="utf-8")
