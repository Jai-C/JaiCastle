//
//  degressRadians.c
//  
//
//  Created by Jai Castle on 12/9/18.
//

#include "Workshop3.h"

double degrees_to_radians(double degrees){
    return (M_PI * degrees)/180;
}

double radians_to_degrees(double radians){
    return (180 * radians)/M_PI;
}
