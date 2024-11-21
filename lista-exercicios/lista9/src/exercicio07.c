#include <stdio.h>
#include <string.h>

int main()
{
  char nome[50];
  char endereco[100];
  char telefone[20];
  char info_completa[170]; // Tamanho suficiente para armazenar todas as informações

  // Lendo as informações
  printf("Digite o nome: ");
  fgets(nome, sizeof(nome), stdin);
  nome[strcspn(nome, "\n")] = 0; // Remove o \n do final

  printf("Digite o endereco: ");
  fgets(endereco, sizeof(endereco), stdin);
  endereco[strcspn(endereco, "\n")] = 0;

  printf("Digite o telefone: ");
  fgets(telefone, sizeof(telefone), stdin);
  telefone[strcspn(telefone, "\n")] = 0;

  // Concatenando as informações
  strcpy(info_completa, nome);
  strcat(info_completa, ", ");
  strcat(info_completa, endereco);
  strcat(info_completa, ", ");
  strcat(info_completa, telefone);

  // Exibindo o resultado
  printf("\nInformacoes: %s\n", info_completa);

  return 0;
}