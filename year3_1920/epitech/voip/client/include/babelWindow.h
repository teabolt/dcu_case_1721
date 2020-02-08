#pragma once
#include <QMainWindow>
#include <QStackedWidget>
#include "babelView.h"
#include "babelLogin.h"
#include "babelConnect.h"
#include "babelContacts.h"
#include "babelCall.h"

class babelWindow : public QMainWindow
{
    Q_OBJECT
private:
    //Add a QStackedWidget and inlude all the windows
    QStackedWidget *central;
    babelView * view;
    babelLogin * login;
    babelCall * call;
    babelConnect * conexion;
    babelContacts * contacts;

public:
    babelWindow(/* args */);
    ~babelWindow();
    void setCenter(QWidget *);
    void show();

public slots:
    void logIn(QString);
    void connectServer(QString, qint16);
    void sendCall(QString);

signals:
    void tryCall(QString);

};