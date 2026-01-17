# 🎵 Physical Spotify Visualizer (IoT / Window Title Hack)

![Arduino](https://img.shields.io/badge/-Arduino-00979D?style=for-the-badge&logo=Arduino&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

An IoT system that visualizes the current Spotify track on a physical LCD screen. It bridges the digital and physical worlds using **Arduino** and a background **Python** script.

<div align="center">
  <img src="https://github.com/user-attachments/assets/51246f91-9100-40eb-9d30-fdd5fef1aae8" width="200" />
</div>

---

### 💡 The Engineering (The Workaround)

**The Challenge:**
Originally designed to utilize the official Spotify API. However, since Spotify for Developers temporarily disabled the creation of new apps (blocking access to OAuth credentials), a creative alternative was required.

**The Solution:**
I implemented a process monitoring technique on **Windows** (`win32gui`). The Python script:
1.  Scans the OS active windows.
2.  Detects the `Artist - Song` pattern in the Spotify window title.
3.  Cleans and formats the data.
4.  Transmits it via Serial to the microcontroller.

> **Result:** A fully functional system that does not depend on external API keys or internet connection on the microcontroller side.

---

### 🛠️ Hardware & Software

* **Board:** Arduino Uno.
* **Display:** LCD 1602 (with potentiometer for contrast).
* **Languages:** C++ (Arduino) and Python 3.x.
* **Python Libraries:** `pyserial`, `pywin32`.

### 🔌 Wiring (Pinout)

Configuration for the `LiquidCrystal` library:

| LCD Pin | Arduino Pin | Description |
| :--- | :--- | :--- |
| **RS** | 7 | Register Select |
| **E** | 8 | Enable |
| **D4** | 9 | Data 4 |
| **D5** | 10 | Data 5 |
| **D6** | 11 | Data 6 |
| **D7** | 12 | Data 7 |
| **RW** | GND | Write |
| **V0** | Potentiometer | Contrast Adjustment |

---

### 🚀 Installation & Setup Guide

Follow these steps strictly to avoid Serial Port conflicts.

#### Step 1: Flash the Arduino
1.  Open `Spotify_LCD.ino` in Arduino IDE.
2.  Connect your board via USB.
3.  Select the correct Board and Port.
4.  Click **Upload**.

#### ⚠️ Step 2: IMPORTANT - Free the Port
**Once uploaded, COMPLETELY CLOSE THE ARDUINO IDE.**
> If you leave the IDE (or Serial Monitor) open, Python won't be able to access the USB port, triggering an `Access Denied` error.

#### Step 3: Python Environment
Open a terminal (CMD or PowerShell) in the project folder and install dependencies:

```bash
pip install -r requirements.txt
```

#### Step 4: Port Configuration

Open `spotify_lcd.py` with a text editor (or VS Code) and verify the port line:

```python
SERIAL_PORT = 'COM3'  # <--- Make sure this matches your Arduino port
```

#### Step 5: Run it!

1. Open the Spotify desktop app and play some music.
2. In your terminal, run the script:

```bash
python spotify_lcd.py
```

3. If successful, you'll see: *"Connected to COM3. Waiting for music..."* and your LCD will display the track.

---

### 🐛 Troubleshooting

* **`Access is denied` Error:** You didn't close the Arduino IDE! Close it and run the Python script again.
* **White squares on LCD:** Adjust the potentiometer on the back or breadboard to fix the contrast.
* **Song not detected:** Ensure you are using the Spotify Desktop App (not the web player) and that it's not minimized to the system tray.

---

### 📄 License

Project developed by **franlrs**. Distributed under the [MIT License](LICENSE).



