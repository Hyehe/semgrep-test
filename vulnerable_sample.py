# vulnerable_sample.py

import os
import hashlib
import sqlite3
import subprocess

# ─── Security: 하드코딩된 비밀번호 ───
DB_PASSWORD = "admin1234"
SECRET_KEY = "supersecretkey123"

# ─── Security: 약한 암호화 (MD5) ───
def hash_password(pw):
    return hashlib.md5(pw.encode()).hexdigest()

# ─── Security: SQL Injection 취약점 ───
def get_user(username):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchall()

# ─── Security Hotspot: 사용자 입력을 그대로 실행 ───
def run_command(cmd):
    os.system(cmd)

# ─── Reliability: None 체크 없이 사용 ───
def get_username(user):
    return user["name"].upper()

# ─── Reliability: 예외처리 없음 ───
def divide(a, b):
    return a / b

# ─── Maintainability: 중복 코드 ───
def process_user_a(user):
    name = user["name"]
    age = user["age"]
    email = user["email"]
    print(f"{name}, {age}, {email}")
    return name

def process_user_b(user):
    name = user["name"]
    age = user["age"]
    email = user["email"]
    print(f"{name}, {age}, {email}")
    return age

# ─── Maintainability: 너무 복잡한 함수 ───
def complex_logic(a, b, c, d, e):
    if a > 0:
        if b > 0:
            if c > 0:
                if d > 0:
                    if e > 0:
                        return a + b + c + d + e
                    else:
                        return a + b + c + d
                else:
                    return a + b + c
            else:
                return a + b
        else:
            return a
    else:
        return 0

# ─── 실행 ───
if __name__ == "__main__":
    print(hash_password(DB_PASSWORD))
    get_user("admin")
    run_command("dir")
    divide(10, 0)