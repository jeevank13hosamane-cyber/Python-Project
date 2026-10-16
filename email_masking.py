#in this the email address will be hidden
def mask_email(email):
    at=email.find("@")
    name=email[0:at]
    domain=email[at+1:]
    print(name[0]+"*"*(len(name)-2)+name[-1]+"@"+domain)

email=input("Enter your email: ")
mask_email(email)    
