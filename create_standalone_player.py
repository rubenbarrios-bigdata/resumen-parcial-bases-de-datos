import base64
import os

html_path = "reproductor_estudio.html"
with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

tracks = [
    "00_Resumen_Completo_Repaso_Total_Parcial.mp3",
    "01_Diseno_Conceptual_DER_y_Claves.mp3",
    "02_Relaciones_y_Cardinalidades.mp3",
    "03_Proceso_de_Normalizacion_1FN_2FN_3FN.mp3",
    "04_Introduccion_a_SQL_DDL_y_DML.mp3",
    "05_Tipos_de_Datos_y_Sintaxis_CREATE_TABLE.mp3"
]

for track in tracks:
    mp3_file = os.path.join("audios_estudio", track)
    if os.path.exists(mp3_file):
        with open(mp3_file, "rb") as mf:
            b64_data = base64.b64encode(mf.read()).decode("ascii")
            data_uri = f"data:audio/mp3;base64,{b64_data}"
            # Replace relative source path
            rel_src = f'src="audios_estudio/{track}"'
            new_src = f'src="{data_uri}"'
            content = content.replace(rel_src, new_src)
            # Replace download link to download data uri with filename
            old_download = f'href="audios_estudio/{track}"'
            new_download = f'href="{data_uri}" download="{track}"'
            content = content.replace(old_download, new_download)

standalone_path = "reproductor_estudio_autocontenido.html"
with open(standalone_path, "w", encoding="utf-8") as f:
    f.write(content)

print(f"Creado: {standalone_path} ({os.path.getsize(standalone_path)} bytes)")
