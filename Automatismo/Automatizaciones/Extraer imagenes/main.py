import shutil
from pathlib import Path

def extraer_pngs():
    # Solicita la ruta directamente al usuario
    ruta_input = input(r"Pega la ruta de la carpeta (ej. C:\Users\Nombre\Carpeta): ").strip()
    
    # Quitamos comillas si el usuario las pegó por error
    ruta_input = ruta_input.replace('"', '').replace("'", "")
    
    origen = Path(ruta_input).resolve()
    
    # Verifica si la ruta existe
    if not origen.exists():
        print(f"Error: La ruta '{origen}' no existe. Revisa que esté bien escrita.")
        return

    # La carpeta 'assets' se creará dentro de la carpeta que ingresaste
    destino = origen / "assets"
    
    if not destino.exists():
        destino.mkdir(parents=True, exist_ok=True)

    nombres_vistos = set()
    contador = 0

    print(f"\nBuscando PNGs en: {origen}...")

    # rglob('*') busca en todas las carpetas y subcarpetas
    for archivo_path in origen.rglob('*'):
        
        # Evitar entrar en la propia carpeta 'assets' y filtrar solo archivos PNG
        if "assets" not in archivo_path.parts and archivo_path.is_file():
            if archivo_path.suffix.lower() == '.png':
                nombre_archivo = archivo_path.name
                
                # Solo copiar si el nombre no se ha procesado antes
                if nombre_archivo not in nombres_vistos:
                    try:
                        shutil.copy2(archivo_path, destino / nombre_archivo)
                        nombres_vistos.add(nombre_archivo)
                        contador += 1
                        print(f"Copiado: {nombre_archivo}")
                    except Exception as e:
                        print(f"No se pudo copiar {nombre_archivo}: {e}")

    print(f"\n¡Listo! Se guardaron {contador} PNGs únicos en: {destino}")

if __name__ == "__main__":
    extraer_pngs()
