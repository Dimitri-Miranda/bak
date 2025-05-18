import os, shutil, subprocess
from config import load_config

DESTINY_DIR, FILE_EXPLORER, FILE_ARCHIVER = load_config()

def get_bak_files_names():
    if not os.path.exists(DESTINY_DIR):
        print("[ERRO] Diretorio não existe")
        return False
    
    files = os.listdir(DESTINY_DIR)

    if not files:
        print("[WARN] Diretorio vazio")
        return False

    files_dict = {}
    for i, f in enumerate(files):
        files_dict[str(i)] = f

    return files_dict

def clean_baks_directory():
    try:
        shutil.rmtree(DESTINY_DIR)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"[ERRO] Falha ao remover o diretorio: {e}")
        return False

    try:
        os.makedirs(DESTINY_DIR, exist_ok=True)
    except Exception as e:
        print(f"[ERRO] Falha ao criar o diretorio: {e}")
        return False

    return True

def open_backup_dir():
    if os.path.exists(DESTINY_DIR):
        try:
            subprocess.run([FILE_EXPLORER, DESTINY_DIR], check=True)
        except subprocess.CalledProcessError as e:
            print(f"[ERRO] Falha ao abrir o {FILE_EXPLORER}:", e)

def log_info(msg): return (f"\033[35m[INFO]\033[0m {msg}")

def log_ok(msg): print(f"\033[92m[OK]\033[0m {msg}")

def log_warn(msg): print(f"\033[93m[WARN]\033[0m {msg}")

def log_error(msg): print(f"\033[91m[ERRO]\033[0m {msg}")
