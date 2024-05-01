import sys
import re

def find_emails_in_file(file_path):
    """
    Function to find email addresses in a text file.
    
    Args:
    file_path (str): Path to the text file.
    
    Returns:
    list: List of found email addresses.
    """
    with open(file_path, 'r') as file:
        text = file.read()
        pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        emails = re.findall(pattern, text)
    return emails

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <path_to_text_file>")
        sys.exit(1)
        
    file_path = sys.argv[1]
    emails = find_emails_in_file(file_path)
    if emails:
        print("Found email addresses:")
        for email in emails:
            print(email)
    else:
        print("There are no email addresses in the text file.")

if __name__ == "__main__":
    main()
