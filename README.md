Email Data Extractor
A Python utility for extracting specific data from raw emails.

Features:
Email Count: Analyze and get a count of occurrences for each email address.
Phone Number Extraction: Retrieve all phone numbers from the raw emails.
Address Extraction: Extract and structure address details including state, city, zip code, street name, and street number.
Usage:
python
Copy code
from extractor import get_email_info, get_email_count, get_phone_list, get_address_list

# Read and parse raw emails
emails = get_email_info("path_to_raw_emails.txt")

# Get email counts
email_counts = get_email_count(emails)

# Extract phone numbers
phone_numbers = get_phone_list(emails)

# Extract addresses
addresses = get_address_list(emails)
Dependencies:
Python 3.x
re module for regular expressions
Notes:
The provided functions are optimized for the given email format. Depending on the variations in your raw emails, some adjustments might be required.

This description provides an overview of your project, highlights its main features, and gives a basic usage guide. Adjustments can be made based on any other details or features you might add to the project in the future.
