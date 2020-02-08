#include "client.h"

client::client(): QObject()
{
    connect(&window, SIGNAL(tryCall(QString)), &manager, SLOT(connect(QString)));
}

client::~client()
{
    
}

void client::start()
{
    window.show();
    // thread
}