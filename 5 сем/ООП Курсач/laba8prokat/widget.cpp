#include "widget.h"
#include "ui_widget.h"
#include "subscriber.h"
#include "movies.h"
#include "rental.h"
#include "rentalmovies.h"
#include "shop.h"
#include "string.h"
#include <QMessageBox>
sub_table subs;

RentalMovies RM;
shop Dibenko("Дыбенко");
shop Nevskiy("Невский");
std::string cur_user="";
void update_films(Ui::Widget *ui){
    ui->comboBox_film->clear();
    shop * current;
    if(ui->comboBox__shop_select->currentIndex() == 0){
      current =&Dibenko;
    }
    else{
        current =&Nevskiy;
    }

    for(int i = 0; i< current->catalog.get_length(); i++){
        std::string name = current->catalog.get(i)->name + ", " + std::to_string(current->catalog.get(i)->year);
        ui->comboBox_film->addItem(QString::fromStdString(name));

    }
}

Widget::Widget(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::Widget)
{
    ui->setupUi(this);

     ui->comboBox__shop_select->addItem("Дыбенко");
     ui->comboBox__shop_select->addItem("Невский");



    ui->comboBox_period->addItem("1 день");
    ui->comboBox_period->addItem("2 дня");
    ui->comboBox_period->addItem("1 неделя");


    Dibenko.catalog.add(1993, "Питер Джексон", "Властелин колец: Братство кольца" );
    Dibenko.catalog.add(1993, "Квентин Тарантино", "Криминальное чтиво"           );
    Dibenko.catalog.add(1995, "Мартин Скорсезе", "Таксист"                        );
    Dibenko.catalog.add(2006, "Квентин Тарантино", "Убить Билла");
    Dibenko.catalog.add(2013, "Алексей Балабанов", "Морфий");
    Dibenko.catalog.add(2018, "Денис Вильнев", "Бегущий в лабиринте");
    Dibenko.catalog.add(2000, "Стивен Спилберг", "Список Шиндлера");
    Dibenko.catalog.add(2014, "Алексей Учитель", "Кислород");
    Dibenko.catalog.add(2016, "Дэвид Финчер", "Социальная сеть");
    Dibenko.catalog.add(2019, "Дэвид Финчер", "Манк");
    Dibenko.catalog.add(2005, "Фрэнк Маршалл", "Последний самурай");

    Nevskiy.catalog.add(1997, "Фрэнк Дарабонт", "Темная башня"     );
    Nevskiy.catalog.add(1990, "Дэвид Кроненберг", "История насилия");
    Nevskiy.catalog.add(1999,"Найт Шьямалан", "Шестое чувство" );
    Nevskiy.catalog.add(2006, "Квентин Тарантино", "Убить Билла");
    Nevskiy.catalog.add(2013, "Алексей Балабанов", "Морфий");
    Nevskiy.catalog.add(2018, "Денис Вильнев", "Бегущий в лабиринте");
    Nevskiy.catalog.add(2000, "Стивен Спилберг", "Список Шиндлера");
    Nevskiy.catalog.add(2014, "Алексей Учитель", "Кислород");
    Nevskiy.catalog.add(2016, "Дэвид Финчер", "Социальная сеть");
    Nevskiy.catalog.add(2019, "Дэвид Финчер", "Манк");

    ui->label_welcome->setHidden(1);
    ui->groupBox_logs->setHidden(1);
    ui->groupBox_registration->setHidden(1);
    ui->pushButton_quit->setHidden(1);
    update_films(ui);

}



Widget::~Widget()
{
    delete ui;
}



void Widget::on_pushButton_check_cost_clicked()
{
    double cost;
    auto rent = new Rental(new DailyRentalStrategy());
    int period = ui->comboBox_period->currentIndex();
    switch (period) {
    case 0:
        rent = new Rental(new DailyRentalStrategy());
        cost = rent->CalculateRentalCost(1);
        break;
    case 1:
         rent = new Rental(new DailyRentalStrategy());
        cost = rent->CalculateRentalCost(2);
        break;
    case 2:
        rent = new Rental(new WeeklyRentalStrategy());
        cost = rent->CalculateRentalCost(1);
        break;
    default:
        break;
    }

    ui->label_cost->setText(QString::number(cost));
}

void Widget::on_pushButton_take_clicked()
{
    shop * current;
    if(ui->comboBox__shop_select->currentIndex() == 0){
      current =&Dibenko;
    }
    else{
        current =&Nevskiy;
    }
    std::string name =cur_user;
    if(name=="") {
        QMessageBox msgBox;
        msgBox.setText("Вы не прошли регистрацию");
        msgBox.exec();
        return;
    }


    subscriber* sub = subs.find(name);
    movie* mov = current->catalog.get(ui->comboBox_film->currentIndex());
    info * input = new info(mov, sub);
    RM.add(input);

    ui->comboBox_film_return->clear();

    sub = subs.find(name);
    if (sub==nullptr) return;

    info* cur = RM.head;
    std::string res ;
    while (cur){
        if(cur->renterId == sub->id)
        {res= cur->film_name;
        ui->comboBox_film_return->addItem(QString::fromStdString(res));}
        cur = cur->next;
    }

   // std::string addition = mov->name;
   // ui->comboBox_film_return->addItem(QString::fromStdString(addition));
}



void Widget::on_pushButton_return_clicked()
{
    std::string name = cur_user;
    if(name=="") {
        QMessageBox msgBox;
        msgBox.setText("Вы не прошли регистрацию");
        msgBox.exec();
        return;
    }
    subscriber* sub = subs.find(name);
    std::string mov = ui->comboBox_film_return->currentText().toStdString();


    RM.return_film(mov, sub);

    info* cur = RM.head;
    std::string res ;
    ui->comboBox_film_return->clear();
    while (cur){
        if(cur->renterId == sub->id)
        {res= cur->film_name;
        ui->comboBox_film_return->addItem(QString::fromStdString(res));}
        cur = cur->next;
    }
   // ui->comboBox_film_return->removeItem(0);

}

void Widget::on_pushButton_check_clicked()
{

}

void Widget::on_pushButton_show_films_clicked()
{
    ui->label_logs->clear();
    std::string outp = "Класс Фильмов:\nid\tНазвание\tАвтор\t\tгод";

    shop * current;
    if(ui->comboBox__shop_select->currentIndex() == 0){
      current =&Dibenko;
    }
    else{
        current =&Nevskiy;
    }

    for(int i = 0; i<current->catalog.get_length();i++){
        outp+="\n "+std::to_string(current->catalog.get(i)->id)+"\t"+current->catalog.get(i)->name+"\t"+current->catalog.get(i)->author+"\t"+std::to_string(current->catalog.get(i)->year);
    }
    ui->label_logs->setText(QString::fromStdString(outp));
}

void Widget::on_pushButton_show_films_2_clicked()
{
    ui->label_logs->clear();
    std::string outp = "Класс юзеров:\nid\tФИО";

    for(int i = 0; i<subs.get_length();i++){
        outp+="\n "+std::to_string(subs.get(i)->id)+"\t"+subs.get(i)->fio;
    }
    ui->label_logs->setText(QString::fromStdString(outp));
}

void Widget::on_pushButton_show_films_3_clicked()
{
    ui->label_logs->clear();
    std::string outp = "Класс Фильмов:\nidOP\tRenter id\tНазв фильма\tДата";

    for(int i = 0; i<RM.get_length();i++){
        outp+="\n "+std::to_string(RM.get(i)->OperId)+"\t"+std::to_string(RM.get(i)->renterId)+"\t"+RM.get(i)->film_name+"\t"+RM.get(i)->date_return;
    }
    ui->label_logs->setText(QString::fromStdString(outp));
}

void Widget::on_pushButton_clicked()
{
    ui->groupBox_registration->setHidden(0);

}

void Widget::on_pushButton_registrate_clicked()
{
    std::string name = ui->lineEdit_registration->text().toStdString();
    subs.registers(name);
    ui->groupBox_registration->setHidden(1);
    ui->label_welcome->setText(QString::fromStdString("Добро пожаловать, "+name));
    ui->label_welcome->setHidden(0);
    ui->pushButton->setHidden(1);
    cur_user = name;
    ui->pushButton_quit->setHidden(0);
}

void Widget::on_pushButton_2_clicked()
{
    if (ui->groupBox_logs->isHidden()){
        ui->groupBox_logs->setHidden(0);
        ui->groupBox_ArendaTake->setHidden(1);
        ui->groupBox_ArendaReturn->setHidden(1);
        ui->pushButton_2->setText(QString::fromStdString("Скрыть логи"));
    }
    else{
        ui->groupBox_logs->setHidden(1);
        ui->pushButton_2->setText(QString::fromStdString("Показать логи"));
        ui->groupBox_ArendaTake->setHidden(0);
        ui->groupBox_ArendaReturn->setHidden(0);
    }

}

void Widget::on_comboBox__shop_select_currentIndexChanged(int index)
{
    update_films(ui);
}

void Widget::on_pushButton_quit_clicked()
{
    cur_user="";
    ui->pushButton_quit->setHidden(1);
    ui->pushButton->setHidden(0);
    ui->label_welcome->setHidden(1);
}
