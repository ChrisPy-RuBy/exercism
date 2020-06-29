#include "darts.h"
#include <math.h>
#include <stdio.h>

int score(coordinate_t landing_postion) {
	int score;

	float sum = pow(landing_postion.x, 2) + pow(landing_postion.y, 2);

	if(sum > 100.0) {
		score = 0;
	} else if (sum > 25) {
		score = 1;
	} else if (sum > 1) {
		score = 5;
	} else {
		score = 10;
	}
	printf("score: %d", score);
	return score;
}
