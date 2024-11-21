#include <stdio.h>
#include <string.h>
#include <ctype.h>

void toUpperStr(char *str)
{
  for (int i = 0; str[i]; i++)
  {
    str[i] = toupper(str[i]);
  }
}

int main()
{
  char estado[3];

  printf("Digite a sigla do estado (PR, RS, SC): ");
  scanf("%s", estado);

  toUpperStr(estado);

  if (strcmp(estado, "PR") == 0)
  {
    printf("Paranaense\n");
  }
  else if (strcmp(estado, "RS") == 0)
  {
    printf("Gaucho\n");
  }
  else if (strcmp(estado, "SC") == 0)
  {
    printf("Catarinense\n");
  }
  else
  {
    printf("Outros estados\n");
  }

  return 0;
}
