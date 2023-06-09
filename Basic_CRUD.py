import os
from tabulate import tabulate

students = []

def os_clear():
    system_operation = os.name
    if system_operation ==  'nt':
        os.name == os.system('cls')
    else:
        os.name == os.system('clear')

def main_menu():
    os_clear()
    while(True):
        print("""
List Menu
-----------------------------
1. Create Data
2. Read Data
3. Update Data
4. Delete Data
5. Exit Program
-----------------------------""")
        try:
            select_menu = int(input("Please Select Menu : "))
            if select_menu == 1:
                create_data()
                break
            elif select_menu == 2:
                read_data()
                break
            elif select_menu == 3:
                update_data()
                break
            elif select_menu == 4:
                delete_data()
                break
            elif select_menu == 5:
                exit = input("Do You Want To Exit Program ? (Y/N) : ")
                if exit == "Y" or exit == "y":
                    print("Exit Program Success!")
                    break
                else:
                    main_menu()
                    break
            else:
                print("Menu Not Found!")
        except ValueError as E:
            print(E)
 
def read_data():
    while (True):
        print("""
Menu Read Data
-----------------------------
1. Show All Data
2. Search Data
3. Back to Main Menu
-----------------------------""")
        try:
            select_read = int(input("Please Select Menu : "))
            if select_read == 1:
                if len(students) == 0:
                    print("Data Empty!")
                else:
                    print(tabulate(students,headers="keys",tablefmt='grid'))
            elif select_read == 2:
                if len(students) == 0:
                    print("Data Empty!")
                else:
                    select_id = input("Select ID : ").upper()
                    check_id = list(map(lambda data:data['ID'],students))
                    if select_id not in check_id:
                        print("Data Not Found!")
                    else:
                        search_data(select_id)
                        print(tabulate(search_data(select_id),headers="keys",tablefmt='grid'))
            elif select_read == 3:
                main_menu()
                break
            else:
                print("Menu Not Found!")
        except ValueError as E:
            print(E)

def search_data(select_id):
    output = list(filter(lambda data:data['ID'] in str(select_id),students))
    return output
        
def create_data():
    while (True):
        print("""
Menu Create Data
-----------------------------
1. Create Data
2. Back to Main Menu
-----------------------------""")
        try:
            select_menu = int(input("Please Select Menu : "))
            if select_menu == 1:
                create_id = input("Input ID : ").upper()
                check_id = list(map(lambda data:data['ID'],students))
                if create_id in check_id:
                    print("ID Already Exists")
                else:
                    create_name = input("Input Name : ").capitalize()
                    create_score = int(input("Input Score : "))
                    if create_score >= 80 :
                        create_status = 'Pass'
                    else:
                        create_status = 'Not Pass'
                    save = input("Do You Want To Save It ? (Y/N) : ")
                    if save == "Y" or save == "y" or save == "yes":
                        new_data = []
                        new_data.append({
                                'ID' : create_id,
                                'Name' : create_name,
                                'Score' : create_score,
                                'Status' : create_status, 
                            })
                        students.extend(new_data)
                        new_data.clear()
                        print("Create Data Success!")
                        print(tabulate(students,headers="keys",tablefmt='grid'))
                    else:
                        print("Create Data Canceled!")
            elif select_menu == 2:
                main_menu()
                break
            else:
                print("Menu Not Found!")
        except ValueError as E:
            print(E)

def update_data():
    while (True):
        print("""
Menu Update Data
-----------------------------
1. Update Data
2. Back to Main Menu
-----------------------------""")   
        try:
            select_menu = int(input("Please Select Menu : "))
            if select_menu == 1:
                print(tabulate(students,headers="keys",tablefmt='grid'))
                select_id = input("Select ID : ").upper()
                check_id = list(map(lambda data:data['ID'],students))
                if select_id in check_id:
                    select_column = input("Select Columns : ")
                    if select_column == 'ID' or select_column == 'Name':
                        new_value = input("Input New Value : ").capitalize()
                        save = input("Do You Want To Save It ? (Y/N) : ")
                        if save == "Y" or save == "y" or save == 'yes':
                            search_data(select_id)[0][select_column] = new_value
                            print("Update Data Success!")
                        else:
                            print("Update Data Canceled!")
                    elif select_column == 'Score':
                        new_value = int(input("Input New Score : "))
                        save = input("Do You Want To Save It ? (Y/N) : ")
                        if save == "Y" or save == "y" or save == 'yes':
                            search_data(select_id)[0][select_column] = new_value
                            print("Update Data Success!")
                        else:
                            print("Update Data Canceled!")
                        if search_data(select_id)[0]['Score'] >= 80:
                           search_data(select_id)[0]['Status'] = 'Pass'
                        else:
                            search_data(select_id)[0]['Status'] = 'Not Pass'
                    elif select_column == 'Status':
                        print("Column Automatically Updated By Score")
                    else:
                        print("Column Not Found")  
                else:
                    print("Data Not Found!")
            elif select_menu == 2:
                main_menu()
                break
            else:
                print("Menu Not Found!")              
        except ValueError as E:
            print(E)

def delete_data():
    while (True):
        print("""
Menu Delete Data
-----------------------------
1. Delete Data
2. Back to Main Menu
-----------------------------""")
        try:
            select_menu = int(input("Please Select Menu : "))
            if select_menu == 1:
                if len(students) == 0:
                    print("Data Empty!")
                else:
                    print(tabulate(students,headers="keys",tablefmt='grid'))
                    select_id = input("Select ID : ").upper()
                    check_id = list(map(lambda data:data['ID'],students))
                    if select_id in check_id:
                        data = search_data(select_id)
                        for a,val in enumerate(students):
                            if students[a] == data[0]:
                                delete = input("Do You Want To Delete This Data ? (Y/N) : ")
                                if delete == "Y" or delete == "y":
                                    del students[a]
                                    print("Delete Data Success!")
                                else:
                                    print("Delete Data Canceled!")
                    else:
                        print("Data Not Found!")
            elif select_menu == 2:
                main_menu()
                break
            else:
                print("Menu Not Found!")
        except ValueError as E:
            print(E)                                 
             
while(True):
    main_menu()
    break



