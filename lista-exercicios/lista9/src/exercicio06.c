#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100

int main()
{
  char str1[MAX_SIZE];
  char str2[MAX_SIZE];

  printf("Digite a primeira string: ");
  fgets(str1, MAX_SIZE, stdin);
  str1[strcspn(str1, "\n")] = '\0';

  printf("Digite a segunda string: ");
  fgets(str2, MAX_SIZE, stdin);
  str2[strcspn(str2, "\n")] = '\0';

  int len1 = strlen(str1);
  int len2 = strlen(str2);

  if (strcmp(str1, str2) == 0)
  {
    printf("As strings são iguais.\n");
  }
  else
  {
    printf("As strings são diferentes.\n");

    if (len1 > len2)
    {
      printf("A primeira string é maior com %d caracteres.\n", len1);
    }
    else if (len2 > len1)
    {
      printf("A segunda string é maior com %d caracteres.\n", len2);
    }
    else
    {
      printf("As strings têm o mesmo comprimento: %d caracteres.\n", len1);
    }
  }

  return 0;
}