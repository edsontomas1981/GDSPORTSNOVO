import re

def validar_senha(senha):
    if len(senha) < 8:
        return False
    if not re.search("[a-zA-Z]", senha):
        return False
    if not re.search("[0-9]", senha):
        return False
    if not re.search("[!@#$%^&*()_+-]", senha):
        return False
    return True