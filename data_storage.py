# data_storage.py
def save_user_data(user_data):
    # GDPR violation: Data stored insecurely in plaintext format
    with open("customers.txt", "a") as file:
        file.write(f"{user_data}\n")

if __name__ == "__main__":
    sample_user = {'full_name': 'Jane Doe', 'email': 'jane@example.com', 'phone': '+447123456789'}
    save_user_data(sample_user)
    print("User data saved to customers.txt")
