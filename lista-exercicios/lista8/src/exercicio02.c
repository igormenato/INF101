#include <stdio.h>
#include <stdlib.h>

int main()
{
  FILE *arquivo;
  char nome[50];
  char nomeArquivo[100];
  int i = 0;

  // Solicita o nome do arquivo
  printf("Digite o nome do arquivo para salvar: ");
  scanf("%s", nomeArquivo);

  // Abre o arquivo para escrita
  arquivo = fopen(nomeArquivo, "w");

  if (arquivo == NULL)
  {
    printf("Erro ao abrir o arquivo!\n");
    return 1;
  }

  printf("Digite um nome: ");
  scanf("%s", nome);

  // Grava cada caractere do nome no arquivo
  while (nome[i] != '\0')
  {
    fputc(nome[i], arquivo);
    i++;
  }

  fclose(arquivo);
  printf("Nome gravado com sucesso em %s!\n", nomeArquivo);

  return 0;
}