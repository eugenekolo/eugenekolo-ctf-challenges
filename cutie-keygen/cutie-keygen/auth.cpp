#include "auth.h"
#include <QDebug>
#include <QGenericMatrix>
#include <QMatrix4x4>
#include <stdint.h>
#include <QVector4D>

Auth::Auth(QObject *parent) : QObject(parent) {
    initAuth();
}

bool Auth::initAuth(void) {

    uint64_t _vals[] = {4992,   1252,   9993,   8245,
                        9722,  22234,   259,  5425,
                        3242,    6753,   3591,   32,
                        226,   4671,     192,  3527};
    m_mult_matrix = new QGenericMatrix<4,4,uint64_t>(_vals);

    // This is BKP{KYU7EC!PH3R}
    uint64_t _vals2[] = {342868586, 607388058, 380802638, 503103844,
                         276196100, 526903709, 328226818, 346660259,
                         719703660, 1078504063, 869243743, 739251810,
                         771095780, 1277609804, 752195599, 732552923};

    m_ans_matrix = new QGenericMatrix<4,4,uint64_t>(_vals2);

    uint16_t _vals3[] = {0x90df, 0x70bc, 0xef57, 0x5a96,
                         0xcfee, 0x5509, 0x80ce, 0x0d20,
                         0xe14f, 0x070e, 0xa446, 0x2fc6,
                         0xecf0, 0x5355, 0x782b, 0x6457};

    m_confusion_array = new QVector<uint16_t>();

    for (int i = 0; i < 16; i++) {
        m_confusion_array->append(_vals3[i]);
    }

    m_speck_key[0] = 0x16d856af880f0e3a;
    m_speck_key[1] = 0xd8e8367c058ff310;

    return true;
}

bool Auth::checkPassword(QString s) {
    if (s.length() != 16) {
        return false;
    }

    s = *confusion(s);
    QGenericMatrix<4,4,uint64_t> m = *transform(s);
    QGenericMatrix<4,4,uint64_t> n = *multiply(m);

    if (n != *m_ans_matrix) {
        return false;
    }

    return true;
}

QString* Auth::confusion(QString s) {
    QString* newString = new QString(s);
    for (int i = 0; i < 16; i++) {
        newString->replace(i, 1, m_confusion_array->at(i) ^ (newString->at(i).toLatin1()));
    }

    return newString;
}

QGenericMatrix<4,4,uint64_t>* Auth::transform(QString s) {
    uint64_t y[2] = {(((uint64_t)s[0].unicode() << 48) | ((uint64_t)s[1].unicode() << 32) |
                      ((uint64_t)s[2].unicode() << 16) | ((uint64_t)s[3].unicode()  << 0)),

                     (((uint64_t)s[8].unicode() << 48) | ((uint64_t)s[9].unicode() << 32) |
                      ((uint64_t)s[10].unicode() << 16)| ((uint64_t)s[11].unicode() << 0))};

    uint64_t x[2] = {(((uint64_t)s[4].unicode() << 48) | ((uint64_t)s[5].unicode() << 32)  |
                      ((uint64_t)s[6].unicode() << 16)  | ((uint64_t)s[7].unicode()  << 0)),

                     (((uint64_t)s[12].unicode() << 48)| ((uint64_t)s[13].unicode() << 32) |
                      ((uint64_t)s[14].unicode() << 16) | ((uint64_t)s[15].unicode() << 0))};
    uint64_t ct[4] = {0x000000000000000, 0x0000000000000000, 0x000000000000000, 0x0000000000000000};

    // Speck says
    //Key: 0f0e0d0c0b0a0908 0706050403020100
    //Plaintext: 6c61766975716520 7469206564616d20
    //key0 = 0x0f0e0d0c0b0a0908; //test
    //key1 = 0x0706050403020100; //test
    //ct[1] = 0x6c61766975716520; //test
    //ct[0] = 0x7469206564616d20; //test

    // Encrypt 4 qwords using a 128-bit key
    #define R(x,y,k) x=(x>>8|x<<56),x+=y,x^=k,y=y<<3|y>>61,y^=x

    uint64_t key0 = m_speck_key[0];
    uint64_t key1 = m_speck_key[1];
    ct[0] = x[0];
    ct[1] = y[0];
    for (uint64_t i = 0; i < 32; i++) {
        R(ct[1], ct[0], key1);
        R(key0, key1, i);
    }

    key0 = m_speck_key[0];
    key1 = m_speck_key[1];
    ct[2] = x[1];
    ct[3] = y[1];
    for (uint64_t i = 0; i < 32; i++) {
        R(ct[3], ct[2], key1);
        R(key0, key1, i);
    }

    uint64_t vals[] = {
        (uint64_t)((ct[1] & 0xffff000000000000) >> 48), (uint64_t)((ct[0] & 0xffff000000000000) >> 48), (uint64_t)((ct[3] & 0xffff000000000000) >> 48), (uint64_t)((ct[2] & 0xffff000000000000) >> 48),
        (uint64_t)((ct[1] & 0x0000ffff00000000) >> 32), (uint64_t)((ct[0] & 0x0000ffff00000000) >> 32), (uint64_t)((ct[3] & 0x0000ffff00000000) >> 32), (uint64_t)((ct[2] & 0x0000ffff00000000) >> 32),
        (uint64_t)((ct[1] & 0x00000000ffff0000) >> 16), (uint64_t)((ct[0] & 0x00000000ffff0000) >> 16), (uint64_t)((ct[3] & 0x00000000ffff0000) >> 16), (uint64_t)((ct[2] & 0x00000000ffff0000) >> 16),
        (uint64_t)((ct[1] & 0x000000000000ffff) >> 0), (uint64_t)((ct[0] & 0x000000000000ffff) >> 0), (uint64_t)((ct[3] & 0x000000000000ffff) >> 0), (uint64_t)((ct[2] & 0x000000000000ffff) >> 0)};

    QGenericMatrix<4,4,uint64_t>* mat = new QGenericMatrix<4,4,uint64_t>(vals);

    return mat;
}

QGenericMatrix<4,4,uint64_t>* Auth::multiply(QGenericMatrix<4,4,uint64_t> m) {
    QGenericMatrix<4,4,uint64_t>* n = new QGenericMatrix<4,4,uint64_t>;
    *n = (m * *(m_mult_matrix));
    return n;
}

void Auth::receiveFromQml(QString s) {
    QString password;
    qDebug() << "Authing";

    // Remove whitespace from password
    for (int i = 0; i < s.length(); i ++) {
        if (s[i] != ' ' && s[i] != '_') {
            password.append(s[i]);
        }
    }

    if (checkPassword(password)) {
        qDebug() << "YES!";
        sendToQml(0);
    } else {
        qDebug() << "NOPE :(";
        sendToQml(-1);
    }
}

