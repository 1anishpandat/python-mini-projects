email = input("enter your email: ")
if len(email) >=5:
    if email[0].isalpha():
        if ("@" in email)  and (email.count("@") == 1):
            if (email.endswith(".com") or email.endswith(".in") ):
                for i in email:
                    if i == i.isspace():
                        print("wrong emial 5")
                    elif i.isalpha():
                        if i == i.upper():
                            print("wrong email 6")
                    elif i.isdigit() or i in ["_","@","."]:
                        continue
                    
                
            else:
                print("wrong email 4")
        else:
            print("wrong email 3")
    else:
        print("wrong email 2")
        
else:
    print("wrong email 1")
