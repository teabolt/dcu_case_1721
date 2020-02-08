#pragma once

#include <portaudio.h>

#define SAMPLE_FORMAT paFloat32
typedef float SAMPLE_TYPE;


class AudioWrapper {
    private:
        PaStream* _stream;

    public:
        int channels = 2;
        double sampleRate = 48000;
        unsigned long framesPerBuffer = 128;

        AudioWrapper();
        AudioWrapper(int channels, double sampleRate, unsigned long framesPerBuffer);
        ~AudioWrapper();
        void record(SAMPLE_TYPE *buffer);
        void play(SAMPLE_TYPE *buffer);
};


void paError(PaError err);