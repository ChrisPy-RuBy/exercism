#include "space_age.h"
#include <stdint.h>
#include <stdio.h>

float convert_planet_age(planet_t planet, int64_t input) 
{
	double seconds_per_year[9];
	seconds_per_year[0] = 31557600 * 0.2408467;
	seconds_per_year[1] = 31557600 * 0.61519726;
	seconds_per_year[2] = 31557600 * 1.0;
	seconds_per_year[3] = 31557600 * 1.8808158;
	seconds_per_year[4] = 31557600 * 11.862615;
	seconds_per_year[5] = 31557600 * 29.447498;
	seconds_per_year[6] = 31557600 * 84.016846;
	seconds_per_year[7] = 31557600 * 164.79132;


	planet_t p;
	p = planet;

	return (double)input / seconds_per_year[p];
}
