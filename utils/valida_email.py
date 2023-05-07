import re

def valida_email(email):
    """
    Verifica se o endereço de email é válido.

    Retorna True se o endereço de email for válido, False caso contrário.
    """
    if not email:
        return False

    # Regex para verificar a validade do email
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    regex = re.compile(pattern)

    return regex.match(email) is not None
