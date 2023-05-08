#include <stdio.h>
#include <string.h>

/**
 * are_perm - compares is two strings are permutations of 
 * each other
 * @s: first string
 * @t: second string
 * Return - True (1) if `are_perm` else False (0)
 */
int are_perm(char *s, char *t)
{
	int str1_sum, str2_sum, len_str = strlen(s);

	if (len_str != strlen(t))
		return (0);	
	
	str1_sum = 0;
	str2_sum = 0;
	while (*s && *t)
	{
		str1_sum += *s;
		str2_sum += *t;
		s++;
		t++;
	}
	
	if (str1_sum == str2_sum)
		return (1);
	return (0);
}


int main(int args, char* argv[])
{
	if (args <= 1)
	{
		printf("Format %s {word1} {word2}\n", argv[0]);
		return (-1);
	}
	char *word1 = argv[1];
	char *word2 = argv[2];

	printf("%s, %s, %d\n", word1, word2, are_perm(word1, word2));

	return (0);
}
