#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX 100

static int sao_anagramas(const char str1[], const char str2[])
{
  int contagem[26] = {0};

  if (strlen(str1) != strlen(str2))
    return 0;

  for (const char *s = str1; *s; s++)
  {
    if (isalpha(*s))
      contagem[toupper(*s) - 'A']++;
  }

  for (const char *s = str2; *s; s++)
  {
    if (isalpha(*s))
      if (--contagem[toupper(*s) - 'A'] < 0)
        return 0;
  }

  return 1;
}

int main()
{
  char str1[MAX], str2[MAX];

  printf("Digite a primeira palavra: ");
  if (!fgets(str1, MAX, stdin) || str1[0] == '\n')
  {
    printf("Erro na leitura da primeira palavra.\n");
    return 1;
  }
  str1[strcspn(str1, "\n")] = 0;

  printf("Digite a segunda palavra: ");
  if (!fgets(str2, MAX, stdin) || str2[0] == '\n')
  {
    printf("Erro na leitura da segunda palavra.\n");
    return 1;
  }
  str2[strcspn(str2, "\n")] = 0;

  printf("As palavras %s anagramas!\n",
         sao_anagramas(str1, str2) ? "são" : "não são");

  return 0;
}