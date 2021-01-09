username=input("enter username with minimum 3 characters")

if len(username)<3:
    print("username is shorter than 3 characters")
else:
    msg="Hello <<UserName>>, How are you?"
    print(msg.replace("<<UserName>>", username))