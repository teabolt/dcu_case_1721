#pragma once

#include <QWidget>
#include "ui_babelCall.h"

namespace Ui {
class babelCall;
}

class babelCall : public QWidget
{
    Q_OBJECT

public:
    babelCall();
    ~babelCall();
    QSize minimumSizeHint() const;
private:
    Ui::babelCall *ui;
    QSize mySize;

private slots:
    void tryCall();

signals:
    void call(QString);
};
