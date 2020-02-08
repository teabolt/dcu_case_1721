#pragma once
#include <QObject>
#include <QUdpSocket>
#include <QHostAddress>
#include <string>

#define BABELPORT 6754

class UdpSocket : public QObject
{
    Q_OBJECT
private:
    
public:
    UdpSocket();
    ~UdpSocket();
    void sendData(char *,int , QHostAddress); //Send message package TODO
    QByteArray recieveData();
    void connect(int port);
    void disconnect();
    QUdpSocket *socket;
    
};
