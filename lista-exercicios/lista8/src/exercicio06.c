#include <stdio.h>

int main()
{
  char nome[50];
  char arquivo_nome[100];
  FILE *arquivo;

  // Solicita o nome do arquivo ao usuário
  printf("Digite o nome do arquivo para gravar: ");
  scanf("%s", arquivo_nome);

  // Abre o arquivo para escrita
  arquivo = fopen(arquivo_nome, "w");

  if (arquivo == NULL)
  {
    printf("Erro ao abrir o arquivo!\n");
    return 1;
  }

  // Solicita o nome ao usuário
  printf("Digite um nome: ");
  scanf("%s", nome);

  // Grava o nome no arquivo
  fprintf(arquivo, "%s", nome);

  // Fecha o arquivo
  fclose(arquivo);

  printf("Nome gravado com sucesso em %s!\n", arquivo_nome);

  return 0;
}