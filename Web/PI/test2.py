import subprocess
import os

subprocess.call(["python", "Uploads/upload.py"])
print("end of script")

os.remove("Uploads/upload.py")