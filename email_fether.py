import re
import sys

'''
A simple python script that will extract all the emails from a given file

Usages:
python3 email_fetcher file.txt

'''

file_name = sys.argv[1]

# Opening the file
file = open(file_name)

contents = file.read()

# Use a regular expression to search for all email addresses in the text
email_pattern = r'[\w\.-]+@[\w\.-]+'
email_addresses = re.findall(email_pattern, contents)

# Count the number of email addresses
email_count = len(email_addresses)

# Print the results
print(f'Number of email addresses found: {email_count}')
print()
print('Email addresses:')
for email in email_addresses:
    print(email)
