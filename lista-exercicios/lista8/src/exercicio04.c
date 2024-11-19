#include <stdio.h>
#include <stdlib.h>

int main()
{
  char nome[100];
  char arquivo_nome[100];
  FILE *arquivo;

  // Solicita o nome do arquivo ao usuário
  printf("Digite o nome do arquivo para salvar: ");
  scanf("%s", arquivo_nome);
  getchar(); // Limpa o buffer do teclado

  // Abre o arquivo para escrita
  arquivo = fopen(arquivo_nome, "w");

  if (arquivo == NULL)
  {
    printf("Erro ao abrir o arquivo!\n");
    return 1;
  }

  // Solicita o nome ao usuário
  printf("Digite um nome: ");
  fgets(nome, sizeof(nome), stdin);

  // Escreve o nome no arquivo
  fputs(nome, arquivo);

  // Fecha o arquivo
  fclose(arquivo);

  printf("Nome gravado com sucesso em %s!\n", arquivo_nome);

  return 0;
}