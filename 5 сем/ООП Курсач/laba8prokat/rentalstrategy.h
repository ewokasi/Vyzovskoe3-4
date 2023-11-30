#ifndef RENTALSTRATEGY_H
#define RENTALSTRATEGY_H

class IRentalStrategy {
public:
    virtual double CalculateRentalCost(int rentalTime) = 0;
};

#endif // RENTALSTRATEGY_H
