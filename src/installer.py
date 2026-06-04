import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

APP_NAME = "007 First Light Thai Localization"

def select_folder():
    folder = filedialog.askdirectory(title="Select 007 First Light folder")
    if folder:
        path_entry.delete(0, tk.END)
        path_entry.insert(0, folder)

def copy_folder(source, destination):
    if not os.path.exists(source):
        raise FileNotFoundError("Localization folder not found.")

    os.makedirs(destination, exist_ok=True)

    for item in os.listdir(source):
        src = os.path.join(source, item)
        dst = os.path.join(destination, item)

        if os.path.isdir(src):
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            shutil.copy2(src, dst)

def install_localization():
    game_path = path_entry.get().strip()

    if not game_path:
        messagebox.showerror("Error", "Please select the game folder.")
        return

    if not os.path.exists(game_path):
        messagebox.showerror("Error", "Selected folder does not exist.")
        return

    source = os.path.join(os.getcwd(), "Localization")
    destination = os.path.join(game_path, "Localization")

    try:
        copy_folder(source, destination)
        messagebox.showinfo("Success", "Thai localization installed successfully.")
    except Exception as e:
        messagebox.showerror("Installation Error", str(e))

root = tk.Tk()
root.title(APP_NAME)
root.geometry("600x260")
root.resizable(False, False)

tk.Label(root, text=APP_NAME, font=("Segoe UI", 16, "bold")).pack(pady=15)

tk.Label(
    root,
    text="Install Thai interface, subtitles, menus and story localization.",
    font=("Segoe UI", 10)
).pack(pady=5)

frame = tk.Frame(root)
frame.pack(pady=20)

path_entry = tk.Entry(frame, width=58)
path_entry.pack(side=tk.LEFT, padx=5)

tk.Button(frame, text="Browse", command=select_folder).pack(side=tk.LEFT)

tk.Button(
    root,
    text="Install Thai Localization",
    font=("Segoe UI", 11, "bold"),
    width=26,
    command=install_localization
).pack(pady=10)

tk.Label(
    root,
    text="007 First Light Thai Localization",
    font=("Segoe UI", 8)
).pack(side=tk.BOTTOM, pady=10)

root.mainloop()
