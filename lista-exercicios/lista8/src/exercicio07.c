#include <stdio.h>

int main()
{
  FILE *file;
  char buffer[256];
  char filename[256];

  printf("Digite o nome do arquivo: ");
  scanf("%255s", filename);

  file = fopen(filename, "r");
  if (file == NULL)
  {
    printf("Erro ao abrir o arquivo.\n");
    return 1;
  }

  while (fscanf(file, "%255s", buffer) != EOF)
  {
    printf("%s ", buffer);
  }

  fclose(file);
  return 0;
}