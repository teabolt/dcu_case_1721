#include "SoundControl.h"


SoundController::SoundController() {
    bufferSize = audio.framesPerBuffer * audio.channels; // interleaved channels
    bufferSizeBytes = bufferSize * sizeof(SAMPLE_TYPE);

    audioInputBuffer = new SAMPLE_TYPE[bufferSize];
    audioOutputBuffer = new SAMPLE_TYPE[bufferSize];
}


SoundController::~SoundController() {}


void SoundController::start() 
{
    audio.record(audioInputBuffer);
    emit soundReady(audioInputBuffer);
}