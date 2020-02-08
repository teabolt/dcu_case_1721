#pragma once
#include <QObject>
#include <QTcpSocket>
#include <QHostAddress>
#include "message.h"

class tcpSocket : public QObject
{
    Q_OBJECT
private:
    QTcpSocket *socket;
public:
    tcpSocket();
    ~tcpSocket();
    void sendData(Message &); //Send message package TODO
    Message recieveData();
    void connect(QString, int);
    void disconnect();
};
