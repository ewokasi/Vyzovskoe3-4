#ifndef MOVIES_H
#define MOVIES_H
#include <string>


class movie{
public:
    int number;
    int id, year;
    std::string author, name;
    bool state; //0 - на складе, 1 - выдан

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

    movies(){

    }
};

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
