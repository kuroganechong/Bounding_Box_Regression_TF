#ifndef MODELSETTINGS_H
#define MODELSETTINGS_H

// Keeping these as constant expressions allow us to allocate fixed-sized arrays
// on the stack for our working memory.

// All of these values are derived from the values used during model training,
// if you change your model you'll need to update these constants.
constexpr char kNumCols = 32;
constexpr char kNumRows = 32;
constexpr char kNumChannels = 1;

constexpr int kMaxImageSize = kNumCols * kNumRows * kNumChannels;

#endif