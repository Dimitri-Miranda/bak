import os, argparse
from backup import handle_backup
from rescue import handle_rescue
from helpers import clean_baks_directory, get_bak_files_names, open_backup_dir, log_info, log_ok
from config import default_conifg

def main():
    parser = argparse.ArgumentParser(
        prog="bak",
        description="Tool de backups",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Exemplos de uso:\n"
               "  bak -b -f meuArquivo.txt\n"
               "  bak -r -f meuArquivo_1747371147836.txt\n"
               "  bak -r -s meuArquivo\n"
               "  bak -l\n"
               "  bak --clean\n"
               "  bak -o\n"
               "  bak --init\n"
    )

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-b", "--backup", action="store_true", help="Faz o backup do arquivo")
    group.add_argument("-r", "--rescue", action="store_true", help="Recupera o arquivo")
    group.add_argument("--clean", action="store_true", help="Limpa o diretorio de backups")
    group.add_argument("-l", "--list", action="store_true", help="Lista os arquivos no diretorio de backups")
    group.add_argument("-o", "--open", action="store_true", help="Abre o diretorio de backups no Explorer")
    group.add_argument("--init", action="store_true", help="Criar ou resetar configuração")

    parser.add_argument("-f", "--file", nargs="+", help="Arquivo a para o backup ou ser recuperado, use com -b ou -r")
    parser.add_argument("-s", "--search", nargs="+", help="Recupera um arquivo por parte do nome do arquivo, use com -r")

    args = parser.parse_args()

    if args.backup:
        if not args.file:
            parser.error(log_info("Para fazer o backup de um arquivo, use -b junto com -f\nExemplo -> bak -b -f meuArquivo.txt"))

        saved_files = handle_backup(args.file)
        for file in saved_files: log_ok(f"Arquivo salvo em '{file}'")

    elif args.rescue:
        if not args.file and not args.search:
            parser.error(log_info("Para fazer o resgate de um arquivo, use -r junto com -f ou -fd\nExemplo -> bak -b -r meuArquivo.txt"))

        rescue_files = handle_rescue(args.file, args.search)
        if rescue_files:
            for file in rescue_files: log_ok(f"Arquivo '{os.path.basename(file)}' recuperado")
    
    elif args.clean:
        clean_baks_directory()
        log_ok("Diretorio limpo com sucesso")

    elif args.list:
        file_dict = get_bak_files_names()

        if file_dict:
            log_ok("Arquivos no diretorio:\n")
            for file in file_dict: print(f"[\033[91m{file}\033[0m] \033[36m{file_dict[file]}\033[0m")

    elif args.open:
        open_backup_dir()

    elif args.init:
        log_ok("Arquivo de configuração criado/resetado")
        default_conifg()

if __name__ == "__main__":
    main()
