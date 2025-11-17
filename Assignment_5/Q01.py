userid='admin'
passw='1234'
for i in range(1,4):
    username=input("enter the userid:")
    password=input("enter the passw:")
    if( username==userid and password==passw):
        print("login successfully.")
    else:
        print("wrong userid and password re-enter again.")
if(username!=userid or password!=passw):
    print("access denied")