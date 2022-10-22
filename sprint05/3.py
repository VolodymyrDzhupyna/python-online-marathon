import re


def valid_email(email):
    try:
        if re.search(r"^([a-zA-Z0-9_\-\.]+)@([a-zA-Z0-9\-\.]+)\.([a-zA-Z]{2,3})$", email):
            return "Email is valid"
        else:
            raise Exception("Email is not valid")
    except Exception as e:
        return e


print(valid_email("trafik@ukr_tel.com"))
print(valid_email("trafik@ukr.tel.com"))
print(valid_email("tra@fik@ukr.com"))
print(valid_email("example@source.ua"))
print(valid_email("example@source_arth.com"))