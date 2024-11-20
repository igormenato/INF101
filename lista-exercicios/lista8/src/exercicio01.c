#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main()
{
  FILE *arquivo;
  char nomeArquivo[100];

  printf("Digite o nome do arquivo que deseja criar: ");
  scanf("%s", nomeArquivo);

  arquivo = fopen(nomeArquivo, "w");

  if (arquivo == NULL)
  {
    printf("Erro ao criar o arquivo!\n");
    return 1;
  }

  printf("Arquivo criado com sucesso!\n");

  fclose(arquivo);
  return 0;
}