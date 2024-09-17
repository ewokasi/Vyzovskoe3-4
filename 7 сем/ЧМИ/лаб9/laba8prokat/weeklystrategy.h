#ifndef WEEKLYRENTALSTRATEGY_H
#define WEEKLYRENTALSTRATEGY_H
#include "rentalstrategy.h"
class WeeklyRentalStrategy : public IRentalStrategy {
public:
    double CalculateRentalCost(int rentalTime) override {
        return rentalTime * 20.0;
    }
};
#endif // WEEKLYRENTALSTRATEGY_H
