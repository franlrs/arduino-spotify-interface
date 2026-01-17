import serial
import time
import win32gui # Librería específica de Windows

# --- CONFIGURACIÓN ---
SERIAL_PORT = 'COM3'  # <--- Cambia esto si tu puerto es diferente (ej: COM4, COM5)
# ---------------------

print("--- RADIO SPOTIFY (METODO WINDOWS) ---")

try:
    arduino = serial.Serial(SERIAL_PORT, 9600)
    time.sleep(2) # Esperar reinicio
    print(f"Conectado a {SERIAL_PORT}. Esperando música...")
except:
    print("ERROR: No se pudo conectar al Arduino. Revisa el puerto.")
    exit()

def encontrar_spotify():
    """Busca una ventana que tenga ' - ' en el título (típico de Artista - Cancion)"""
    cancion_detectada = ""
    
    def callback(hwnd, extra):
        nonlocal cancion_detectada
        titulo = win32gui.GetWindowText(hwnd)
        # Spotify Free/Premium suele poner "Spotify" cuando está pausado
        # Cuando reproduce, pone "Artista - Cancion"
        # Buscamos una ventana visible que no esté vacía
        if win32gui.IsWindowVisible(hwnd) and len(titulo) > 0:
            # Filtro simple: Si el titulo tiene un guión y NO es el navegador
            if " - " in titulo and "Google Chrome" not in titulo and "Edge" not in titulo:
                # Asumimos que es Spotify (o YouTube music en app)
                # Esto es un truco, pero suele funcionar
                cancion_detectada = titulo

    win32gui.EnumWindows(callback, None)
    return cancion_detectada

ultima_cancion = ""

while True:
    try:
        titulo_ventana = encontrar_spotify()
        
        # Si encontramos algo y es diferente a lo anterior
        if titulo_ventana and titulo_ventana != ultima_cancion:
            # Separar Artista y Cancion (Spotify usa "Autor - Tema")
            if " - " in titulo_ventana:
                # El formato de ventana suele ser "Artista - Cancion"
                partes = titulo_ventana.split(" - ", 1)
                if len(partes) >= 2:
                    artista = partes[0].strip()
                    cancion = partes[1].strip()
                    
                    # Limpieza de caracteres raros
                    reemplazos = (("á", "a"), ("é", "e"), ("í", "i"), ("ó", "o"), ("ú", "u"), ("ñ", "n"))
                    for a, b in reemplazos:
                        artista = artista.replace(a, b).replace(a.upper(), b.upper())
                        cancion = cancion.replace(a, b).replace(a.upper(), b.upper())

                    # Enviar al Arduino: Cancion*Artista
                    mensaje = f"{cancion}*{artista}\n"
                    print(f"Detectado: {mensaje.strip()}")
                    arduino.write(mensaje.encode())
                    ultima_cancion = titulo_ventana
            
    except Exception as e:
        print(f"Error: {e}")
        
    time.sleep(2)