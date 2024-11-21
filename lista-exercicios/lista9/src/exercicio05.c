#include <stdio.h>

int compareStrings(const char *str1, const char *str2)
{
  int i = 0;

  while (str1[i] != '\0' && str2[i] != '\0')
  {
    if (str1[i] != str2[i])
    {
      return 0;
    }
    i++;
  }

  if (str1[i] == '\0' && str2[i] == '\0')
  {
    return 1;
  }
  return 0;
}

int main()
{
  char str1[100], str2[100];

  printf("Digite a primeira string: ");
  scanf("%s", str1);

  printf("Digite a segunda string: ");
  scanf("%s", str2);

  if (compareStrings(str1, str2))
  {
    printf("As strings são iguais\n");
  }
  else
  {
    printf("As strings são diferentes\n");
  }

  return 0;
}
