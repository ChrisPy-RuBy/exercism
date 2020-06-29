#ifndef RESISTOR_COLOR_H
#define RESISTOR_COLOR_H

enum resistor_band_t {
	BLACK,
	BROWN, 
	RED, 
	ORANGE,
	YELLOW,
	GREEN,
	BLUE,
	VIOLET,
	GREY,
	WHITE,
	};


int color_code(enum resistor_band_t candidate);

#endif
