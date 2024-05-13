import re
def extract_emails(file_path):
    try:
        
        with open(file_path, 'r') as file:
            
            content = file.read()

            
            email_addresses = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', content)

           
            print("Extracted email addresses:")
            for email in email_addresses:
                print(email)

    except FileNotFoundError:
        print("Error: The specified file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


file_path = "contacts.txt"


extract_emails(file_path)