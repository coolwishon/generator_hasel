from cryptography.fernet import Fernet

def load_key():
    with open('key.key', 'rb') as key_file:
        return key_file.read()

def decrypt_password(encrypted_password, key):
    f = Fernet(key)
    decrypted_password = f.decrypt(encrypted_password.encode())
    return decrypted_password.decode()

def find_encrypted_password(site_name):
    try:
        with open('dane.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            for line in lines:
                if site_name.lower() in line.lower():
                    if "Hasło:" in line:
                        encrypted_part = line.split("Hasło:")[1].strip()
                        return encrypted_part
        return None
    except FileNotFoundError:
        print("❌ Nie znaleziono pliku dane.txt")
        return None

def main():
    site = input("🌐 Podaj nazwę witryny, której hasło chcesz odszyfrować: ").strip()
    key = load_key()
    encrypted_password = find_encrypted_password(site)
    
    if encrypted_password:
        try:
            decrypted_password = decrypt_password(encrypted_password, key)
            print(f"✅ Odszyfrowane hasło do {site} to: {decrypted_password}")
        except Exception as e:
            print("❌ Błąd podczas odszyfrowywania hasła.")
            print(e)
    else:
        print("❌ Nie znaleziono zaszyfrowanego hasła dla tej witryny.")

if __name__ == "__main__":
    main()
