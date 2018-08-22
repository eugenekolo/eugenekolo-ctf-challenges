#include <QtMultimedia/QMediaPlayer>
#include <QQuickView>
#include <QQmlEngine>
#include <QGuiApplication>
#include <QQmlContext>

#include "auth.h"

int main(int argc, char *argv[]) {
    QGuiApplication app(argc, argv); // The parent QT logic thread

    app.setOrganizationName("eugenekolo");
    app.setOrganizationDomain("eugenekolo.com");
    app.setApplicationName("cutie keygen");

    QQuickView qmlView;
    qmlView.setSource(QUrl("qrc:/kickass.qml"));
    qmlView.connect(qmlView.engine(), &QQmlEngine::quit, &app, &QCoreApplication::quit);
    qmlView.setMaximumWidth(512);
    qmlView.setMaximumHeight(384);
    qmlView.setMinimumWidth(512);
    qmlView.setMinimumHeight(384);
    qmlView.setTitle("cutie keygen");

    qmlView.show();

    Auth auth;
    QQmlContext* ctx = qmlView.rootContext();
    QObject* root = (QObject*)(qmlView.rootObject());

    ctx->setContextProperty("auth", &auth);

    QObject::connect(&auth,
                     SIGNAL(sendToQml(int)),
                     root,
                     SIGNAL(sendToQml(int)));

    return app.exec();
}
