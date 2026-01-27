import pandas as pd
import os
import pyautogui
import pyperclip
import time

# --- CAMBIO AQUÍ: RUTA DINÁMICA ---
# Obtiene la carpeta exacta donde vive este script main.py
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Une esa carpeta con el nombre del archivo Excel
ARCHIVO_EXCEL = os.path.join(BASE_DIR, "cancel.xlsx")
# ---------------------------------


COLUMNAS_OBJETIVO = ['TASK_GRP', 'TASK', 'BARRA']
GRUPO_INICIAL = "D1"

if not os.path.exists(ARCHIVO_EXCEL):
    print(f"Error: El archivo NO se encontró en: {ARCHIVO_EXCEL}")
else:
    try:
        # 1. Carga y limpieza de datos
        # Usamos engine='openpyxl' por seguridad en entornos modernos
        df = pd.read_excel(ARCHIVO_EXCEL)
        df.columns = df.columns.str.strip()
        
        if set(COLUMNAS_OBJETIVO).issubset(df.columns):
            df_final = df[COLUMNAS_OBJETIVO].dropna(how='all').reset_index(drop=True)
            
            print(f"Registros cargados: {len(df_final)}")
            print("Selecciona la ventana de PuTTY. Iniciamos en 2 segundos...")
            time.sleep(2)

            for index, fila in df_final.iterrows():
                task_grp = str(fila['TASK_GRP']).strip()
                task = str(fila['TASK']).strip()
                barra = str(fila['BARRA']).strip()

                print(f"Procesando fila {index + 1}: {task_grp} / {task}")

                if task_grp == GRUPO_INICIAL:
                    pyautogui.hotkey('ctrl', 't')
                    pyperclip.copy(task_grp)
                    pyautogui.click(button='right') 
                    time.sleep(0.3)
                    pyautogui.press('enter', presses=2, interval=0.2) 

                    pyautogui.hotkey('ctrl', 'e')
                    pyperclip.copy(task)
                    pyautogui.click(button='right')
                    time.sleep(0.3)
                    pyautogui.press('enter', presses=1, interval=0.2)
                    
                    pyperclip.copy(barra)
                    pyautogui.click(button='right')
                    pyautogui.press('enter')
                    time.sleep(0.2)
                    pyautogui.hotkey('ctrl', 'n')
                else:
                    pyautogui.hotkey('ctrl', 'w')
                    pyautogui.hotkey('ctrl', 't')
                    pyperclip.copy(task_grp)
                    pyautogui.click(button='right') 
                    time.sleep(0.3)
                    pyautogui.press('enter', presses=2, interval=0.2)

                    pyautogui.hotkey('ctrl', 'e')
                    pyperclip.copy(task)
                    pyautogui.click(button='right')
                    time.sleep(0.3)
                    pyautogui.press('enter', presses=1, interval=0.2)

                    pyperclip.copy(barra)
                    pyautogui.click(button='right')
                    pyautogui.press('enter')
                    time.sleep(0.2)
                    pyautogui.hotkey('ctrl', 'n')

                GRUPO_INICIAL = task_grp  # Actualiza el grupo al final de cualquier bloque
                time.sleep(1) 

            print("--- PROCESO FINALIZADO ---")
        else:
            print(f"Error: Columnas no encontradas. Las columnas son: {list(df.columns)}")
    except Exception as e:
        print(f"Error inesperado: {e}")
