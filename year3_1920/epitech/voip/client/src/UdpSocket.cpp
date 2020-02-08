#include "UdpSocket.h"

UdpSocket::UdpSocket()
{
    socket = new QUdpSocket(this);
}

UdpSocket::~UdpSocket()
{
    disconnect();
    if(socket)
        delete socket;
}

void UdpSocket::disconnect()
{
    if(socket->state() != QAbstractSocket::UnconnectedState)
        socket->close();
}

void UdpSocket::sendData(char * msg,int size ,QHostAddress host)
{
    socket->writeDatagram(msg, size, host, BABELPORT);
}

QByteArray UdpSocket::recieveData()
{
    //TODO BUILD A PACKAGE
    QByteArray data;
    QHostAddress sender;
    quint16 port;
    data.resize(socket->pendingDatagramSize());

    socket->readDatagram(data.data(), data.size(), &sender, &port);
    return data;
}

void UdpSocket::connect(int port)
{
    disconnect();
    socket->bind(QHostAddress::Any, port);
}
