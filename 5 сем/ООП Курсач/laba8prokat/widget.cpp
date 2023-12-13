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

int mark_stars(Ui::Widget *ui, int st){
     QCheckBox *stars[] = {ui->checkBox, ui->checkBox_2, ui->checkBox_3, ui->checkBox_4, ui->checkBox_5};
    for (int i =0;i<5 ; i++){
        stars[i]->setCheckState(Qt::CheckState(0));
    }
    for (int i =0;i<st ; i++){
        stars[i]->setCheckState(Qt::CheckState(1));
    }
    return st;

}
int last_stared ;
void update_films(Ui::Widget *ui){
    ui->listWidget_catalog->clear();
    shop * current;
    if(ui->comboBox__shop_select->currentIndex() == 0){
      current =&Dibenko;
    }
    else{
        current =&Nevskiy;
    }


    for(int i = 0; i< current->catalog.get_length(); i++){
        std::string rat = "";
        for (int j = 0; j<3; j++){
            rat+= std::to_string(current->catalog.get(i)->rating)[j];
        }
        std::string name = current->catalog.get(i)->name + ", " + std::to_string(current->catalog.get(i)->year) +' '+rat + " ⭐" ;


        ui->listWidget_catalog->addItem(QString::fromStdString(name));

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


    Nevskiy.catalog.add(1997, "Фрэнк Дарабонт", "Темная башня"     );
    Nevskiy.catalog.add(1990, "Дэвид Кроненберг", "История насилия");
    Nevskiy.catalog.add(1999,"Найт Шьямалан", "Шестое чувство" );
    Nevskiy.catalog.add(2006, "Квентин Тарантино", "Убить Билла");
    Nevskiy.catalog.add(2013, "Алексей Балабанов", "Морфий");
    Nevskiy.catalog.add(2018, "Денис Вильнев", "Бегущий в лабиринте");


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
    movie* mov = current->catalog.get(ui->listWidget_catalog->currentRow());
    info * input = new info(mov, sub);
    RM.add(input);

    ui->listWidget_film_return->clear();

    sub = subs.find(name);
    if (sub==nullptr) return;

    info* cur = RM.head;
    std::string res ;
    while (cur){
        if(cur->renterId == sub->id)
        {res= cur->film_name;
        ui->listWidget_film_return->addItem(QString::fromStdString(res));}
        cur = cur->next;
    }


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
    std::string mov = ui->listWidget_film_return->currentItem()->text().toStdString();


    RM.return_film(mov, sub);

    info* cur = RM.head;
    std::string res ;
    ui->listWidget_film_return->clear();
    while (cur){
        if(cur->renterId == sub->id)
        {res= cur->film_name;
        ui->listWidget_film_return->addItem(QString::fromStdString(res));}
        cur = cur->next;
    }


}

void Widget::on_pushButton_check_clicked()
{

}

void Widget::on_pushButton_show_films_clicked()

{


    std::string outp = "Класс Фильмов:\nid\tНазвание\t\t\t\t\tАвтор\t\tгод";

    shop * current;
    if(ui->comboBox__shop_select->currentIndex() == 0){
      current =&Dibenko;
    }
    else{
        current =&Nevskiy;
    }
    ui->tableWidget_logs->clear();
    ui->tableWidget_logs->setColumnCount(5);
    QStringList headers;
    headers<<"id" << "name" << "author"<<"year" <<"rating";
    ui->tableWidget_logs->setHorizontalHeaderLabels(headers);
    for(int i = 0; i<current->catalog.get_length();i++){
         ui->tableWidget_logs->insertRow(i);
            QTableWidgetItem *item=new QTableWidgetItem (QString::fromStdString(current->catalog.get(i)->name));
            QTableWidgetItem *item2=new QTableWidgetItem (QString::fromStdString(current->catalog.get(i)->author));
            QTableWidgetItem *item3=new QTableWidgetItem (QString::fromStdString(std::to_string(current->catalog.get(i)->year)));
            QTableWidgetItem *item4=new QTableWidgetItem (QString::fromStdString(std::to_string(current->catalog.get(i)->rating)));
            QTableWidgetItem *item5=new QTableWidgetItem (QString::fromStdString(std::to_string(current->catalog.get(i)->id)));

            ui->tableWidget_logs->setItem(i, 0, item5);
            ui->tableWidget_logs->setItem(i, 1, item);
            ui->tableWidget_logs->setItem(i, 2, item2);
            ui->tableWidget_logs->setItem(i, 3, item3);
            ui->tableWidget_logs->setItem(i, 4, item4);



    }

}

void Widget::on_pushButton_show_films_2_clicked()
{



    ui->tableWidget_logs->clear();
    ui->tableWidget_logs->setColumnCount(2);
    QStringList headers;
    headers << "id" << "fio" ;
    ui->tableWidget_logs->setHorizontalHeaderLabels(headers);
    for(int i = 0; i< subs.get_length();i++){
         ui->tableWidget_logs->insertRow(i);
            QTableWidgetItem *item=new QTableWidgetItem (QString::fromStdString(std::to_string(subs.get(i)->id)));
            QTableWidgetItem *item2=new QTableWidgetItem (QString::fromStdString(subs.get(i)->fio));

            ui->tableWidget_logs->setItem(i, 0, item);
            ui->tableWidget_logs->setItem(i, 1, item2);


    }

}

void Widget::on_pushButton_show_films_3_clicked()
{

    ui->tableWidget_logs->clear();
    ui->tableWidget_logs->setColumnCount(4);
    QStringList headers;
    headers << "OperId" << "renterId" << "film_name" << "date_return";
    ui->tableWidget_logs->setHorizontalHeaderLabels(headers);

    for(int i = 0; i< subs.get_length();i++){
         ui->tableWidget_logs->insertRow(i);
            QTableWidgetItem *item=new QTableWidgetItem (QString::fromStdString(std::to_string(RM.get(i)->OperId)));
            QTableWidgetItem *item2=new QTableWidgetItem (QString::fromStdString(std::to_string(RM.get(i)->renterId)));
            QTableWidgetItem *item3=new QTableWidgetItem (QString::fromStdString(RM.get(i)->film_name));
            QTableWidgetItem *item4=new QTableWidgetItem (QString::fromStdString(RM.get(i)->date_return));

            ui->tableWidget_logs->setItem(i, 0, item);
            ui->tableWidget_logs->setItem(i, 1, item2);
            ui->tableWidget_logs->setItem(i, 2, item3);
            ui->tableWidget_logs->setItem(i, 3, item4);


    }


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

void Widget::on_pushButton_3_clicked()
{
    std::string name = ui->lineEdit_film_name->text().toStdString();
    std::string author = ui->lineEdit_film_author->text().toStdString();
    std::string year = ui->lineEdit_film_year->text().toStdString();
    shop * current;
    if(ui->comboBox__shop_select->currentIndex() == 0){
      current =&Dibenko;
    }
    else{
        current =&Nevskiy;
    }
    current->catalog.add(std::stoi(year), author, name);
}

void Widget::on_checkBox_5_clicked()
{

   last_stared= mark_stars(ui, 5);
}

void Widget::on_checkBox_4_clicked()
{
    last_stared=mark_stars(ui, 4);
}

void Widget::on_checkBox_3_clicked()
{
   last_stared= mark_stars(ui, 3);
}

void Widget::on_checkBox_2_clicked()
{
    last_stared=mark_stars(ui, 2);
}

void Widget::on_checkBox_clicked()
{
   last_stared= mark_stars(ui, 1);
}

void Widget::on_pushButton_4_clicked()
{
    shop * current;
    if(ui->comboBox__shop_select->currentIndex() == 0){
      current =&Dibenko;
    }
    else{
        current =&Nevskiy;
    }
    std::string name = ui->listWidget_film_return->currentItem()->text().toStdString();
    current->catalog.get_by_name(name)->set_rate(last_stared);
    update_films(ui);
}
