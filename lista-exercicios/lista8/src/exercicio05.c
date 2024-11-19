#include <stdio.h>
#include <stdlib.h>

int main()
{
  char filename[100];
  char buffer[1024];
  FILE *file;

  // Get filename from user
  printf("Digite o nome do arquivo para ler: ");
  scanf("%s", filename);

  // Open file in read mode
  file = fopen(filename, "r");

  // Check if file exists
  if (file == NULL)
  {
    printf("Erro ao abrir o arquivo!\n");
    return 1;
  }

  // Read and print file content line by line
  printf("\nConteudo do arquivo:\n");
  while (fgets(buffer, sizeof(buffer), file) != NULL)
  {
    printf("%s", buffer);
  }

  // Close file
  fclose(file);
  return 0;
}