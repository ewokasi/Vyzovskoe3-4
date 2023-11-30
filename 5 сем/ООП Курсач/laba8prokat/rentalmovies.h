#ifndef ARENDA_H
#define ARENDA_H
#include <string>
#include "movies.h"
#include "subscriber.h"
#include <iostream>
class info{
public:
    int renterId;
    int filmId;
    int OperId;
    std::string date_take;
    std::string date_return;
    std::string film_name;
    info* next = nullptr;

    info(movie* mov, subscriber* sub){
        renterId = sub->id;
        filmId = mov->id;
        film_name = mov->name;
        date_take = "16.07.23";
        date_return = "17.07.23";
    }
};

class RentalMovies {
private:
    int count;


public:
    info* head= nullptr;
    int get_length(){return count;}
    std::string show();
    void add(info *input);
    info* find(std::string name, int sub_id);
    void return_film(std::string name, subscriber* sub);
    std::string* get_all_from_sub(subscriber* sub);
    info* get(int index);
};

info* RentalMovies::get(int index){

        if(count<index) return nullptr;
        info* current = head;
        int i = 0;
        while (i<index){
            current=current->next;
            i++;
        }
        return current;

}

void RentalMovies::return_film(std::string name, subscriber* sub){
    info* to_remove = find(name, sub->id);
    info* current = head;
    if(current == to_remove){
        head = head->next;
        count--;
        return;

    }

    while(current->next!= to_remove){
        current = current->next;
    }
    current->next=current->next->next;
    count--;
}

info* RentalMovies::find(std::string name, int sub_id){
    info* current = head;
    while (current!=nullptr){
        if(current->film_name==name && current->renterId == sub_id) return current;
        current= current->next;
    }
    return nullptr;
}

std::string RentalMovies::show(){
    std::string res = "";
    info* current = head;
    while(current!=nullptr){
        res += std::to_string(current->OperId)+": "+" "+current->film_name+", ";
        current = current->next;
    }
    return res;
}

void RentalMovies::add(info* input){
    if(!input) return;
    int number = get_length();
    int id = 1+number*21;
    input->OperId= id;
    info* sub = input;

    if(head==nullptr){
        head = sub;
        count++;
        return;
    }
    info* current = head;
    while(current->next!=nullptr){
        current = current->next;
    }
    current->next = sub;
    count++;
    return;
}
#endif
