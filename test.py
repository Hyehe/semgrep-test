import os
import hashlib

password = "admin1234"

def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()

def run_command(cmd):
    os.system(cmd)

result = hash_password(password)
print(result)