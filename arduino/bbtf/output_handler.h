#ifndef OUTPUT_HANDLER_H
#define OUTPUT_HANDLER_H

#include "tensorflow/lite/c/c_api_internal.h"
#include "tensorflow/lite/experimental/micro/micro_error_reporter.h"

// Called by the main loop to produce some output based on the x and y values
void HandleOutput(tflite::ErrorReporter* error_reporter, float x_value,
                  float y_value);

#endif