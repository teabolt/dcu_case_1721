#pragma once

#include <QObject>
#include "audio.h"

class SoundController : public QObject {
    Q_OBJECT
    
    public:
        AudioWrapper audio;
        int bufferSize;
        int bufferSizeBytes;
        float* audioInputBuffer;
        float* audioOutputBuffer;

        SoundController();
        ~SoundController();
        void start();

signals:
    void soundReady(float*);
};