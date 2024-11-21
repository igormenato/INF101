#include <stdio.h>
#include <string.h>

#define MAX_SIZE 100

int main()
{
    char nome[MAX_SIZE];

    printf("Digite um nome: ");
    if (!fgets(nome, sizeof(nome), stdin))
    {
        printf("Erro na leitura do nome.\n");
        return 1;
    }

    size_t len = strlen(nome);
    if (len > 0 && nome[len - 1] == '\n')
    {
        nome[len - 1] = '\0';
        len--;
    }

    if (len == 0)
    {
        printf("Nome vazio!\n");
        return 1;
    }

    printf("Nome ao contrario: ");
    for (int i = len - 1; i >= 0; i--)
    {
        putchar(nome[i]);
    }
    printf("\n");

    return 0;
}
