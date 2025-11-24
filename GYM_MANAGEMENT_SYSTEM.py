class color:
    red = '\033[91m'
    blue = '\033[94m'
    green = '\033[92m'
    pink = '\033[95m'
    cyan = '\033[96m'
    yellow = '\033[93m'
    orange = '\033[38;5;208m'
    white = '\033[97m'
print(f"{color.red}                                ___________                 ")
print(f"{color.blue}                     _____      |         |      _____      ")
print(f"{color.green}                     |   |      |         |      |   |      ")
print(f"{color.pink}                _____|___|______|         |______|___|____  ")
print(f"{color.cyan}                |               |         |              |  ")
print(f"{color.yellow}                |               |_________|              |  ")
print(f"{color.orange}                |  _____   _____  _____  _____   _____   |  ")
print(f"{color.red}                |  |   |   |   |  |   |  |   |   |   |   |  ")
print(f"{color.blue}                |  |___|   |___|  |___|  |___|   |___|   |  ")
print(f"{color.green}                |                                        |  ")
print(f"{color.pink}                |              VIT BHOPAL GYM            |  ")
print(f"{color.cyan}                |    ___       ______________      ___   |  ")
print(f"{color.yellow}                |    |_|       |   _ || _   |      |_|   |  ")
print(f"{color.orange}                |______________|_____||_____|____________|  ")
print(f"""{color.red}
            *************************************************
            !!            GYM MANAGEMENT SYSTEM            !!
            *************************************************
    {color.white}""")
print(f"""{color.blue}
	                    TRAINER ID: pranav
	                    PASSWORD: 12345678
    {color.white}""")
q={}
t={"pranav":"12345678"}
def signup():
	username=input("ENTER YOUR USERNAME: ")
	if username in q:
		print("THIS USER EXISTS IN OUR DATABASE")
		return
	password=input("ENTER A STRONG PASSWORD: ")
	age=input("ENTER YOUR AGE: ")
	gender=input("ENTER YOUR GENDER: ")
	height=input("ENTER YOUR HEIGHT IN CM: ")
	q[username]={"password":password,"age":age,"gender":gender,"height":height}
	print(f"""{color.green}
            ******************************************************
            !!  CONGRATS, YOU ARE SIGNED UP FOR VIT BHOPAL GYM  !!
            ******************************************************
    {color.white}""")
def login():
	username=input("USERNAME: ")
	password=input("PASSWORD: ")
	if username in q and q[username]["password"]==password:
		print(f"""{color.pink}
            **************************************
            !!  YOU ARE SUCCESSFULLY LOGGED IN  !!
            **************************************
    {color.white}""")
		member_menu(username)
	else:
		print("INVALID RESPONSE")
def trainer_login():
	username=input("TRAINER ID: ")
	password=input("PASSWORD: ")
	if username in t and t[username]==password:
		print(f"""{color.pink}
            **************************************
            !!  YOU ARE SUCCESSFULLY LOGGED IN  !!
            **************************************
    {color.white}""")
		trainer_menu()
	else:
		print(f"""{color.yellow}
            ************************
            !!  INVALID RESPONSE  !!
            ************************
    {color.white}""")
def member_menu(u):
	while True:
		print("\n1.EDIT PROFILE\n2.LOGOUT\n3.EXIT THE PROGRAM")
		ch=input("CHOICE: ")
		if ch=="1":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			edit_profile(u)
		elif ch=="2":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			return
		elif ch=="3":
			print(f"""{color.red}
            *****************
            !!  THANK YOU  !!
            *****************
    {color.white}""")
			exit()
		else:
			print(f"""{color.yellow}
            ************************
            !!  INVALID RESPONSE  !!
            ************************
    {color.white}""")
def trainer_menu():
	while True:
		print("\n1.VIEW ALL MEMBERS\n2.SEARCH MEMBERS\n3.LOGOUT\n4.EXIT THE PROGRAM")
		ch=input("CHOICE: ")
		if ch=="1":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			view_all()
		elif ch=="2":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			search_member()
		elif ch=="3":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			return
		elif ch=="4":
			print(f"""{color.red}
            *****************
            !!  THANK YOU  !!
            *****************
    {color.white}""")
			exit()
		else:
			print(f"""{color.yellow}
            ************************
            !!  INVALID RESPONSE  !!
            ************************
    {color.white}""")
def view_profile(u):
	p=q[u]
	print("ENTER YOUR AGE: ",p["age"])
	print("ENTER YOUR GENDER: ",p["gender"])
	print("ENTER YOUR HEIGHT: ",p["height"])
def edit_profile(u):
	p=q[u]
	a=input("ENTER YOUR AGE: ")
	g=input("ENTER YOUR GENDER: ")
	h=input("ENTER YOUR HEIGHT: ")
	if a!="":p["age"]=a
	if g!="":p["gender"]=g
	if h!="":p["height"]=h
	print(f"""{color.cyan}
            *****************************************
            !!  YOUR DATA IS SUCCESSFULLY UPDATED  !!
            *****************************************
    {color.white}""")
def view_all():
	for u in q:
		print(u,q[u])
def search_member():
	name=input("PLEASE ENTER THE NAME: ")
	if name in q:
		print(q[name])
	else:
		print(f"""{color.yellow}
            *****************************
            !!  MEMBER DOES NOT EXIST  !!
            *****************************
    {color.white}""")
def main():
	while True:
		print("\n1.MEMBER SIGNUP\n2.MEMBER LOGIN\n3.TRAINER LOGIN\n4.EXIT THE PROGRAM")
		ch=input("CHOICE: ")
		if ch=="1":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			signup()
		elif ch=="2":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			login()
		elif ch=="3":
			print(f"""{color.yellow}
            ******************************************************
    {color.white}""")
			trainer_login()
		elif ch=="4":
			print(f"""{color.red}
            *****************
            !!  THANK YOU  !!
            *****************
    {color.white}""")
			exit()
		else:
			print(f"""{color.yellow}
            ************************
            !!  INVALID RESPONSE  !!
            ************************
    {color.white}""")
main()