//
//  Workshop3.c
//  
//
//  Created by Jai Castle on 16/8/18.
//

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <math.h>
#include "Workshop3.h"

#define RADIUS_OF_EARTH 6371 //kilometres

#define MIN_LAT -90
#define MAX_LAT 90
#define MIN_LONG -180
#define MAX_LONG 180



bool valid_location(double latitude, double longitude){
    bool valid_longitude = longitude <= MAX_LONG && longitude >= MIN_LONG;
    bool valid_latitude = latitude >= MIN_LAT && latitude <= MAX_LAT;
    
    return valid_latitude && valid_longitude;
}
/*
 Takes parameters double latitude1, double longitude1, double latitude2, double longitude2 in radians.
 Finds the distance between the two points.
 */
double haversine(double latitude1, double longitude1, double latitude2, double longitude2){
    if (valid_location(latitude1, longitude1) && valid_location(latitude2, longitude2)){
        // https://en.wikipedia.org/wiki/Haversine_formula
        
        double twoR = RADIUS_OF_EARTH * 2;
        double sinSquaredOne = pow(sin((latitude2-latitude1)/2),2);
        double sinSquaredTwo = pow(sin((longitude2-longitude1)/2),2);
        double cosProduct = cos(latitude1)*cos(latitude2);
        
        double result = twoR * asin(sqrt(sinSquaredOne+cosProduct*sinSquaredTwo));
        
        return result;
        
    } else {
        printf("Locations are invalid\n");
        return -1;
    }
}

int main(int argc, char *argv[]){
    
    if (argc != 5) {
        printf("Please enter the correct number of arguments!\n");
        exit(EXIT_FAILURE);
    } else{
        double lat1 = degrees_to_radians(atof(argv[1]));
        double long1 = degrees_to_radians(atof(argv[2]));
        double lat2 = degrees_to_radians(atof(argv[3]));
        double long2 = degrees_to_radians(atof(argv[4]));
        
        if (valid_location(lat1, long1) && valid_location(lat2, long2)) {
            printf("%f kilometres\n", haversine(lat1, long1, lat2, long2));
        } else {
            printf("Please enter valid latitudes and longitudes\n");
            exit(EXIT_FAILURE);
        }
        
    }
    
    
    return EXIT_SUCCESS;
}
