import re


def mutate_phone_number(phone_string):
    pattern = r'[(+-/ _=())]'
    phone_number = int(re.sub(pattern, "", phone_string))
    return phone_number
