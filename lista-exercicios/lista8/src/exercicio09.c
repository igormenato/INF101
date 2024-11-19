#include <stdio.h>

int main()
{
  FILE *arquivo;
  char caractere;
  int numeroLinhas = 0;

  arquivo = fopen("nomes", "r");

  if (arquivo == NULL)
  {
    printf("Erro ao abrir o arquivo!\n");
    return 1;
  }

  while ((caractere = fgetc(arquivo)) != EOF)
  {
    if (caractere == '\n')
    {
      numeroLinhas++;
    }
  }

  if (caractere != '\n' && numeroLinhas > 0)
  {
    numeroLinhas++;
  }

  fclose(arquivo);

  printf("O arquivo possui %d linha(s).\n", numeroLinhas);

  return 0;
}