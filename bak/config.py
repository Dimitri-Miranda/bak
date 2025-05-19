import os, configparser, platform
from pathlib import Path
from .logger import log_error

CONFIG_FILE = Path.home() / ".config" / "bak" / "bak_config.ini"
__version__ = "25.5.1"

def check_os_file_manager():
    current_os = platform.system()

    if current_os == "Linux":
        env = os.environ

        file_managers = {
            "nautilus": ["gnome"],
            "dolphin": ["kde"],
            "thunar": ["xfce"],
            "pcmanfm-qT": ["lxqt"],
            "pcmanfm": ["lxde"],
            "nemo": ["cinnamon"],
            "caja": ["mate"],
            "io.elementary.files": ["pantheon"]
        }

        env_vars = [
            env.get("GNOME_DESKTOP_SESSION_ID", ""),
            env.get("XDG_CURRENT_DESKTOP", ""),
            env.get("DESKTOP_SESSION", ""),
            env.get("GDMSESSION", ""),
            env.get("KDE_FULL_SESSION", ""),
            env.get("KDE_SESSION_VERSION", "")
        ]

        for file_manager, keywords in file_managers.items():
            for keyword in keywords:
                if any(keyword in var.lower() for var in env_vars if var):
                    return file_manager

        log_error("Não foi possível reconhecer o sistema operacional para configurar gerenciador de aquivos padrão. Se o erro persistir, configure manualmente em 'bak_config.ini'.")
        return "undefined"

    elif current_os == "Windows":
        return "explorer"

    elif current_os == "Darwin":
        return "open"

    else:
        log_error("Não foi possível reconhecer o sistema operacional para configurar gerenciador de aquivos padrão. Se o erro persistir, configure manualmente em 'bak_config.ini'.")
        return "undefined"


def default_conifg():
    config = configparser.ConfigParser(interpolation=None)
    config.add_section("config")

    directory = Path.home() / ".bak_temp"

    config["config"]["directory"] = str(directory)
    config["config"]["file_explorer"] = check_os_file_manager()
    config["config"]["file_archiver"] = "shutil"

    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_FILE, "w") as f:
        config.write(f)

    return config


def load_config():
    if not os.path.exists(CONFIG_FILE) or (os.stat(CONFIG_FILE).st_size == 0):
        config = default_conifg()

    else:
        config = configparser.ConfigParser(interpolation=None)
        config.read(CONFIG_FILE)

    directory = config["config"]["directory"]
    file_explorer = config["config"]["file_explorer"]
    file_archiver = config["config"]["file_archiver"]

    return directory, file_explorer, file_archiver
