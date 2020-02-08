#include "babelCall.h"


babelCall::babelCall() :
    QWidget(),
    ui(new Ui::babelCall)
{
    ui->setupUi(this);   
    mySize = size();
    connect(ui->callButton, SIGNAL(clicked()), this , SLOT(tryCall()));
}

babelCall::~babelCall()
{
    delete ui;
}

QSize babelCall::minimumSizeHint() const
{
    return mySize;
}

void babelCall::tryCall()
{
    QString ip = ui->ipText->text();
    emit call(ip);
}
