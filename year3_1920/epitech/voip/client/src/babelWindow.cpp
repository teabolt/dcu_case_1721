#include "babelWindow.h"

babelWindow::babelWindow() :
    login(new babelLogin), view(new babelView), 
    call(new babelCall), conexion(new babelConnect),
    contacts(new babelContacts)
{
    this->setWindowTitle("International Babel");

    central = new QStackedWidget;
    setCentralWidget(central);

    central->addWidget(view);
    central->addWidget(login);
    central->addWidget(call);
    central->addWidget(conexion);
    central->addWidget(contacts);
    connect(call , SIGNAL(call(QString)), this, SLOT(sendCall(QString)));
    connect(login, SIGNAL(gotUsername(QString)), this, SLOT(logIn(QString)));
    connect(conexion, SIGNAL(tryServer(QString, qint16)), this, SLOT(connectServer(QString, qint16)));
}

babelWindow::~babelWindow()
{

}

void babelWindow::show()
{
    setCenter(call);
    QMainWindow::show();
}

void babelWindow::setCenter(QWidget * widget)
{
    central->setCurrentWidget(widget);
    central->currentWidget()->setSizePolicy(QSizePolicy::Fixed, QSizePolicy::Fixed);
    widget->adjustSize();
    adjustSize();
}

void babelWindow::logIn(QString usr)
{
    setCenter(contacts);
}

void babelWindow::connectServer(QString ip, qint16 port)
{
    setCenter(login);
}

void babelWindow::sendCall(QString ip)
{
    emit tryCall(ip);
}