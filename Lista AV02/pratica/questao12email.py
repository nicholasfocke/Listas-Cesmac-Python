import re

def possui_arroba(email):
    return '@' in email

def email_valido_regex(email):
    # Regex simples para validar estrutura de e-mail
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(padrao, email) is not None

print(possui_arroba("teste@email.com"))             # Saída: True
print(email_valido_regex("teste@email.com"))        # Saída: True
print(email_valido_regex("invalido@@.com"))         # Saída: False