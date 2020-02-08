#include "tcpSocket.h"

tcpSocket::tcpSocket()
{
    socket = new QTcpSocket(this);
}

tcpSocket::~tcpSocket()
{
    disconnect();
    if(socket)
        delete socket;
}

void tcpSocket::disconnect()
{
    if(socket->state() == QAbstractSocket::ConnectedState)
        socket->disconnectFromHost();
}

void tcpSocket::sendData(Message & msg)
{
    if(socket->write(msg.data.toStdString().c_str(), msg.mySize) == -1)
        throw -1;
}

Message tcpSocket::recieveData()
{
    int size = socket->bytesAvailable();
    Message msg;
    msg.mySize = 0;
    if(size == 0)
        return msg;
    char * buffer = new char[size];
    socket->read(buffer, size);

    msg.data = buffer;
    msg.mySize = size;
    msg.port = socket->peerPort();
    msg.sender = socket->peerAddress().toString();
    return msg;
}

void tcpSocket::connect(QString ip , int port)
{
    disconnect();
    socket->connectToHost(ip, port);
    if(!socket->waitForConnected(-1))
        throw -1;

    QObject::connect(socket, SIGNAL(readyRead()), this, SLOT(recieveData()));
}
