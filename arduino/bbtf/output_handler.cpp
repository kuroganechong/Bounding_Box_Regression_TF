#include "output_handler.h"

#include "Arduino.h"

// The pin of the Arduino's built-in LED
const int led = LED_BUILTIN;

// Pins for the built-in RGB LEDs on the Arduino Nano 33 BLE Sense
const int led_red = 22;
const int led_green = 23;
const int led_blue = 24;

// Track whether the function has run at least once
bool initialized = false;

// Print result to serial output
void RespondToDetection(tflite::ErrorReporter* error_reporter,float xA, float yA, float xB, float yB) {
  // Do this only once
  if (!initialized) {
    // Set the LED pin to output
    pinMode(led, OUTPUT);
    pinMode(led_red, OUTPUT);
    pinMode(led_green, OUTPUT);
    pinMode(led_blue, OUTPUT);
    
    digitalWrite(led_green, HIGH);
    digitalWrite(led_red, HIGH);
    digitalWrite(led_blue, HIGH);
    initialized = true;
  }

  // Note: The RGB LEDs on the Arduino Nano 33 BLE
  // Sense are on when the pin is LOW, off when HIGH.
  char tbs[20];
  sprintf(tbs, "%.2f,%.2f,%.2f,%.2f\n", xA, yA, xB, yB);
  error_reporter->Report(tbs);

  digitalWrite(led,LOW);
  delay(100);
  digitalWrite(led,HIGH);

  if(xA > 0 && xB > 0 && yA > 0 && yB > 0){
    digitalWrite(led_green, LOW);
    digitalWrite(led_red, HIGH);
  } else {
    digitalWrite(led_green, HIGH);
    digitalWrite(led_red, LOW);
  }
}
