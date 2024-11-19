#include <stdio.h>
#include <stdlib.h>

#define MAX_DIAS 31

int main()
{
  FILE *arqEntrada, *arqSaida;
  float temperaturas[MAX_DIAS];
  float temp, menor = 40.0, maior = 10.5, soma = 0.0, media;
  int i = 0, diasAbaixo = 0, diasAcima = 0;

  arqEntrada = fopen("temperatura.txt", "r");
  if (arqEntrada == NULL)
  {
    printf("Erro ao abrir arquivo de entrada!\n");
    return 1;
  }

  while (fscanf(arqEntrada, "%f", &temp) != EOF && i < MAX_DIAS)
  {
    temperaturas[i] = temp;
    if (temp < menor)
      menor = temp;
    if (temp > maior)
      maior = temp;
    soma += temp;
    i++;
  }
  fclose(arqEntrada);

  media = soma / i;

  for (int j = 0; j < i; j++)
  {
    if (temperaturas[j] < media)
      diasAbaixo++;
    if (temperaturas[j] > media)
      diasAcima++;
  }

  arqSaida = fopen("temperaturaR.txt", "w");
  if (arqSaida == NULL)
  {
    printf("Erro ao criar arquivo de saída!\n");
    return 1;
  }

  fprintf(arqSaida, "Menor temperatura: %.1f\n", menor);
  fprintf(arqSaida, "Maior temperatura: %.1f\n", maior);
  fprintf(arqSaida, "Temperatura média: %.1f\n", media);
  fprintf(arqSaida, "Dias com temperatura abaixo da média: %d\n", diasAbaixo);
  fprintf(arqSaida, "Dias com temperatura acima da média: %d\n", diasAcima);

  fclose(arqSaida);
  printf("Processamento concluído. Verifique o arquivo temperaturaR.txt\n");

  return 0;
}
