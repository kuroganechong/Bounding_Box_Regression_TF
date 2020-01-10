#ifndef IMAGEPROVIDER_H
#define IMAGEPROVIDER_H

#include "tensorflow/lite/c/c_api_internal.h"
#include "tensorflow/lite/experimental/micro/micro_error_reporter.h"

TfLiteStatus GetImage(tflite::ErrorReporter* error_reporter, char image_width,
                      char image_height, char channels, float *image_data);

#endif
