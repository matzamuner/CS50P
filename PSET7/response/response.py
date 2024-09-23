from validator_collection import validators, errors

def main():
    if valid := validate(input("Email: ")):
        print("Valid")
    else:
        print("Invalid")

def validate(s):
    try:
        email_address = validators.email(s)
    except errors.EmptyValueError:
        return False
    except errors.InvalidEmailError:
        return False
    else:
        return True

if __name__ == "__main__":
    main()
