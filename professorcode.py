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


storageURL= "http://130.65.159.227:8080/v1/AUTH_c69217d717bb40988d42d4dfc4da6bdf"
token= "gAAAAABaLNpyI5SDmw0DMxm_CK-mkbDHgz4_L0MDQWZHC5hLGhxWA7lQcjtmj6r03T55OWiD6O18rjBwFaE3fawmgyJXVNudtW4RlVUjRpNSklgi8Aov1viVwet24wFzAxpkqq-ZMpf8Rj78vUK-54xAW1VnPfS-qI5vImlxmUQUm9-mYc6DNok"
Account= "AUTH_c69217d717bb40988d42d4dfc4da6bdf"


path = "/home/user/Desktop"

# All accounts
users = {
    "admin": {
        "password": "profesor",
        "group": "admin",
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


##############

    

def openstac(username, password):
    username = username
    password = password
    ######1########
    def create_container():
        while True:
            container_name2 = input("Enter Student name to create: ")
            os.system('curl -i $storageURL/'+container_name2+' -X PUT -H "Content-Length: 0" -H "X-Auth-Token: $token"')
            print("Student container created:"+container_name2)
        

    #####2#########
    def delete_container():
        container_name2 = input("Enter Student name to delete: ")
        os.system('curl -i $storageURL/'+container_name2+'-X DELETE -H "Content-Length: 0" -H "X-Auth-Token: $token"')
        print("Student container deleted:"+container_name2)

    
    ########3#########

                
    def list_students():
        container_name3 = raw_input("Enter container name: ")

        command3 = 'http://130.65.159.227:8080/v1/AUTH_c69217d717bb40988d42d4dfc4da6bdf/'

        output3 = os.system("curl "+command3)

        print (output3)

    

    ########4#########
    def create_subjects():
        container_name4 = input("Enter Student name: ")
        subject_name4 = input("Enter Subject name:")
        os.system('curl -i $storageURL/'+container_name4+'/'+subject_name4+'-X PUT -H "Content-Length: 0" -H "X-Auth-Token: $token"')
        print("Subject folder created:"+subject_name4)


    ########5#########

    def upload_files():
        # Ask the user for input
        container_name2 = raw_input("Enter container name: ")
        filename_name2 = raw_input("Enter file name to upload: ")

        # Set up the echo command and direct the output to a pipe
        output2 = os.system("swift upload "+container_name2+ " "+filename_name2)
        # Run the command

        print (output2)

        print ("File uploaded successfully!!!")
        
   
    #######6#######
        
    def delete_files():
        # Ask the user for input
        container_name6 = raw_input("Enter Student name: ")
        subject_name6 = raw_input("Enter Subject name: ")
        file_name6 = raw_input("Enter file name to delete: ")
        output6 = os.system('curl -i $storageURL/'+container_name6+'/'+'/'+subject_name6+'/'+file_name6 +' -X DELETE -H "Content-Length: 0" -H "X-Auth-Token: $token"')
        print (output6)
        print ("Subject deleted!!!")

    #######7#######
        
    def delete_subjects():
        # Ask the user for input
        container_name7 = raw_input("Enter Student name: ")
        subject_name7 = raw_input("Enter Subject name: ")
        output7 = os.system('curl -i $storageURL/'+container_name7+'/'+'/'+subject_name7+'/'+' -X DELETE -H "Content-Length: 0" -H "X-Auth-Token: $token"')
        print (output7)
        print ("Subject deleted!!!")
        
    #######8#######
        
    def download_files():
        # Ask the user for input
        container_name8 = raw_input("Enter Student name: ")
        subject_name8 = raw_input("Enter Subject name: ")
        file_name8 = raw_input("Enter file name to download: ")
        output8 = os.system('curl -X GET -i "X-Auth-Token: $token" http://130.65.159.227:8080/v1/'+Account+'/'+container_name8+'/'+subject_name8+'/'+file_name8 +'--insecure')
        print (output8)
        print (os.system('echo '+str(output8)+'> '+str(file_name8)))
        print ("File downloaded!!!")

        
    while (True):
        print ("****************Menu********************")
        print ("Enter 1 for create container(students)")
        print ("Enter 2 to delete container")
        print ("Enter 3 to list students")
        print ("Enter 4 to create subjects for students")
        print ("Enter 5 to upload files to subject")
        print ("Enter 6 to delete files from subjects")
        print ("Enter 7 to delete subjects")
        print ("Enter 8 to download files from subjects")
        number = input();
        if number == 1:
            create_container()
            print
            print
        elif number == 2:
            delete_container()
            print
            print
        elif number == 3:
            list_students()
            print
            print
        elif number == 4:
            create_subjects()
            print
            print
        elif number == 5:
            upload_files()
            print
            print

        elif number == 6:
            delete_files()
            print
            print
        elif number == 7:
            delete_subjects()
            print
            print
        elif number == 8:
            download_files()
            print
            print
        else:
            exit()



   
while True:
    print ("****************Menu********************")
    print ("Enter 1 to login")
    print ("Enter 2 to exit")
    number = input();
    if number == 1:
        login()
        print
        print
    elif number == 2:
        exit()
    else:
        exit()

