#ifndef AUTH_H
#define AUTH_H

#include <QObject>
#include <QGenericMatrix>
#include <stdint.h>

class Auth : public QObject
{
  Q_OBJECT
  public:
    explicit Auth(QObject *parent = 0);
  private:
    bool initAuth(void);
    bool checkInitAuth(void);
    bool checkPassword(QString s);
    QString* confusion(QString s);
    QGenericMatrix<4,4,uint64_t>* transform(QString s);
    QGenericMatrix<4,4,uint64_t>* multiply(QGenericMatrix<4,4,uint64_t>);

    QGenericMatrix<4,4,uint64_t>* m_mult_matrix;
    QGenericMatrix<4,4,uint64_t>* m_ans_matrix;

    QVector<uint16_t>* m_confusion_array;
    uint64_t m_speck_key[2];

  signals:
    void sendToQml(int resp);
  public slots:
    void receiveFromQml(QString str);

};


#endif // AUTH_H
