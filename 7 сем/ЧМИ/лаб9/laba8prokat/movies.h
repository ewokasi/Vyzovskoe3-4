#ifndef MOVIES_H
#define MOVIES_H
#include <string>


class movie{
public:
    int number;
    int id, year;
    std::string author, name;
    bool state; //0 - на складе, 1 - выдан

    float cnt_rates = 1+rand()%9;
    float sum_rates = cnt_rates+rand()%25;
    float rating = sum_rates/cnt_rates ;
    void set_rate( int stars);
    movie* next= nullptr;
    movie(int num=0, int i=0, int y=0, std::string auth=0, std::string n=0, bool stat =1){number=num;id=i; year = y; author = auth; name = n; state = stat;}

};

class movies{
private:
    int count;
    movie* head = nullptr;

public:
    void add(int y, std::string auth, std::string n);
    movie* get(int index);
    int get_length(){return count;}

    float get_rating(int index);
    movie* get_by_name(std::string name);
    movies(){

    }
};

movie* movies::get_by_name(std::string name)
{

    movie* current = head;
    int i = 0;
    while (i<count){
        if(current->name==name)return current;
        current=current->next;
        i++;
    }
    return nullptr;
}

movie* movies::get(int index){
    if(count<index) return nullptr;
    movie* current = head;
    int i = 0;
    while (i<index){
        current=current->next;
        i++;
    }
    return current;
}

void movie::set_rate(int stars){

    this->cnt_rates++;
    this->sum_rates+=stars;
    this->rating =  this->sum_rates/ this->cnt_rates;

}
float movies::get_rating(int index ){
    movie* trg = get(index);
    return trg->rating;

}

void movies::add(int y, std::string auth, std::string n){
    int number = get_length();
    int id =1+ number*7;
    movie* sub = new movie(number, id, y, auth, n ,1);

    if(head==nullptr){
        head = sub;
        count++;
        return;
    }
    movie* current = head;
    while(current->next!=nullptr){
        current = current->next;
    }
    current->next = sub;
    count++;
    return;
}

#endif // MOVIES_H
