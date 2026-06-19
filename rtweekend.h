#ifndef RTWEEKEND_H
#define RTWEEKEND_H

#include<iostream>
#include<cmath>
#include<memory>
#include<limits>
#include<random>

// C++ Std Usings

using std::make_shared;
using std::shared_ptr;

// Constants

const double infinity = std::numeric_limits<double>::infinity();
const double pi = 3.1415926535897932385;

// Utility Functions

inline double degrees_to_radians(double degrees) {
    return degrees * pi / 180.0;
}

// inline double random_double()
// {
//     // Returns a random real in [0,1).
//     return std::rand() / (RAND_MAX + 1.0 ) ;
// }

inline double random_double()
{
    thread_local std::mt19937 generator(
        std::random_device{}()
    );

    thread_local std::uniform_real_distribution<double>
        distribution(0.0, 1.0);

    return distribution(generator);
}

inline double random_double (double min , double max )
{
    // Returns a random real in [min,max).
    return min + (max- min) * random_double();
}

inline int random_int(int min, int max) {
    // Returns a random integer in [min,max].
    return int(random_double(min, max+1));
}

// Common Headers

#include "vec3.h"
#include "interval.h"
#include "ray.h"
#include "color.h"


#endif