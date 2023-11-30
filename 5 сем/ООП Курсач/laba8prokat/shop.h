#ifndef SHOP_H
#define SHOP_H
#include "string.h"

class shop
{
public:
    movies catalog;
    std::string name;

    void set_name(std::string name){
        this->name = name;
    }

    shop(std::string name){
        set_name(name);

    }


    std::string get_name(){
        return name;
    }
};

#endif // SHOP_H
