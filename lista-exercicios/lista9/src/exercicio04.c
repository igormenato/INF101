#include <stdio.h>
#include <string.h>
#include <ctype.h>

int isVowel(char c)
{
  c = tolower(c);
  return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

int countVowels(const char *str)
{
  int count = 0;
  for (int i = 0; str[i] != '\0'; i++)
  {
    if (isVowel(str[i]))
    {
      count++;
    }
  }
  return count;
}

int main()
{
  char str[21];
  char temp[100];

  while (1)
  {
    printf("Digite uma string (máximo 20 caracteres): ");
    if (fgets(temp, sizeof(temp), stdin) == NULL)
    {
      break;
    }

    temp[strcspn(temp, "\n")] = '\0';

    if (strlen(temp) > 20)
    {
      printf("Erro: A string deve ter no máximo 20 caracteres!\n");
      continue;
    }

    strcpy(str, temp);
    int vowels = countVowels(str);
    printf("Número de vogais na string: %d\n", vowels);
    break;
  }

  return 0;
}
