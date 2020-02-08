//
// EPITECH PROJECT, 2018
// audio
// File description:
// Wrapper for C audio library.
//


#include <cstdio>
#include <cstdlib>
#include "audio.h"


using namespace std;


AudioWrapper::AudioWrapper() {
    PaError err;

    // initialize wrapped library
    // TODO: might want to do this only once when load the audio file
    // instead of per object instantiation
    // because multiple audio objects may be instantiated?
    // TODO: replace this boilerplate "error" code with #define macros?
    err = Pa_Initialize();
    if (err != paNoError) paError(err);

    // initialize stream with default audio device
    // TODO: select device, customize number of channels for input and output
    err = Pa_OpenDefaultStream(
        &_stream,
        channels,
        channels,
        SAMPLE_FORMAT,
        sampleRate,
        framesPerBuffer,
        NULL,   // we will use blocking IO instead of the callback method
        NULL);
    if (err != paNoError) paError(err);

    // start audio processing streams
    // TODO: may want to wait until the first call to record() before starting the stream
    err = Pa_StartStream(_stream);
    if (err != paNoError) paError(err);
}


AudioWrapper::AudioWrapper(int channels, 
                           double sampleRate, 
                           unsigned long framesPerBuffer):
    channels(channels), sampleRate(sampleRate), framesPerBuffer(framesPerBuffer) {
    AudioWrapper();
};


AudioWrapper::~AudioWrapper() {
    PaError err;

    // stop audio processing streams
    err = Pa_StopStream(_stream);
    if (err != paNoError) paError(err);

    // terminate wrapped library
    err = Pa_Terminate();
    if (err != paNoError) paError(err);
};


void AudioWrapper::record(SAMPLE_TYPE *buffer) {
    PaError err;

    err = Pa_ReadStream(_stream, buffer, framesPerBuffer);
    if (err != paNoError) paError(err);
};


void AudioWrapper::play(SAMPLE_TYPE *buffer) {
    PaError err;

    err = Pa_WriteStream(_stream, buffer, framesPerBuffer);
    if (err == paOutputUnderflowed) {
        printf("Output underflowed. Ignoring \n");
    } else if (err != paNoError) {
        paError(err);
    }
};


/**
 * Report PortAudio errors and terminate the library.
 * 
**/
void paError(PaError err) {
    fprintf(stderr, "An error occured while using PortAudio.\n");
    fprintf(stderr, "Error number: %d.\n", err);
    fprintf(stderr, "Error message: %s.\n", Pa_GetErrorText(err));

    err = Pa_Terminate();
    // TODO: report error
    fprintf(stderr, "Exiting.\n");
    exit(84);
}