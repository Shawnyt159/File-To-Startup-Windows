import os
import shutil

file_to_move = ""

user_profile = os.environ['USERPROFILE']
startup_folder = user_profile + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"

shutil.move(file_to_move, startup_folder)


