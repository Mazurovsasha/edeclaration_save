import os
import shutil
import zipfile
from datetime import datetime, timedelta

# Путь к директории, где находятся папки EDeclaration_*
base_dir = "D:\\"
# Путь к директории, куда будем сохранять скопированные папки edecl
save_dir = os.path.join(base_dir, "save_edecl", "save")
# Путь к директории, куда будем сохранять архивы
archive_dir = os.path.join(base_dir, "save_edecl", "arhiv")

# Создаем необходимые директории, если они не существуют
os.makedirs(save_dir, exist_ok=True)
os.makedirs(archive_dir, exist_ok=True)

# Проходим все папки в base_dir
for folder_name in os.listdir(base_dir):
    if folder_name.startswith("EDeclaration_"):
        edecl_path = os.path.join(base_dir, folder_name, "edecl")
        if os.path.isdir(edecl_path):
            # Копируем папку edecl в save_dir/folder_name/edecl
            dest_path = os.path.join(save_dir, folder_name, "edecl")
            os.makedirs(dest_path, exist_ok=True)
            shutil.copytree(edecl_path, dest_path, dirs_exist_ok=True)

# Создаем архив с именем текущей даты
today_date = datetime.now().strftime("%Y-%m-%d")
archive_path = os.path.join(archive_dir, f"{today_date}.zip")

# Архивируем содержимое save_dir
with zipfile.ZipFile(archive_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(save_dir):
        for file in files:
            file_path = os.path.join(root, file)
            arcname = os.path.relpath(file_path, save_dir)
            zipf.write(file_path, arcname)

# Очищаем папку save_dir после архивирования
shutil.rmtree(save_dir)
os.makedirs(save_dir, exist_ok=True)

# Удаляем архивы, которым больше 1 года и 4 месяцев
expiration_time = datetime.now() - timedelta(days=486)  # 1 год и 4 месяца примерно 486 дней
for archive_file in os.listdir(archive_dir):
    archive_file_path = os.path.join(archive_dir, archive_file)
    if os.path.isfile(archive_file_path):
        file_creation_time = datetime.fromtimestamp(os.path.getctime(archive_file_path))
        if file_creation_time < expiration_time:
            os.remove(archive_file_path)

print("Все Готово!")
