#Group-1
#Project Partners -
#Dharmik Shah - 011413103 (29)
#Gargi Saraf - 011447865 (27)
#Vaidehee Barde - 011447267 (07)


# Import modules
import time
import requests,json
import subprocess
import os
import swiftclient

path = "/home/user/Desktop"
# All accounts
users = {
    "dharmik": {
        "password": "dharmik",
        "group": "dharmik",
        "mail": []
    },
    "gargi": {
        "password": "gargi",
        "group": "gargi",
        "mail": []
    },
    "vaidehee": {
        "password": "vaidehee",
        "group": "vaidehee",
        "mail": []
    }
}

# Form validation
def validate(form):
    if len(form) > 0:
        return False
    return True

# Login authorization
def loginauth(username, password):
    if username in users:
        if password == users[username]["password"]:
            print("Login successful")
            return True
    return False

# Login
def login():
    while True:
        username = input("Username: ")
        if not len(username) > 0:
            print("Username can't be blank")
        else:
            break
    while True:
        password = input("Password: ")
        if not len(password) > 0:
            print("Password can't be blank")
        else:
            break

    if loginauth(username, password):
        openstac(username, password)
    else:
        print("Invalid username or password")

# Register
def register():
    while True:
        username = input("New username: ")
        if not len(username) > 0:
            print("Username can't be blank")
            continue
        else:
            break
    while True:
        password = input("New password: ")
        if not len(password) > 0:
            print("Password can't be blank")
            continue
        else:
            break
    print("Creating account...")
    users[username] = {}
    users[username]["password"] = password
    users[username]["group"] = "user"
    users[username]["mail"] = []
    time.sleep(1)
    print("Account has been created")

##############

    

def openstac(username, password):

    ######1########
    username = username
    password = password
    def list_files(path):
        print ("********The file in the local directory are: ***********")
        i = 1
        for file in os.listdir(path):
            if not file.startswith('.') and os.path.isfile(os.path.join(path, file)):
                print (i,file)
                i = i+1

    #####2#########
                
    def upload_files():
        # Ask the user for input
        container_name2 = raw_input("Enter container name: ")
        filename_name2 = raw_input("Enter file name to upload: ")
        if continaer_name2 == username:
            # Set up the echo command and direct the output to a pipe
            output2 = os.system("swift upload "+container_name2+ " "+filename_name2)
            # Run the command

            print (output2)

            print ("File uploaded successfully!!!")

    ########3#########

    def list_uploaded_files():
        container_name3 = raw_input("Enter container name: ")

        command = 'http://130.65.159.227:8080/v1/AUTH_c69217d717bb40988d42d4dfc4da6bdf/'+container_name3
        if continaer_name2 == username:
            output3 = os.system("curl "+command)
            print (output3)
        
    ########4#########
            
    def delete_uploaded_files():
        # Ask the user for input     
        container_name4 = raw_input("Enter Student name:")
        subjects_name = raw_input("Enter Subject name from which you have to delete file:")
        if continaer_name2 == username:
            file_name4 = raw_input("Enter file name to delete: ")
            output4 = os.system("swift delete "+container_name4+' '+file_name4)
            print (output4)
            print ("File deleted!!!")
        

    ########5#########

    def container_files():
        # Ask the user for input
        container_name5 = raw_input("Enter container name: ")
        file_name5 = raw_input("Enter folder name: ")
        if continaer_name2 == username:
            output5 = os.system("swift delete "+container_name5+' '+file_name5)
            print (output5)
        
        
    #######6#######
        
    def download_files():
        # Ask the user for input
        container_name6 = raw_input("Enter container name: ")
        file_name6 = raw_input("Enter file name to download: ")
        if continaer_name2 == username:
            output6 = os.system("swift download "+container_name6+' '+file_name6)
            print (output6)
            print ("File downloaded!!!")

        
    while (True):
        print ("****************Menu********************")
        print ("Enter 1 for listing all files in the local directory")
        print ("Enter 2 to upload a specific file to the repository")
        print ("Enter 3 for Subjects list")
        print ("Enter 4 to delete a specific file from the repository")
        print ("Enter 5 for files in a subject")
        print ("Enter 6 to download a specific file from the repository")
        number = input();
        if number == 1:
            list_files(path)
            print
            print
        elif number == 2:
            upload_files()
            print
            print
        elif number == 3:
            list_uploaded_files()
            print
            print
        elif number == 4:
            delete_uploaded_files()
            print
            print
        elif number == 5:
            container_files()
            print
            print

        elif number == 6:
            download_files()
            print
            print
        else:
            exit()



   
while True:
    print ("****************Menu********************")
    print ("Enter 1 to login")
    print ("Enter 2 to register")
    number = input();
    if number == 1:
        login()
        print
        print
    elif number == 2:
        register()
        print
        print
    else:
        exit()

