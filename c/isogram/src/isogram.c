#include "isogram.h"
#include <stdbool.h>
#include <stdio.h>
#include <string.h>

bool is_isogram(const char *phrase) 
{
	size_t length = strlen(phrase);

	char letters[length];

	size_t i = 0;
	size_t j;
	for(;i < length; i++) {
		//printf("Phrase letter: %c\n", phrase[i]);
		for(j = 0; j < i; j++) {
			printf("Phrase Letter: %c, Seen Letter: %c\n", phrase[i], letters[j]);
			if(phrase[i] == letters[j]) {
				printf("False");
				return false;
			}
		}
		letters[j] = phrase[i];
	}
	printf("True");
	return true;
}
/*
int main(void)
{
	char * phrase = "lumberjack";
	is_isogram(phrase);

	char * aphrase = "lumberljack";
	is_isogram(aphrase);
	 
}*/
