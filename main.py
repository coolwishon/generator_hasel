import subprocess
import sys
import importlib
required_libraries = ['cryptography', 'pyperclip', 'colorama']

for lib in required_libraries:
    try:
        importlib.import_module(lib)
    except ImportError:
        print(f"📦 biblioteka '{lib}' nie jest wgrana, wgrywam...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", lib])

import random
import string
import pyperclip
import os
from cryptography.fernet import Fernet


def generate_password(length):
    if length < 4:
        return "Hasło musi byc o długości conajmniej 4 znaków"

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def create_file_if_not_exists(filename):
    if not os.path.exists(filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write("🔒 Menedżer haseł - zapisane strony i hasła do nich 🔒\n")
            file.write("=======================================\n\n")

def save_password(site, password):
    with open('dane.txt', 'a', encoding='utf-8') as file:
        file.write(f"Witryna: {site} | Hasło: {password}\n")

def load_or_create_key():
    if not os.path.exists('key.key'):
        key = Fernet.generate_key()
        with open('key.key', 'wb') as key_file:
            key_file.write(key)
    else:
        with open('key.key', 'rb') as key_file:
            key = key_file.read()
    return key

def encrypt_password(password, key):
    f = Fernet(key)
    encrypted_password = f.encrypt(password.encode())
    return encrypted_password

def main():
    create_file_if_not_exists('dane.txt')
    key = load_or_create_key()
    
    try:
        length = int(input("🔒 Wpisz długość hasła (min. 4 znaki): "))
        site = input("🌐 Podaj nazwę witryny (np. gmail.com): ").strip()
        
        generated_password = generate_password(length)
        ##print(f"✅ Twoje hasło do {site} to: {generated_password}") # usuń hasztagi "##" na początku linii aby program wyświetlił hasło do użytkownika (niebezpieczny zabieg)
        
        ##pyperclip.copy(generated_password) #Usuń hasztagi "##" aby program kopiował hasło do schowka
        ##print("📋 Hasło zostało skopiowane do schowka!") 

        choice = input("🛡️ Czy chcesz zaszyfrować hasło przed zapisem? (T/N) (T odpowiada Tak - N odpowiada Nie): ").strip().upper()
        
        if choice == 'T':
            encrypted_password = encrypt_password(generated_password, key)
            save_password(site, encrypted_password.decode())
            print("💾 Zaszyfrowane hasło zapisane w pliku dane.txt")
        else:
            save_password(site, generated_password)
            print("💾 Hasło zapisane w pliku dane.txt (bez szyfrowania)")
    except ValueError:
        print("❌ niepoprawna liczba, wpisz ponownie poprawna")

if __name__ == "__main__":
    main()
