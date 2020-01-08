#ifndef IMAGEPROVIDER_H
#define IMAGEPROVIDER_H

#include "tensorflow/lite/c/c_api_internal.h"
#include "tensorflow/lite/experimental/micro/micro_error_reporter.h"

TfLiteStatus GetImage(tflite::ErrorReporter* error_reporter, int image_width,
                      int image_height, int channels, short *image_data);

#endif
