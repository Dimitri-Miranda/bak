import os, shutil
from .config import load_config
from .logger import log_ok, log_warn, log_error
from .helpers import get_bak_files_names, search_fd, file_per_index

DESTINY_DIR, FILE_EXPLORER, FILE_ARCHIVER = load_config()

def rescue_file(file_path):
    file_dict = get_bak_files_names()

    # vai pegar o nome do arquivo caso tenha sido passado por index
    file_path = file_per_index(file_dict, file_path)

    dir_cwd = os.getcwd()

    file_origin = os.path.join(DESTINY_DIR, file_path)

    if not os.path.exists(file_origin):
        log_warn(f"Arquivo '{file_path}' não encontrado.")
        return

    file_base, file_ext = os.path.splitext(file_path)

    file_destiny = os.path.join(dir_cwd, file_base)

    shutil.copy2(file_origin, file_destiny)

    return file_destiny

def rescue_multiples(file_list):
    rescue_file_list = []

    for file in file_list:
        r_file = rescue_file(file)

        if r_file:
            rescue_file_list.append(r_file)

    return rescue_file_list

def handle_rescue(args_file=None, args_search=None):

    if args_file:
        rescue_files = rescue_multiples(args_file)

        return rescue_files

    if args_search:
        for file in args_search:
            fd_file = search_fd(file, DESTINY_DIR)

            if fd_file:
                try:
                    saved_file = rescue_file(fd_file)
                    log_ok(f"Arquivo '{os.path.basename(saved_file)}' recuperado")
                except:
                    log_error(f"Arquivo '{fd_file}' não encontrado")
            else:
                log_warn(f"Arquivo com o termo '{file}' não encontrado")

        return None
