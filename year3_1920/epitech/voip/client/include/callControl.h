#pragma once

#include "UdpSocket.h"
#include "SoundControl.h"
#include <iostream>
using namespace std;

class callControl : public QObject
{
    Q_OBJECT

public:
    explicit callControl(QObject *parent = 0);
    ~callControl();
private:
    UdpSocket socket;
    QHostAddress host;
    SoundController sound;
    bool _connected;

public slots:
    void receiveSoundPacket();
    void sendSoundPacket(float*);
    void connect(QString);

};