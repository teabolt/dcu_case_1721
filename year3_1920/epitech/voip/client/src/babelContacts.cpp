#include "babelContacts.h"


babelContacts::babelContacts() :
    QWidget(),
    ui(new Ui::babelContacts)
{
    ui->setupUi(this);
    mySize = size();
}

babelContacts::~babelContacts()
{
    delete ui;
}

QSize babelContacts::minimumSizeHint() const
{
    return mySize;
}