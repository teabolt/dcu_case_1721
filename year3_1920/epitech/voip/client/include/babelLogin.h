#pragma once

#include <QWidget>
#include "ui_babelLogin.h"

namespace Ui {
class babelLogin;
}

class babelLogin : public QWidget
{
    Q_OBJECT
public:
    explicit babelLogin();
    ~babelLogin();
    QSize SizeHint() const;

private:
    Ui::babelLogin *ui;
    QSize mySize;

public slots:
    void sendUser();

signals:
    void gotUsername(QString);

};
