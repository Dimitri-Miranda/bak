import os, shutil, subprocess
from .config import load_config
from .logger import log_warn, log_error

DESTINY_DIR, FILE_EXPLORER, FILE_ARCHIVER = load_config()


def get_bak_files_names():
    if not os.path.exists(DESTINY_DIR):
        log_error("Diretorio não existe")
        return False
    
    files = os.listdir(DESTINY_DIR)

    if not files:
        log_warn("Diretorio vazio")
        return False

    files_dict = {}
    for i, f in enumerate(files):
        files_dict[str(i)] = f

    return files_dict

#TODO: Adcicionar possibiladade de apagar de um a varios aquivos
def clean_baks_directory():
    try:
        shutil.rmtree(DESTINY_DIR)
    except FileNotFoundError:
        pass
    except Exception as e:
        log_error(f"Falha ao remover o diretorio: {e}")
        return False

    try:
        os.makedirs(DESTINY_DIR, exist_ok=True)
    except Exception as e:
        log_error(f"Falha ao criar o diretorio: {e}")
        return False

    return True

def open_backup_dir():
    if os.path.exists(DESTINY_DIR):
        try:
            subprocess.run([FILE_EXPLORER, DESTINY_DIR])
        except subprocess.CalledProcessError as e:
            log_error(f"Falha ao abrir o {FILE_EXPLORER}: {e}")
