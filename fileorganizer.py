import os
import tkinter as tk
from tkinter import filedialog
import ttkbootstrap as ttk

window = ttk.Window(themename = 'morph')
window.geometry("350x120")
window.title("Files Orangizer")
photo = tk.PhotoImage(file = "appimage.png")
window.iconphoto(False, photo)
# window.withdraw()

def organize_folder():
    folderpath = filedialog.askdirectory(title="Select a Folder")

    # folderpath = input()

    extensions = {
        "audios": ["mp3", "wav", "flac"],
        "videos": ["mp4", "mkv", "avi"],
        "pdfs": ["pdf"],
        "word": ["doc", "docx"],
        "pictures": ["jpg", "jpeg", "png"],
        "executables": "exe",
        "presentations": "pptx",
        "zip files": "zip"
        }

    for files in os.listdir(folderpath):
        filepath = os.path.join(folderpath, files)
        if os.path.isfile(filepath):
            file_extention = (os.path.splitext(filepath)[1])[1:]
            miscellaneous_flag = True
            for key, value in extensions.items():
                if file_extention in value:
                    os.makedirs(os.path.join(folderpath, key), exist_ok = True)
                    os.rename(filepath, os.path.join(folderpath, key, files))
                    miscellaneous_flag = False
            if miscellaneous_flag:
                os.makedirs(os.path.join(folderpath, "miscellaneous"), exist_ok = True)
                os.rename(filepath, os.path.join(folderpath, "miscellaneous", files))

                
title_label = ttk.Label(master = window, text="Files Organizer", font = 'Calibri 24 bold')
title_label.pack()

selection_frame = ttk.Frame(master = window)
select_label = ttk.Label(master = selection_frame, text="Select a Folder", font = 'Calibri 12 bold')
button = ttk.Button(master = selection_frame, text = "Select", command = organize_folder)
select_label.pack(side = 'left', padx= 5)
button.pack(side = 'left')
selection_frame.pack(pady=10)
                
window.mainloop()