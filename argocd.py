import os
import requests
import sys
from pathlib import Path
import winreg

# --- Variables ---
install_path = Path("C:/ArgoCD-CLI")
install_path.mkdir(exist_ok=True)
argo_exe_path = install_path / "argocd.exe"

# --- 1️⃣ Récupérer la dernière version d'Argo CD ---
print("Récupération de la dernière version d'Argo CD...")
latest_release = requests.get("https://api.github.com/repos/argoproj/argo-cd/releases/latest").json()
version = latest_release["tag_name"]
print(f"Dernière version trouvée : {version}")

# --- 2️⃣ Télécharger argocd.exe ---
url = f"https://github.com/argoproj/argo-cd/releases/download/{version}/argocd-windows-amd64.exe"
print(f"Téléchargement depuis {url} ...")
response = requests.get(url, stream=True)
total_size = int(response.headers.get('content-length', 0))
with open(argo_exe_path, "wb") as f:
    downloaded = 0
    for data in response.iter_content(1024*1024):  # 1 MB par chunk
        f.write(data)
        downloaded += len(data)
        done = int(50 * downloaded / total_size)
        sys.stdout.write(f"\r[{'█' * done}{'.' * (50-done)}] {downloaded/1024/1024:.1f}/{total_size/1024/1024:.1f} MB")
        sys.stdout.flush()
print("\nTéléchargement terminé !")

# --- 3️⃣ Ajouter au PATH utilisateur ---
def add_to_user_path(new_path):
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_READ) as key:
        try:
            current_path, _ = winreg.QueryValueEx(key, "Path")
        except FileNotFoundError:
            current_path = ""

    if new_path.lower() in current_path.lower():
        print(f"{new_path} est déjà dans le PATH utilisateur")
        return

    new_path_value = current_path + ";" + new_path if current_path else new_path
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Environment", 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, "Path", 0, winreg.REG_EXPAND_SZ, new_path_value)
    print(f"{new_path} ajouté au PATH utilisateur")
    print("Fermez et rouvrez votre terminal pour que le PATH soit pris en compte.")

add_to_user_path(str(install_path))
