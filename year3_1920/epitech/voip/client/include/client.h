#pragma once
#include <QObject>
#include "babelWindow.h"
#include "serverControl.h"
#include "callControl.h"


class client : public QObject
{
    Q_OBJECT
private:
    //TODO
    callControl manager;
    //ContactList
    //ServerManager
    babelWindow window;
    //serverControl server;
public:
    client();
    ~client();
    void start();
};


