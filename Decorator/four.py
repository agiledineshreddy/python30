def credentials(func):
    def inner(name):
        if name == "Modi":
            print("Modi is PM")
        else:
            func(name)

    return inner


@credentials
def security(name):
    print("Welcome to onboard")


security("Rahul")
security("Modi")
security("Sonia")
