#include "output_handler.h"

#include "Arduino.h"

// The pin of the Arduino's built-in LED
int led = LED_BUILTIN;

// Track whether the function has run at least once
bool initialized = false;

// Animates a dot across the screen to represent the current x and y values
void RespondToDetection(tflite::ErrorReporter* error_reporter,float xA, float yA, float xB, float yB) {
  // Do this only once
  if (!initialized) {
    // Set the LED pin to output
    pinMode(led, OUTPUT);
    initialized = true;
  }

  error_reporter->Report("xA: %f, yA: %f, xB: %f, yB: %f\n\n", xA, yA, xB, yB);

  digitalWrite(led,LOW);
  delay(100);
  digitalWrite(led,HIGH);
}
