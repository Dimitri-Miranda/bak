# Backup Tool (bak)

Uma ferramenta de linha de comando simples e rápida para fazer **backups temporários de arquivos e pastas**, com opção de compressão, recuperação e listagem. Ideal para quem trabalha com código ou arquivos importantes e quer uma forma rápida e prática de fazer backups localmente.

## Funcionalidades

- Backup de arquivos e diretórios
- Compressão automática de diretórios (via `shutil` ou `7z`)
- Recuperação de arquivos por nome ou busca parcial (`fd`)
- Listagem de arquivos salvos
- Limpeza total da pasta de backups
- Abertura do diretório no explorador de arquivos

## Instalação

Clone este repositório ou copie os arquivos para um diretório do seu sistema.

```bash
git clone https://github.com/Dimitri-Miranda/bak
cd bak
python main.py --help
```
Opcional: adicione um alias para o comando, como bak.

### Windows alias:

Crie um arquivo `.bat` em algum diretório que esteja no seu `PATH`, por exemplo, `bak.bat`.

Conteúdo do `bak.bat`:

```batch
@echo off

python %USERPROFILE%\local_da_ferramenta\bak\main.py %*
```

## Configuração

Ao executar pela primeira vez, o script cria um arquivo de configuração em:

```bash
~/.local/bin/scripts/bak_config.ini
```
Esse arquivo define:

- Diretório onde os backups serão salvos
- Comando para abrir o explorador (explorer, xdg-open, etc.)
- Mecanismo de compactação (shutil, 7z, etc.)

## Como usar

| Flag            | Descrição                                                                            |
|-----------------|------------------------------------------------------------|
| `-b`, `--backup`  | Faz o backup de arquivos ou pastas                           |
| `-r`, `--rescue`  | Recupera arquivos a partir do nome ou busca              |
| `-l`, `--list`    | Lista os arquivos no diretório de backups                          | 
| `--clean`         | Limpa todos os arquivos de backup                                |
| `-o`, `--open`    | Abre o diretório de backups no explorador                  |
| `-f`, `--file`    | Um ou mais arquivos/diretórios para usar                        |
| `-s`, `--search`  | Termo(s) para buscar arquivos (fd)                                |
| `--init`          | Cria/reseta configurações                                    |

Obs: As flags `-b`, `-r`, `-l`, `--clean`, `-o`, `--init` são mutuamente exclusivas.

## Exemplos

Fazer backup de um arquivo:
```bash
python main.py -b -f meuArquivo.txt
```

Fazer backup de uma pasta (compactada):
```bash
python main.py -b -f minhaPasta/
```

Recuperar arquivo por nome:
```bash
python main.py -r -f meuArquivo_2024-05-18_20-32-10.txt.bak
```

Recuperar arquivo por busca (usa `fd`):
```bash
python main.py -r -s meuArquivo
```

Listar arquivos de backup:
```bash
python main.py -l
```

Limpar todos os backups:
```bash
python main.py --clean
```

Abrir a pasta de backups:
```bash
python main.py -o
```

Cria ou reseta o arquivo de configurações:
```bash
python main.py --init
```

## Exemplos com múltiplos arquivos

Fazer backup de vários arquivos e pastas:
```bash
python main.py -b -f arquivo1.txt arquivo2.txt pasta1/
```

Recuperar múltiplos arquivos por nome completo:
```bash
python main.py -r -f backup1_2024-05-18_20-32-10.txt.bak backup2_2024-05-18_2
```

Recuperar múltiplos arquivos por busca parcial:
```bash
python main.py -r -s backup1 backup2
```

## Estrutura do Projeto

```
backup_tool/
├── main.py          # Ponto de entrada e argumentos
├── backup.py        # Lógica de backup
├── rescue.py        # Lógica de recuperação
├── config.py        # Leitura/criação do config
├── helpers.py       # Utilitários e funções auxiliares
├── .gitignore       # Arquivos ignorados no versionamento
├── LICENSE          # Arquivo de licença
└── README.md        # Este arquivo
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
