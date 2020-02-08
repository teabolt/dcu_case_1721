#include "babelView.h"

babelView::babelView(): QWidget()
{
    ui.setupUi(this);
    this->setWindowTitle("Babel--Main Page");
    mySize = size();
    connect(ui.sendB, SIGNAL(clicked()), this, SLOT(send()));
    connect(ui.connectB , SIGNAL(clicked()), this, SLOT(connectChat()));
}

babelView::~babelView()
{
}

QSize babelView::minimumSizeHint() const 
{
	return mySize;
}

void babelView::connectChat()
{   
    QString ip = ui.conIP->text();

    if(ip.size())
    {
        try
        {
            host = QHostAddress(ip);
            cSocket.connect(BABELPORT);
            
        }
        catch(const std::exception& e)
        {
            std::cerr << e.what() << '\n';
            return;
        }  
        connect(cSocket.socket, SIGNAL(readyRead()), this, SLOT(leerSocket()));
        ui.connectB->setDisabled(true);
        ui.conIP->setReadOnly(true);      
    }
}

void babelView::leerSocket()
{
    QByteArray data = cSocket.recieveData();
    ui.toRecieve->appendPlainText(QString(data) + "\n");
}

void babelView::send()
{
    //cSocket.sendData(ui.toSend->text().toStdString(), host);
    ui.toSend->clear();
}