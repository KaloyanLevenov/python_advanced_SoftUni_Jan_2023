import re


class NameTooShortError(Exception):
    def __str__(self):
        return 'Name must be more than 4 characters'


class MustContainAtSymbolError(Exception):
    def __str__(self):
        return 'Email must contain @'


class InvalidDomainError(Exception):
    def __str__(self):
        return 'Domain must be one of the following: .com, .bg, .org, .net'


while True:
    email = input()

    if email == 'End':
        break

    name_regex = r"[a-z]{5,}|[0-9]{5,}(?=@)"
    domain_regex = r"bg|com|org|net$"
    name_is_valid = re.findall(name_regex, email)
    domain_is_valid = re.findall(domain_regex, email)

    try:
        if '@' not in email:
            raise MustContainAtSymbolError
        if not name_is_valid:
            raise NameTooShortError
        if not domain_is_valid:
            raise InvalidDomainError

    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError) as text:
        print(text)

    else:
        print("Email is valid")
