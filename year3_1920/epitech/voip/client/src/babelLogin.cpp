#include "babelLogin.h"

babelLogin::babelLogin():
    QWidget(),
    ui(new Ui::babelLogin)
{
    ui->setupUi(this);
    mySize = size();
    connect(ui->login, SIGNAL(clicked()), this, SLOT(sendUser()));
}

babelLogin::~babelLogin()
{
    delete ui;
}

QSize babelLogin::SizeHint() const
{
    return mySize;
}

void babelLogin::sendUser()
{
    QString usr = ui->username->text();
    emit gotUsername(usr);
}