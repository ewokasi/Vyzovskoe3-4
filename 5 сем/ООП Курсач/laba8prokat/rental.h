#ifndef RENTAL_H
#define RENTAL_H
#include "rentalstrategy.h"
#include "weeklystrategy.h"
#include "dailyrentalstrategy.h"



class Rental {
private:
    IRentalStrategy* _rentalStrategy;

public:
    Rental(IRentalStrategy* rentalStrategy) : _rentalStrategy(rentalStrategy) {}

    double CalculateRentalCost(int rentalTime) {
        return _rentalStrategy->CalculateRentalCost(rentalTime);
    }
};

//int main() {
    //auto dailyRental = new Rental(new DailyRentalStrategy());
    //std::cout << "Daily rental cost for 3 days: " << dailyRental->CalculateRentalCost(3) << std::endl;

   // auto weeklyRental = new Rental(new WeeklyRentalStrategy());
   // std::cout << "Weekly rental cost for 2 weeks: " << weeklyRental->CalculateRentalCost(2) << std::endl;

   // delete dailyRental;
   // delete weeklyRental;

   // return 0;
//}
#endif // RENTAL_H
