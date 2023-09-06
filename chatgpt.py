email = input("Enter your Email: ")  # Example: g@g.in
k = 0
j = 0
d = 0

if len(email) >= 6:
    if email[0].isalpha():
        if "@" in email and email.count("@") == 1:
            if email[-4:] == ".com" or email[-3:] == ".in":
                for i in email:
                    if i.isspace():
                        k = 1
                        break
                    elif i.isalpha():
                        if i.isupper():
                            j = 1
                            break
                    elif i.isdigit():
                        continue
                    elif i == "_" or i == "." or i == "@":
                        continue
                    else:
                        d = 1
                        break

                if k == 1 or j == 1 or d == 1:
                    print("Wrong Email - Contains spaces or uppercase letters")
                else:
                    print("Valid Email")
            else:
                print("Wrong Email - Invalid domain")
        else:
            print("Wrong Email - Missing '@'")
    else:
        print("Wrong Email - First character should be an alphabet")
else:
    print("Wrong Email - Length should be at least 6 characters")
