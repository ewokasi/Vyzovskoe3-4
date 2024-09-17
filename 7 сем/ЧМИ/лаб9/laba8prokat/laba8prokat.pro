#-------------------------------------------------
#
# Project created by QtCreator 2023-05-11T18:17:18
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = laba8prokat
TEMPLATE = app


SOURCES += main.cpp\
        widget.cpp

HEADERS  += widget.h \
    rentalstrategy.h \
    movies.h \
    rental.h \
    rentalmovies.h \
    subscriber.h \
    weeklystrategy.h \
    dailyrentalstrategy.h \
    shop.h

FORMS    += widget.ui
