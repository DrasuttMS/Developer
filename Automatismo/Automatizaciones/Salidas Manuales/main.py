import pandas as pd
import os
import pyautogui
import pyperclip
import time
from pynput import keyboard  # Requiere: pip install pynput

# --- CONFIGURACIÓN DE RUTAS ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_EXCEL = os.path.join(BASE_DIR, "SM.xlsx")

COLUMNAS_OBJETIVO = ['LPN', 'LPN_DESTINO', 'EAN', 'UNIDADES']
ETI_INICIAL = '00000000000'

# --- LÓGICA DE ESCAPE (TECLA ESC) ---
running = True

def on_press(key):
    global running
    if key == keyboard.Key.esc:
        print("\n[!] DETENCIÓN SOLICITADA: Tecla Esc presionada.")
        running = False
        return False  # Detiene el listener

# Iniciar el escuchador de teclado en segundo plano
listener = keyboard.Listener(on_press=on_press)
listener.start()

if not os.path.exists(ARCHIVO_EXCEL):
    print(f"Error: El archivo NO se encontró en: {ARCHIVO_EXCEL}")
else:
    try:
        df = pd.read_excel(ARCHIVO_EXCEL)
        df.columns = df.columns.str.strip()
        
        if set(COLUMNAS_OBJETIVO).issubset(df.columns):
            df_final = df[COLUMNAS_OBJETIVO].dropna(how='all').reset_index(drop=True)
            
            print(f"Registros cargados: {len(df_final)}")
            print("Selecciona la ventana de PuTTY. Iniciamos en 2 segundos...")
            time.sleep(2)

            for index, fila in df_final.iterrows():
                # --- VERIFICACIÓN DE ESCAPE ---
                if not running:
                    break 

                LPN = str(fila['LPN']).strip()
                LPN_DESTINO = str(fila['LPN_DESTINO']).strip()
                EAN = str(fila['EAN']).strip()
                UNIDADES = str(fila['UNIDADES']).strip()

                print(f"Procesando fila {index + 1}/{len(df_final)}: {LPN} / {LPN_DESTINO} / {EAN} / {UNIDADES}")

                # Lógica de automatización
                if LPN_DESTINO == ETI_INICIAL:
                    #Copiar y pegar EAN y Unidades
                    pyperclip.copy(EAN)
                    pyautogui.click(button='right') 
                    time.sleep(0.4)
                    pyautogui.press('enter', presses=2, interval=0.2) 
                    pyperclip.copy(UNIDADES)
                    pyautogui.click(button='right') 
                    time.sleep(0.4)
                    pyautogui.press('enter', presses=1, interval=0.2)

                else:
                    pyautogui.hotkey('ctrl', 'e')
                    pyautogui.hotkey('ctrl', 'n')
                    time.sleep(0.5)
                    pyperclip.copy(LPN_DESTINO)
                    pyautogui.click(button='right')
                    time.sleep(0.4)
                    pyautogui.press('enter', presses=1, interval=0.2)
                    pyperclip.copy(EAN)
                    pyautogui.click(button='right')
                    time.sleep(0.4)
                    pyautogui.press('enter', presses=2, interval=0.2)
                    pyperclip.copy(UNIDADES)
                    pyautogui.click(button='right')
                    time.sleep(0.4)
                    pyautogui.press('enter', presses=1, interval=0.2)
                time.sleep(0.5)  # Espera entre filas

                # --- CLAVE: ACTUALIZAR LA ETIQUETA PARA LA PRÓXIMA FILA ---
                ETI_INICIAL = LPN_DESTINO

            if not running:
                print("--- PROCESO INTERRUMPIDO POR EL USUARIO ---")
            else:
                time.sleep(0.5)
                pyautogui.hotkey('ctrl', 'e')
                pyautogui.hotkey('ctrl', 'n')
                print("--- PROCESO FINALIZADO EXITOSAMENTE ---")
        else:
            print(f"Error: Columnas no encontradas. Las columnas son: {list(df.columns)}")
    except Exception as e:
        print(f"Error inesperado: {e}")
