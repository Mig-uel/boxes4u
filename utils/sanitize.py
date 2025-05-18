def check_registration(form):
    errors = []

    first_name = form["first_name"].strip()
    last_name = form["last_name"].strip()
    email = form["email"].strip()
    username = form["username"].strip()
    password = form["password"]
    confirm_password = form["confirm_password"]

    if not all([first_name, last_name, email, username, password, confirm_password]):
        errors.append("All fields are required")

    if password != confirm_password:
        errors.append("Passwords must match")

    if len(password) < 6:
        errors.append("Password must be greater than or equal to 6 characters")

    if len(username) < 3:
        errors.append("Username must be greater than or equal to 3 characters")

    if len(errors) > 0:
        raise Exception(errors)

    return {
        "email": email,
        "username": username,
        "password": password,
        "first_name": first_name,
        "last_name": last_name,
    }


def check_login(form):
    errors = []

    username = form["username"].strip()
    password = form["password"]

    if not all([username, password]):
        errors.append("All fields are required")

    if len(errors):
        raise Exception(errors)

    return {"username": username, "password": password}


def check_checkout_info(form):
    errors = []

    first_name = form.get("first_name")
    last_name = form.get("last_name")
    street = form.get("street")
    postal_code = form.get("postal_code")
    city = form.get("city")
    country = form.get("country")

    if not all([first_name, last_name, street, postal_code, city, country]):
        errors.append("All fields are required")

    if len(errors):
        raise Exception(errors)

    return {
        "first_name": first_name,
        "last_name": last_name,
        "street": street,
        "postal_code": postal_code,
        "city": city,
        "country": country,
    }
