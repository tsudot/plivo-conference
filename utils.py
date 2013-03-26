
def clean_phone_number(phone_no):
    if phone_no is None or phone_no == '':
        return phone_no
    phone_no = str(phone_no)
    phone_no = phone_no.strip()
    if phone_no.startswith('+'):
        phone_no = phone_no[1:]
    if phone_no.startswith('00'):
        phone_no = phone_no[2:]
    if phone_no.startswith('0'):
        phone_no = phone_no[1:]
    wild_chars = (',', ';', '(', ')', '-', '.', ' ', '+', '/', '%', '@', '!', '=', '&')
    for char in wild_chars:
        phone_no = phone_no.replace(char, '')
    return phone_no


def verify_phone_number(phone_no):
    if not phone_no.startswith('91'):
        return None
    return phone_no

