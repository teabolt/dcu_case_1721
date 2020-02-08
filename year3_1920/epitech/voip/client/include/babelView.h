#pragma once

#include <QWidget>
#include <iostream>
#include "UdpSocket.h"
#include "ui_babelView.h"

class babelView : public QWidget
{
    Q_OBJECT
public:
    babelView();
    ~babelView();
    QSize minimumSizeHint() const;
private:
    QSize mySize;
    UdpSocket cSocket;
    Ui::babelView ui;
    QHostAddress host;

public slots:
    void leerSocket();
    void send();
    void connectChat();
};


