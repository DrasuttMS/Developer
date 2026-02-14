import os
import time
from pathlib import Path
import google.generativeai as genai

# CONFIGURACIÓN
API_KEY = "TU_API_KEY_AQUÍ"  # Consíguela en https://aistudio.google.com
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash') # Modelo rápido y con visión

def renombrar_con_ia(ruta_assets):
    carpeta = Path(ruta_assets).resolve()
    
    print(f"Analizando imágenes en: {carpeta}...")

    for archivo in carpeta.glob('*.png'):
        # Ignorar archivos que ya fueron renombrados (opcional)
        if "_" in archivo.stem and not archivo.stem.split('_')[0].isalnum():
            continue

        try:
            # 1. Cargar la imagen
            img_data = {
                'mime_type': 'image/png',
                'data': archivo.read_bytes()
            }

            # 2. Preguntar a la IA
            prompt = "Describe esta imagen de videojuego en 3 palabras simples separadas por guiones bajos. Solo las palabras, ejemplo: personaje_pescando_pixelart. Si es un objeto, ejemplo: espada_madera_item."
            
            response = model.generate_content([prompt, img_data])
            nuevo_nombre_base = response.text.strip().lower().replace(" ", "_").replace(".", "")
            
            # Limpiar caracteres extraños por si la IA se pone creativa
            nuevo_nombre_base = "".join(c for c in nuevo_nombre_base if c.isalnum() or c == '_')

            # 3. Renombrar
            nuevo_nombre = f"{nuevo_nombre_base}.png"
            ruta_nueva = carpeta / nuevo_nombre

            # Evitar sobrescribir si el nombre ya existe
            contador = 1
            while ruta_nueva.exists():
                ruta_nueva = carpeta / f"{nuevo_nombre_base}_{contador}.png"
                contador += 1

            archivo.rename(ruta_nueva)
            print(f"Renombrado: {archivo.name} -> {ruta_nueva.name}")
            
            # Pausa breve para no saturar la API gratuita
            time.sleep(1)

        except Exception as e:
            print(f"Error procesando {archivo.name}: {e}")

if __name__ == "__main__":
    ruta = input("Ingresa la ruta de tu carpeta 'assets': ").strip().replace('"', '')
    renombrar_con_ia(ruta)
