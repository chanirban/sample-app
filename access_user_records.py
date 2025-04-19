# access_user_records.py
def display_customer_records():
    # GDPR violation: No access controls enforced
    with open("customers.txt", "r") as file:
        data = file.read()
    print("Customer Records:\n", data)

if __name__ == "__main__":
    display_customer_records()
