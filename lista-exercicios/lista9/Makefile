# Diretórios do projeto
SRC_DIR = src
BIN_DIR = bin

# Lista todos os arquivos .c do diretório fonte
SOURCES = $(wildcard $(SRC_DIR)/*.c)

# Define extensão baseado no SO
ifeq ($(OS),Windows_NT)
	EXT = .exe
else
	EXT =
endif

# Gera nomes dos executáveis com caminho
EXECUTABLES = $(patsubst $(SRC_DIR)/%.c,$(BIN_DIR)/%$(EXT),$(SOURCES))

# Regra principal
all: $(BIN_DIR) $(EXECUTABLES)

# Cria diretório bin
$(BIN_DIR):
	mkdir -p $@

# Regra de compilação
$(BIN_DIR)/%$(EXT): $(SRC_DIR)/%.c
	gcc $< -o $@

# Regra de limpeza
clean:
	rm -rf $(BIN_DIR)
