#include <stdio.h>
#include <string.h>
#include <stdlib.h>

/**
 * isUniqueChars - checks if a string has unique characters
 * using the bit manipulation method
 * @str: string
 * Return - True(1) if unique, otherwise False (0)
 */
int isUniqueChars(char *str)
{
	int checker, i;

	checker = 0;
	while (*str != '\0')
	{
		int val = *str - 'a';
		
		if ((checker & (1 << val)) > 0)
		{
			return (0);
		}
		checker |= (1 << val);
	}
	return (1);
}


int main(int args, char* argv[])
{
	if (args < 2)
	{
		printf("Format: %s {word}\n", argv[0]); 
		return (-1);
	}
	
	printf("args: %d\n", args);
	char *word = malloc(sizeof(char*) + 1);
	
	strcpy(word, argv[1]);
	if (isUniqueChars(word))
	{
		printf("%s is unique\n", word);
	}
	else
	{
		printf("%s is not unique\n", word);
	}
	return (0);
}

