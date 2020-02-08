
#pragma once

#include <QMainWindow>
#include <QWidget>
#include "ui_babelContacts.h"

using namespace std;

namespace Ui {
class babelContacts;
}

class babelContacts : public QWidget
{
    Q_OBJECT

public:
    explicit babelContacts();
    ~babelContacts();
    QSize minimumSizeHint() const;
private:
    Ui::babelContacts *ui;
    QSize mySize;
};
