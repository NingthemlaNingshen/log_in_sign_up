import json,os
l = []
def signup():
    global name
    name=input("enter your username: ")
    password1=input("enter your password: ")
    # if len(password1)>=6 and "!" or "@" or "#" or "$" or "%" or "^" or "&" or "*" or "-" or "_" and int and upper 
    if len(password1)>=6 and "!" or "@" or "#" or "$" or "%" or "^" or "&" or"*"or"-"or"_" in password1:
        password2=input("re-enter your password: ")
        if password1==password2:
            if (os.path.isfile("Nim.json")):
                f=open("Nim.json","r")
                a=json.load(f)
                for i in a["User"]:
                    if i["Name"]==name:
                        print("This user already exist")
                        break
                else:
                    d1={}
                    d2={}
                    d1["Name"]=name
                    d1["Password"] = password1
                    d2["Description"]=input("Introduce yourself: ")    
                    d2["D.O.B"]=input("Enter your Date of Birth: " )
                    d2["Gender"]=input("Enter your sex: ")  
                    d2["Hobbies"]=input("enter your Hobbies: ")  
                    d1["Profile"]=d2
                    x=a["User"]
                    x.append(d1)
                    f1=open("Nim.json","w+")
                    json.dump(a, f1,indent=4)
                    f1.close()
                    print("sign_up succesful")
            else:
                    dic,l,d,d1={},[],{},{}
                    dic["Name"]=name
                    dic["Password"]=password1
                    d["Description"]=input("Introduce yourself: ")
                    d["D.O.B"]=input("Enter your Date of Birth: ")
                    d["Gender"]=input("Enter your sex: ")
                    d["Hobbies"]=input("enter your Hobbies:  ")
                    dic["Profile"]=d
                    l.append(dic)
                    d1["User"]=l
                    f2=open("Nim.json","w+")
                    json.dump(d1,f2 ,indent=4)
                    f2.close()
                    print("Signup Succesful")
        else:
            print("you have enter a wrong password")
    else:
            print("your password is to weak enter some special charecter or numeric number")                    
def login():
    if user=="log_in":
        c=0
        a=open("Nim.json","r")
        f=json.load(a)
        user_name=input("Enter your user_name for login : ")
        user_password=input("Enter your password for login : ")
        for j in f["User"]:
            if j["Name"]==user_name:
                if user_name==j['Name']:
                    if user_password==j['Password']:
                        print("Login successful")
                        print("PERSONAL RECORD")
                        print(user_name.capitalize(),"You Logged In Succesfully")
                        print("Username",":",j["Name"])
                        print("Gender",":",j["Profile"]["Gender"])
                        print("Bio",":",j["Profile"]["Description"])
                        print("Dob",":",j["Profile"]["D.O.B"])
                        print("Hobby",":",j["Profile"]["Hobbies"])
                        break
                    else:
                        print("Check your password")
                else:
                        print("Check your username")
def main():
    global user
    user=input("enter whether you want to log_in or sign_up:  ")
    if user=="sign_up":
        signup()
    elif user=="log_in":
        login()
    else:
        print("Your enter worng input ")
        print("before entering anything you can check first ")
main()
