#include <stdio.h>
#include <stdlib.h>

int main()
{
  FILE *arquivo;
  char nomeArquivo[100];
  char caractere;

  // Solicita o nome do arquivo ao usuário
  printf("Digite o nome do arquivo a ser lido: ");
  scanf("%99s", nomeArquivo);

  // Abre o arquivo para leitura
  arquivo = fopen(nomeArquivo, "r");

  // Verifica se o arquivo foi aberto com sucesso
  if (arquivo == NULL)
  {
    printf("Erro ao abrir o arquivo %s!\n", nomeArquivo);
    return 1;
  }

  // Lê o arquivo caractere por caractere até o final
  while ((caractere = fgetc(arquivo)) != EOF)
  {
    printf("%c", caractere);
  }

  // Fecha o arquivo
  fclose(arquivo);

  return 0;
}