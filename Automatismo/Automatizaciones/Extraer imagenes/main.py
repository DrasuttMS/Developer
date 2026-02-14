import shutil
from pathlib import Path

def extraer_pngs():
    ruta_input = input(r"Pega la ruta de la carpeta: ").strip().replace('"', '').replace("'", "")
    origen = Path(ruta_input).resolve()
    
    if not origen.exists():
        print(f"Error: La ruta '{origen}' no existe.")
        return

    destino = origen / "assets"
    destino.mkdir(parents=True, exist_ok=True)

    nombres_vistos = set()
    contador = 0

    # rglob('*.png') busca recursivamente solo archivos PNG
    for archivo_path in origen.rglob('*.png'):
        
        # Saltamos archivos que ya estén dentro de la carpeta destino
        if destino in archivo_path.parents:
            continue
            
        nombre_archivo = archivo_path.name
        
        if nombre_archivo not in nombres_vistos:
            try:
                shutil.copy2(archivo_path, destino / nombre_archivo)
                nombres_vistos.add(nombre_archivo)
                contador += 1
                print(f"Copiado: {nombre_archivo}")
            except Exception as e:
                print(f"Error en {nombre_archivo}: {e}")

    print(f"\n¡Listo! {contador} archivos únicos en: {destino}")

if __name__ == "__main__":
    extraer_pngs()
