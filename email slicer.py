# Take email addres from user
email = input("Enter your email address: ").strip()
print(email)
# Slice and store the email address
username = email[:email.index("@")]

#slice and ster the domain name
domain = email[email.index("@") +1:]

result= "Your username is {} \nYour domain name is {}\n".format(username,domain)

print(result)