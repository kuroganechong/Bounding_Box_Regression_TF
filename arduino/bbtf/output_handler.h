#ifndef OUTPUT_HANDLER_H
#define OUTPUT_HANDLER_H

#include "tensorflow/lite/c/c_api_internal.h"
#include "tensorflow/lite/experimental/micro/micro_error_reporter.h"

// Called every time the results of a person detection run are available. The
// `person_score` has the numerical confidence that the captured image contains
// a person, and `no_person_score` has the numerical confidence that the image
// does not contain a person. Typically if person_score > no person score, the
// image is considered to contain a person.  This threshold may be adjusted for
// particular applications.
void RespondToDetection(tflite::ErrorReporter* error_reporter,float xA, float yA, float xB, float yB);

#endif