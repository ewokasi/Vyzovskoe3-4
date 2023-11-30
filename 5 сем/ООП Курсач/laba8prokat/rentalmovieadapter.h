#ifndef RENTALMOVIEADAPTER_H
#define RENTALMOVIEADAPTER_H
#include "rentalmovies.h"
#include "movies.h"
#include "subscriber.h"

class RentalMoviesAdapter : public RentalMovies {
private:
    movie movieInfo;
    subscriber customerInfo;

public:
    RentalMoviesAdapter(movie movieInfo, subscriber customerInfo) {
        this->movieInfo = movieInfo;
        this->customerInfo = customerInfo;
    }

    void rentMovie(string movieName) override {
            }

    void returnMovie(string movieName) override {
        cout << "The movie " << movieName << " has been returned by " << customerInfo.name << "." << endl;
    }
};

#endif // RENTALMOVIEADAPTER_H
