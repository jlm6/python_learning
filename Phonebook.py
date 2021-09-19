#Create a phonebox dictionary where user can input the data and check the dictionary
from prettytable import PrettyTable

phonebook_dict = {}
check_flag = True


def showphonebook():
    x = PrettyTable()
    x.field_names = ["Contact", "Phone_Number"]
    for item in phonebook_dict:
        #format x.add_row ( ["Adelaide", 1295, 1158259, 600.5] )
        x.add_row( [item, phonebook_dict[item]] )
    print(x)

def checkduplicate(phonebook_dict, username, phone_number):
    if username in phonebook_dict:
        reply = input (
            f"We found out there is another record naming {username}, do you want to update the phone number (U) \n"
            f"or Enter a new contact name? (N) " )
        if reply.lower () == 'u':
            phonebook_dict[username] = phone_number
        elif reply.lower () == 'n':
            no_add = 1
            return no_add


def getuserinput():
    try:
        username = str(input ( "What is the name of the new contact? " ))
        phone_number = int ( input ( f"What is {username}'s phone number? " ) )

    except ValueError:
        phone_number = int ( input ( f"What is {username}'s phone number again? you seem to type an invalid data.  " ) )
    if checkduplicate ( phonebook_dict, username, phone_number ) == 1:
        getuserinput()
    else:
        phonebook_dict[username] = phone_number


while check_flag:
    getuserinput()
    response = input("Do you want to add more contact (A) or check the phonebook (C)? ")
    if response.lower() == 'c':
        print("Here is the latest phonebook list")
        showphonebook()
        response = input("Do you want to add more contact (A) or quit (Q)? ")
        if response.lower() == 'q':
            check_flag = False
    elif response.lower() != 'a' and response.lower() != 'q':
        print("Wrong input entry, Goodbye~")
        check_flag = False


