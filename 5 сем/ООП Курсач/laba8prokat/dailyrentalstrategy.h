#ifndef DAILYRENTALSTRATEGY_H
#define DAILYRENTALSTRATEGY_H
#include "rentalstrategy.h"
class DailyRentalStrategy : public IRentalStrategy {
public:
    double CalculateRentalCost(int rentalTime) override {
        return rentalTime * 5.0;
    }
};
#endif // DAILYRENTALSTRATEGY_H
