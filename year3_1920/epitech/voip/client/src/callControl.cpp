#include "callControl.h"

callControl::callControl(QObject *parent) :
    QObject(parent)
{
    _connected = false;
}

callControl::~callControl()
{
}

void callControl::connect(QString ip)
{   
    if(ip.size())
    {
        try
        {

            if (!_connected) {
                host = QHostAddress(ip);
                socket.connect(BABELPORT);

                QObject::connect(socket.socket, SIGNAL(readyRead()), this, SLOT(receiveSoundPacket()));
                QObject::connect(&sound, SIGNAL(soundReady(float*)), this, SLOT(sendSoundPacket(float*)));

                _connected = true;
            }

        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
            return;
        }
        
        int durationSeconds = 30;
        int totalFrames = sound.audio.sampleRate * durationSeconds;
        int numBlocks = totalFrames / sound.audio.framesPerBuffer;
        for (int i = 0; i < numBlocks; i++) {
            printf("sending block=%d\n", i);
            sound.start();
        }
    }
}

void callControl::receiveSoundPacket()
{
    QByteArray data = socket.recieveData();
    float* soundBuffer = (float*) data.toStdString().c_str();

    //REPRODUCE SOUND
    printf("receiving some sound...\n");
    sound.audio.play(soundBuffer);
}

void callControl::sendSoundPacket(float* buffer) {
    printf("sending some sound...\n");
    char* payload = (char*) buffer;
    int size = sound.bufferSizeBytes;

    socket.sendData(payload, size, host);
}
