# Importing required module
import subprocess

# Using system() method to
# execute shell commands
result = subprocess.run(["powershell", "python main.py 2 gbp"], shell=True)
print(result)