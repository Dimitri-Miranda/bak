import os , subprocess, shutil, glob
from .config import load_config
from .logger import log_warn, log_error

DESTINY_DIR, FILE_EXPLORER, FILE_ARCHIVER = load_config()

# retorna o nome do arquivo, em um dict com chave de numero inteiro e valor o arquivo
def file_per_index(file_dict, file_path):
    if file_dict and file_path in file_dict:
        file_path = file_dict[file_path]

    return file_path

def get_bak_files_names():
    if not os.path.exists(DESTINY_DIR):
        log_error("Diretorio não existe")
        return {}
    
    files = os.listdir(DESTINY_DIR)

    if not files:
        log_warn("Diretorio vazio")
        return {}

    files_dict = {}
    for i, f in enumerate(files):
        files_dict[str(i)] = f

    return files_dict

def open_backup_dir():
    if os.path.exists(DESTINY_DIR):
        try:
            subprocess.run([FILE_EXPLORER, DESTINY_DIR])
        except subprocess.CalledProcessError as e:
            log_error(f"Falha ao abrir o {FILE_EXPLORER}: {e}")

# TODO: colocar fallbakc glob
def search_fd(term, dir=None):
    if not dir:
        dir = "."

    if shutil.which("fd"):
        try:
            results = subprocess.run(["fd", term, dir], capture_output=True, text=True, check=True)
            files = results.stdout.strip().split("\n")

            file_path = os.path.basename(files[0]) if files else None

            return file_path

        except subprocess.CalledProcessError as e:
            log_error(f"Falha ao rodar comando fd: {e}")
            return None
    else:
        pattern = os.path.join(dir, "**", f"*{term}*")

        file = next(glob.iglob(pattern), None)

        return file
