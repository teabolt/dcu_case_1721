
#include "client.h"
#include <QtWidgets/QApplication>

int main(int argc, char **argv)
{
	QApplication app(argc, argv);
	client client;
	client.start();	
	return app.exec();
}