#include <stdio.h>

int main()
{
  FILE *arquivo;
  char nomes[5][10]; // Matrix to store 5 names with max 9 chars each
  int i;

  // Open file for reading
  arquivo = fopen("nomes", "r");

  if (arquivo == NULL)
  {
    printf("Erro ao abrir o arquivo!\n");
    return 1;
  }

  // Read names from file
  for (i = 0; i < 5; i++)
  {
    fscanf(arquivo, "%s", nomes[i]);
  }

  // Close file
  fclose(arquivo);

  // Print names
  printf("Nomes lidos do arquivo:\n");
  for (i = 0; i < 5; i++)
  {
    printf("%s\n", nomes[i]);
  }

  return 0;
}