import re

def regex_email(email: str) -> bool:
    req = re.match(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(.[A-Z|a-z]{2,})+', email)
    return True if req else False
