# Bak

Bak é uma ferramenta de linha de comando simples e rápida para fazer **backups temporários de arquivos e diretórios**, com opção de compressão, recuperação e listagem. Ideal para quem trabalha com código ou arquivos importantes e quer uma forma rápida e prática de fazer backups localmente.

## Funcionalidades

- Backup de arquivos e diretórios
- Compressão automática de diretórios (via `shutil` ou `7z`)
- Recuperação de arquivos por nome ou busca parcial (`fd`)
- Listagem de arquivos salvos
- Limpeza total da pasta de backups
- Abertura do diretório no explorador de arquivos

## Instalação

Clone este repositório para um diretório do seu sistema.

```bash
git clone https://github.com/Dimitri-Miranda/bak
cd bak
python -m bak --help
```
Opcional: se você instalou via clone, adicione um alias para o comando.

### Windows alias:

Crie um arquivo `.bat` , por exemplo `bak.bat`, em algum diretório que esteja no seu `PATH`.

Conteúdo do `bak.bat`:

```batch
@echo off
setlocal

set BAK_PATH=%USERPROFILE%\diretorio_onde_voce_clonou\bak
set PYTHONPATH=%BAK_PATH%

python -m bak %*

endlocal
```

## Configuração

Ao executar pela primeira vez, ou usar a flag `--init`, o script criará um arquivo de configuração em:

```bash
~\.config\bak\bak_config.ini
```
Esse arquivo define:

- Diretório onde os backups serão salvos
- Comando para abrir o explorador (explorer, xdg-open, etc.)
- Mecanismo de compactação (shutil, 7z, etc.)

o script também criará uma diretório para os backups em:

```bash
~\.bak_temp
```
Este diretório conterá os backups que você fará (é possível alterar no arquivo de configuração `bak_config.ini`).

## Como usar

### Modos por diferentes tipo de instalação

Você pode usar a ferramenta de duas formas:

- **Clonando o repositório** e executando via `python -m bak`
- **Instalando via pip (local ou PyPI)** e usando o comando `bak`

### Flags

| Flag              | Descrição                                     |
|-------------------|-----------------------------------------------|
| `-b`, `--backup`  | Faz o backup de arquivos ou diretórios        |
| `-r`, `--rescue`  | Recupera arquivos a partir do nome ou busca   |
| `-l`, `--list`    | Lista os arquivos no diretório de backups     | 
| `--clean`         | Limpa todos os arquivos de backup             |
| `-o`, `--open`    | Abre o diretório de backups no explorador     |
| `-f`, `--file`    | Um ou mais arquivos/diretórios para usar      |
| `-s`, `--search`  | Termo(s) para buscar arquivos (fd)            |
| `--init`          | Cria/reseta configurações                     |
| `--version`       | Mostra a versão                               |

Obs: As flags `-b`, `-r`, `-l`, `--clean`, `-o`, `--init`, `--version` são mutuamente exclusivas.

## Exemplos

Fazer backup de um arquivo:
```bash
bak -b -f meuArquivo.txt
```

Fazer backup de um diretório (compactada):
```bash
bak -b -f meuDiretório
```

Recuperar arquivo por nome:
```bash
bak -r -f meuArquivo_2024-05-18_20-32-10.txt.bak
```

Recuperar arquivo por índice:
```bash
bak -r -f 0
```

Recuperar arquivo por busca (usa `fd`):
```bash
bak -r -s meuArquivo
```

Listar arquivos de backup:
```bash
bak -l
```

Limpar todos os backups:
```bash
bak --clean
```

Abrir o diretório de backups:
```bash
bak -o
```

Criar ou resetar o arquivo de configurações:
```bash
bak --init
```

Mostrar a versão:
```bash
bak --version
```

## Exemplos com múltiplos arquivos

Fazer backup de vários arquivos e diretórios:
```bash
bak -b -f arquivo1.txt arquivo2.txt diretório1
```

Recuperar múltiplos arquivos por nome completo:
```bash
bak -r -f backup1_2024-05-18_20-32-10.txt.bak backup2_2024-05-18_2
```

Recuperar múltiplos arquivos por busca parcial:
```bash
bak -r -s backup1 backup2
```

## Estrutura do Projeto

```
bak/
├── .gitignore        # Ignora arquivos temporários e de build
├── LICENSE           # Licença MIT do projeto
├── README.md         # Documentação principal do projeto
├── pyproject.toml    # Metadados e instruções de build (PEP 621)
└── bak/              # Pacote principal da ferramenta
    ├── __init__.py     # Define que a pasta é um pacote Python
    ├── __main__.py     # Permite execução com `python -m bak`
    ├── backup.py       # Lógica de backup de arquivos e diretórios
    ├── config.py       # Leitura e criação do arquivo de configuração
    ├── helpers.py      # Funções auxiliares e utilitárias
    ├── main.py         # Ponto de entrada (define e processa os argumentos CLI)
    └── rescue.py       # Lógica de recuperação de backups
```

## Requisitos

- Python 3.8+
- (opcional) `fd` para busca mais rápida
- (opcional) `7z` se quiser compressão avançada

## Roadmap

- Suporte para diferentes compressores
- Suporte multiplataforma
- Testes automatizados com pytest

## Licença

Este projeto é licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes
