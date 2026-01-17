# 🎵 Physical Spotify Visualizer (IoT / Window Title Hack)

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

Sistema IoT que visualiza la canción actual de Spotify en una pantalla LCD física. Conecta el mundo digital con el hardware utilizando **Arduino** y un script de **Python** en segundo plano.

<div align="center">
  <img src="![demo](https://github.com/user-attachments/assets/b9bc75ae-46d7-4ad8-9bd6-127984fe2318)
" width="250" />
</div>

---

### 💡 Ingeniería del Proyecto (The Workaround)

**El Desafío:**
Originalmente diseñado para usar la API oficial de Spotify. Sin embargo, debido a que Spotify for Developers deshabilitó la creación de nuevas apps (impidiendo obtener credenciales OAuth), fue necesario buscar una alternativa creativa.

**La Solución:**
Implementé una técnica de monitoreo de procesos en **Windows** (`win32gui`). El script de Python:
1.  Escanea las ventanas activas del sistema operativo.
2.  Detecta el patrón `Artista - Canción` en el título de la ventana de Spotify.
3.  Limpia y formatea los datos.
4.  Los transmite vía Serial al microcontrolador.

> **Resultado:** Un sistema funcional que no depende de claves API externas ni conexión a internet en el microcontrolador.

---

### 🛠️ Hardware y Software

* **Placa:** Arduino Uno.
* **Pantalla:** LCD 1602 (con potenciómetro para contraste).
* **Lenguajes:** C++ (Arduino) y Python 3.x.
* **Librerías Python:** `pyserial`, `pywin32`.

### 🔌 Conexiones (Pinout)

Configuración para la librería `LiquidCrystal`:

| LCD Pin | Arduino Pin | Descripción |
| :--- | :--- | :--- |
| **RS** | 7 | Register Select |
| **E** | 8 | Enable |
| **D4** | 9 | Data 4 |
| **D5** | 10 | Data 5 |
| **D6** | 11 | Data 6 |
| **D7** | 12 | Data 7 |
| **RW** | GND | Escritura |
| **V0** | Potenciómetro | Ajuste de contraste |

---

### 🚀 Guía de Instalación y Ejecución

Sigue estos pasos en orden estricto para evitar conflictos con el puerto serie.

#### Paso 1: Carga el código en Arduino
1.  Abre el archivo `Spotify_LCD.ino` en el IDE de Arduino.
2.  Conecta tu placa al PC por USB.
3.  Selecciona tu placa y puerto correcta.
4.  Dale al botón **Subir** (Upload).

#### ⚠️ Paso 2: IMPORTANTE - Libera el Puerto
**Una vez subido el código, CIERRA COMPLETAMENTE EL ARDUINO IDE.**
> Si dejas el IDE abierto (o el Monitor Serie), Python no podrá acceder al puerto USB porque estará ocupado, lanzando un error de `Access Denied`.

#### Paso 3: Prepara el entorno Python
Abre una terminal (CMD o PowerShell) en la carpeta del proyecto e instala las dependencias:

```bash
pip install -r requirements.txt
```

#### Paso 4: Configura el puerto

Abre el archivo `spotify_lcd.py` con un editor de texto (o VS Code) y verifica esta línea al principio:

```python
SERIAL_PORT = 'COM3'  # <--- Asegúrate de que este es el puerto de tu Arduino
```

#### Paso 5: ¡A funcionar!

1. Abre la aplicación de escritorio de Spotify y pon música.
2. En tu terminal, ejecuta el script:

```bash
python spotify_lcd.py
```

3. Si todo va bien, verás en la terminal: *"Conectado a COM3. Esperando música..."* y tu pantalla LCD mostrará la canción actual.

---

### 🐛 Solución de Problemas Frecuentes

* **Error `Access is denied`:** ¡No cerraste el Arduino IDE! Ciérralo y vuelve a ejecutar el script de Python.
* **El LCD muestra cuadrados blancos:** Ajusta el potenciómetro de contraste en la parte trasera o en la protoboard.
* **No detecta la canción:** Asegúrate de que estás usando la aplicación de escritorio de Spotify (no la web) y que no está minimizada en la bandeja del sistema.

---

### 📄 Licencia

Proyecto desarrollado por **franlrs**. Distribuido bajo licencia [MIT](https://www.google.com/search?q=LICENSE).

