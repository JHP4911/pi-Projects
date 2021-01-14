'''
Your task is to write a python script that can fetch the username and domain name from the email.
'''
# Get the user's email address
email = input("What is your email address?: ").strip()
# Slice out the user name
user_name = email[:email.index("@")]
# Slice out the domain name
domain_name = email[email.index("@")+1:]
# Format message
res = f"Your username is '{user_name}' and your domain name is '{domain_name}'"
# Display the result message
print(res)