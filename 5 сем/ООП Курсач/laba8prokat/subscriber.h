
#ifndef SUBSCRIBER_H
#define SUBSCRIBER_H
#include <string>
class subscriber{
public:
    int number;
    int id;
    std::string fio;

    subscriber* next = nullptr;
    subscriber(std::string fio, int number, int id){
        this->fio = fio;
        this->id = id;
        this->number = number;
    }

};

class sub_table{
  private:
    subscriber* head = nullptr;
    int count = 0;

  public:

    int get_length();
    std::string show();
    void registers(std::string name);
    subscriber* find(std::string name);
    subscriber* get(int index);
};

subscriber* sub_table::get(int index){
    subscriber* current = head;
    for(int i = 0; i<index; i++){
        current=current->next;
    }
    return current;
}

std::string sub_table::show(){

    std::string res= "";
    subscriber* current = head;
    while(current!=nullptr){
        res = res + current->fio+", ";
        current = current->next;
   }
    return res;
}


subscriber* sub_table::find(std::string name){

    if(name == "")return nullptr;
    subscriber* current = head;
    while(current!=nullptr){
        if (current->fio == name){
            return current;
        }
        current = current->next;
   }
    return nullptr;
}

void sub_table::registers(std::string name){

    int number = get_length();
    int id = 1+ number*13;
    subscriber* sub = new subscriber(name, number, id);

    if(head==nullptr){
        head = sub;
        count++;
        return;
    }
    subscriber* current = head;
    while(current->next!=nullptr){
        if  (current->fio==name){
            return;
        }
        current = current->next;

    }
    if  (current->fio==name){
        return;
    }
    current->next = sub;
    count++;
    return;

}

int sub_table::get_length(){
    return count;
}

#endif // SUBSCRIBER_H
