# export_data.py
def export_customer_data():
    with open("customers.txt", "r") as file:
        data = file.read()

    # GDPR violation: Exporting data without encryption
    with open("customer_export.csv", "w") as export_file:
        export_file.write(data)

    print("Customer data exported to customer_export.csv without encryption")

if __name__ == "__main__":
    export_customer_data()
