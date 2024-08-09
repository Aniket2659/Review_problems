import re
import pandas as pd
from cryptography.fernet import Fernet

def get_input():
    total_data = int(input('Enter the total number of persons: '))
    return total_data

def validate_mobile_number():
    pattern = re.compile(r'^91[0-9]{10}$')
    while True:
        mobile_number = input('Enter 10-digit mobile number starting with 91: ')
        if pattern.match(mobile_number):
            return mobile_number
        else:
            print("Invalid mobile number! Please enter a valid 10-digit number starting with 91.")

def encrypt_decrypt_mobile_number(mobile_number):
    key = Fernet.generate_key()
    cipher = Fernet(key)
    mobile_number_bytes = mobile_number.encode()
    encrypted_data = cipher.encrypt(mobile_number_bytes)
    decrypted_data = cipher.decrypt(encrypted_data).decode()
    return encrypted_data, decrypted_data

def collect_data(total_data):
    first_name = []
    last_name = []
    encrypt_mobile = []
    decrypt_mobile = []

    for _ in range(total_data):
        f_name = input('Enter first name: ')
        l_name = input('Enter last name: ')
        mobile_number = validate_mobile_number()
        
        encrypted_data, decrypted_data = encrypt_decrypt_mobile_number(mobile_number)

        first_name.append(f_name)
        last_name.append(l_name)
        encrypt_mobile.append(encrypted_data)
        decrypt_mobile.append(decrypted_data)

    return first_name, last_name, encrypt_mobile, decrypt_mobile

def create_dataframe(first_name, last_name, encrypt_mobile):
    data = {
        'first_name': first_name,
        'last_name': last_name,
        'mobile_number': encrypt_mobile
    }
    return pd.DataFrame(data)

def main():
    total_data = get_input()
    first_name, last_name, encrypt_mobile, decrypt_mobile = collect_data(total_data)
    df = create_dataframe(first_name, last_name, encrypt_mobile)
    
    print(df)
    print("\nDecrypted Mobile Numbers:")
    print(decrypt_mobile)

if __name__ == '__main__':
    main()
