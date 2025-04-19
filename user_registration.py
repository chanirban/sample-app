# user_registration.py
def register_user():
    print("User Registration")
    full_name = input("Enter Full Name: ")
    email = input("Enter Email Address: ")
    phone = input("Enter Phone Number: ")

    user_data = {
        'full_name': full_name,
        'email': email,
        'phone': phone
    }

    # GDPR violation: No consent collected or privacy notice presented
    return user_data

if __name__ == "__main__":
    user = register_user()
    print("Registered user data:", user)
