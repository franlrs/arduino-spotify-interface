#include <LiquidCrystal.h>
// Pines del Elegoo Kit: RS=7, E=8, D4=9, D5=10, D6=11, D7=12
LiquidCrystal lcd(7, 8, 9, 10, 11, 12);

void setup() {
  Serial.begin(9600);
  lcd.begin(16, 2);
  lcd.print("Esperando payo");
}

void loop() {
  if (Serial.available() > 0) {
    String data = Serial.readStringUntil('\n');
    int corte = data.indexOf('*');
    if (corte != -1) {
      String cancion = data.substring(0, corte);
      String artista = data.substring(corte + 1);
      lcd.clear();
      lcd.setCursor(0, 0); lcd.print(cancion);
      lcd.setCursor(0, 1); lcd.print(artista);
    }
  }
}