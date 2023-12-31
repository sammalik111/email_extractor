import re
import os
import unittest
from pprint import pprint


def get_email_info(filename: str) -> list:
    """return a list of emails with the raw data

    Args:
        filename (str): file name

    Returns:
        list(str): a list of strings, each of them contains the detailed inforamtion of an email
    """
    source_dir = os.path.dirname(__file__)
    full_path = os.path.join(source_dir, filename)
    with open(full_path) as f:
        return f.read().split("\n-----\n")


def get_email_count(email_info: list) -> dict:
    """return a dictionary counting how many times an email address occurs

    Args:
        email_info (list): a list of strings, each of them contains the detailed inforamtion of an email

    Returns:
        email_count (dict): a dictionary with email address as key and count as value
    """
    # TODO: implement this function
    email_count = {}
    email_pattern = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}")
    
    for email in email_info:
        found_emails = email_pattern.findall(email)
        for e in found_emails:
            if e in email_count:
                email_count[e] += 1
            else:
                email_count[e] = 1
                
    return email_count


def get_phone_list(email_info: list) -> list:
    """return a list of phone numbers.

    Args:
        email_info (list): a list of strings, each of them contains the detailed inforamtion of an email

    Returns:
        phone_list (list): a list of raw phone numbers
    """
    # TODO: implement this function
    phone_pattern = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")
    phone_list = []
    
    for email in email_info:
        phones = phone_pattern.findall(email)
        for phone in phones:
            phone_list.append(phone)
            
    return phone_list



def get_address_list(email_info: list) -> list:
    """return a list of address information.

    Args:
        email_info (list): a list of strings, each of them contains the detailed inforamtion of an email

    Returns:
        address_list (list): a list of tuples, each tuple contains state, city, zip code, street name and street number
    """
    address_pattern = re.compile(
        r"(\d+)\s+([a-zA-Z\s]+(?:St|Ave|Ln|Street|Avenue|Lane)),?\s*([a-zA-Z\s]+),?\s*([A-Z]{2})\s*(\d{5})"
    )
    address_list = []
    
    for email in email_info:
        addresses = address_pattern.findall(email)
        for address in addresses:
            # reordering the extracted data to match the expected output format
            reordered_address = (address[3], address[2], address[4], address[1], address[0])
            address_list.append(reordered_address)
            
    return address_list



def main():
    # call the funcitons
    emails = get_email_info("new_test.txt")
    email_count = get_email_count(emails)
    phone_list = get_phone_list(emails)
    address_list = get_address_list(emails)

    # print your outputs
    print()
    pprint(email_count)
    print()
    pprint(phone_list)
    print()
    pprint(address_list)
    print()

    # unit tests
    unittest.main(verbosity=2)


# Please don't change the test cases
class TestAllMethod(unittest.TestCase):
    def setUp(self):
        self.email_info = get_email_info("raw_emails.txt")
        self.email_count = get_email_count(self.email_info)
        self.email_count_ans = {
            "nicolelam@gmail.com": 4,
            "vinnysu@gmail.com": 2,
            "mikex@gmail.com": 3,
        }
        self.phone_list = get_phone_list(self.email_info)
        self.phone_list_ans = [
            "(555)765-4321",
            "666-555-1111",
            "(888)765 4321",
            "608 901 2345",
        ]
        self.address_list = get_address_list(self.email_info)
        self.address_list_ans = [
            ("MI", "Ann Arbor", "48104", "E William St", "516"),
            ("MI", "Ann Arbor", "48109", "S State St", "530"),
            ("MI", "Ann Arbor", "48104", "Maynard St", "347"),
            ("MI", "Ann Arbor", "48109", "Duffield St", "1931"),
        ]

    def test_get_email_count(self):
        self.assertEqual(self.email_count, self.email_count_ans)

    def test_get_phone_list(self):
        self.assertEqual(self.phone_list, self.phone_list_ans)

    def test_get_address_list(self):
        self.assertEqual(self.address_list, self.address_list_ans)


if __name__ == "__main__":
    main()
