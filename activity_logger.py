# activity_logger.py
import logging

logging.basicConfig(filename="activity.log", level=logging.INFO)

def log_customer_activity(user_data, action="registered"):
    # GDPR violation: Logging unmasked sensitive personal information
    logging.info(f"Customer {user_data['email']} ({user_data['phone']}) has {action}.")

if __name__ == "__main__":
    user_activity = {'full_name': 'John Smith', 'email': 'johnsmith@example.com', 'phone': '+441234567890'}
    log_customer_activity(user_activity)
    print("Logged customer activity including PII to activity.log")
