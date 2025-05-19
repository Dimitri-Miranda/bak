import os, shutil, subprocess
from datetime import datetime
from .config import load_config
from .logger import log_ok, log_error, log_warn

DESTINY_DIR, FILE_EXPLORER, FILE_ARCHIVER = load_config()


def compress_dir(directory):
    if FILE_ARCHIVER.lower() == "7z" or FILE_ARCHIVER == "7zip":
        try:
            file_zip = f"{directory}.zip"
            subprocess.run([FILE_ARCHIVER, "a", file_zip, directory], check=True)
            log_ok(f"Diretorio '{os.path.basename(directory)}' compactado com sucesso")

            return file_zip
            
        except subprocess.CalledProcessError as e:
            log_error(f"Falha ao comprimir o diretorio '{directory}', cheque se o 7zip esta no PATH {e}")
        except FileNotFoundError:
            log_error("Diretorio não encontrado")
        except PermissionError:
            log_error("Sem permissão para acessar arquivos ou salvar o arquivo")
        except Exception as e:
            log_error(f"Erro inesperado ao usar 7-Zip: {e}")
    # fallback para shutill
    else:
        try:
            shutil.make_archive(base_name=directory, format="zip", root_dir=directory)
            log_ok(f"Diretorio '{os.path.basename(directory)}' compactado com sucesso")
            file_zip = f"{directory}.zip"

            return file_zip

        except FileNotFoundError:
            log_error("Diretorio não encontrado")
        except PermissionError:
            log_error("Sem permissão para acessar arquivos ou salvar o arquivo")
        except Exception as e:
            log_error(f"Erro inesperado ao usar shutil: {e}")

def copy_file_to_bak(file_path):
    if not os.path.exists(file_path):
        log_error(f"Arquivo '{file_path}' não encontrado.")
        return

    if not os.path.exists(DESTINY_DIR):
        os.makedirs(DESTINY_DIR)

    file_name = os.path.basename(file_path)
    file_name_no_ext, file_extension = os.path.splitext(file_name)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    destiny_file = os.path.join(DESTINY_DIR, f"{file_name_no_ext}_{timestamp}{file_extension}.bak")

    shutil.copy2(file_path, destiny_file)

    return destiny_file

def copy_file_to_bak_multiples(file_list):
    destiny_file_list = []

    for file in file_list:
        destiny_file = copy_file_to_bak(file)

        if destiny_file:
            destiny_file_list.append(destiny_file)

    return destiny_file_list

def handle_backup(args_file):
    dir_list = []
    file_list = []

    for file in args_file:
        file_path = os.path.join(os.getcwd(), file)
        if os.path.isdir(file_path):
            file_path_zipped = compress_dir(file_path)
            dir_list.append(file_path_zipped)

        elif os.path.isfile(file_path):
            file_list.append(file_path)

        else:
            log_warn(f"Arquivo {file_path} não existe")

    saved_files = []
    if dir_list:
        saved_files += copy_file_to_bak_multiples(dir_list)
        for dir in dir_list: 
            if os.path.exists(dir): 
                os.remove(dir) 

            else: 
                log_error(f"Erro ao apagar {dir}\n[WARN] Esse arquivo é temporario, não se preocupe")

    if file_list:
        saved_files += copy_file_to_bak_multiples(file_list)

    return saved_files
