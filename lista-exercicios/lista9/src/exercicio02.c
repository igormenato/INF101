#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_SIZE 100

int isPalindromo(char *palavra)
{
  int i, j;
  int tamanho = strlen(palavra);

  for (i = 0, j = tamanho - 1; i < j; i++, j--)
  {
    if (tolower(palavra[i]) != tolower(palavra[j]))
    {
      return 0;
    }
  }
  return 1;
}

int main()
{
  char palavra[MAX_SIZE];

  printf("Digite uma palavra: ");
  scanf("%s", palavra);

  if (isPalindromo(palavra))
  {
    printf("'%s' é um palíndromo!\n", palavra);
  }
  else
  {
    printf("'%s' não é um palíndromo.\n", palavra);
  }

  return 0;
}