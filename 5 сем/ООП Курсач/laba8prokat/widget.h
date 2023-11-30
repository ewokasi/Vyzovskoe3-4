#ifndef WIDGET_H
#define WIDGET_H

#include <QWidget>
#include <string>

namespace Ui {
class Widget;
}

class Widget : public QWidget
{
    Q_OBJECT


public:

    explicit Widget(QWidget *parent = 0);
    ~Widget();

private slots:
    void on_pushButton_registrate_clicked();

    void on_pushButton_check_cost_clicked();

    void on_pushButton_take_clicked();


    
    void on_pushButton_return_clicked();

    void on_pushButton_check_clicked();

    void on_pushButton_show_films_clicked();

    void on_pushButton_show_films_2_clicked();

    void on_pushButton_show_films_3_clicked();

    void on_pushButton_clicked();

    void on_pushButton_2_clicked();

    void on_comboBox__shop_select_currentIndexChanged(int index);

    void on_pushButton_quit_clicked();

private:
    Ui::Widget *ui;
};

#endif // WIDGET_H
