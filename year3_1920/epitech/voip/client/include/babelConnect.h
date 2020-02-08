#pragma once

#include <QWidget>
#include <QIntValidator>
#include <QString>
#include "ui_babelConnect.h"

namespace Ui {
class babelConnect;
}

class babelConnect : public QWidget
{
    Q_OBJECT

public:
    explicit babelConnect();
    ~babelConnect();
    QSize minimumSizeHint() const;
private:
    Ui::babelConnect *ui;
    QSize mySize;

public slots:
    void enterServerIp();
    void enterPort();
    void tryConexion();

signals:

    void tryServer(QString, qint16);
};
