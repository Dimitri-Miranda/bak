import os
from .config import load_config
from .helpers import get_bak_files_names, file_per_index
from .logger import log_ok, log_warn, log_error

DESTINY_DIR, FILE_EXPLORER, FILE_ARCHIVER = load_config()

def clean_file(file_path):
    file_dict = get_bak_files_names()

    # vai pegar o nome do arquivo caso tenha sido passado por index
    file_path = file_per_index(file_dict, file_path)

    file_origin = os.path.join(DESTINY_DIR, file_path)

    if not os.path.exists(file_origin):
        log_warn(f"Arquivo '{file_path}' não encontrado.")
        return

    os.remove(os.path.join(DESTINY_DIR, file_path))
    log_ok(f"Arquivo '{file_path}' apagado com sucesso")

    return file_path

def clean_multiples(file_list):
    del_list = set()

    for file in file_list:
        if file not in del_list:
            c_file = clean_file(file)
            del_list.add(c_file)

    return del_list

def handle_clean(file_list=None):
    if not file_list:
        bak_files = get_bak_files_names()
        try:
            for bak in bak_files.values():
                os.remove(os.path.join(DESTINY_DIR, bak))

            log_ok("Diretorio limpo com sucesso")

        except Exception as e:
            log_error(f"Erro ao apagar arquivo '{e}'")
            return None

        return None

    clean_files_list = clean_multiples(file_list)

    return clean_files_list
