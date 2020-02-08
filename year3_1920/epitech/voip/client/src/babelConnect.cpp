#include "babelConnect.h"


babelConnect::babelConnect() :
    QWidget(), ui(new Ui::babelConnect)
{
    ui->setupUi(this);
    mySize = size();  
    connect(ui->nextPage, SIGNAL(clicked()), this, SLOT(tryConexion()));
    ui->enterPort->setValidator( new QIntValidator(1024, 65535, this));
}

babelConnect::~babelConnect()
{
    delete ui;
}

QSize babelConnect::minimumSizeHint() const
{
    return mySize;
}

void babelConnect::enterServerIp()
{
}

void babelConnect::enterPort()
{
}

void babelConnect::tryConexion()
{
    qint16 port = ui->enterPort->text().toInt();
    QString ip = ui->enterIP->text();
    emit tryServer(ip, port);
}
