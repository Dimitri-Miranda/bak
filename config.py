from pathlib import Path
import os, configparser

def default_conifg():
    CONFIG_FILE = Path.home() / ".local" / "bin" / "scripts" / "bak_config.ini"

    config = configparser.ConfigParser(interpolation=None)
    config.add_section("config")

    directory = Path.home() / ".local" / "bin" / "bak_temp"

    config["config"]["directory"] = str(directory)
    config["config"]["file_explorer"] = "explorer"
    config["config"]["file_archiver"] = "shutil"

    CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)

    with open(CONFIG_FILE, "w") as f:
        config.write(f)

    return config


def load_config():
    CONFIG_FILE = Path.home() / ".local" / "bin" / "scripts" / "bak_config.ini"

    if not os.path.exists(CONFIG_FILE) or (os.stat(CONFIG_FILE).st_size == 0):
        config = default_conifg()

    else:
        config = configparser.ConfigParser(interpolation=None)
        config.read(CONFIG_FILE)

    directory = config["config"]["directory"]
    file_explorer = config["config"]["file_explorer"]
    file_archiver = config["config"]["file_archiver"]

    return directory, file_explorer, file_archiver
