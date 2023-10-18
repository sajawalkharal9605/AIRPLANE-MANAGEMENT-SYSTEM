#sajawal_khan_assignement_1_airplane management system

flight_data = {}

def display_seat_layout(seat_layout):
    print('       A B C D E F')
    for i, row in enumerate(seat_layout, start=1):
        print(f'Row {i}: {" ".join(row)}')

def book_a_seat(airline):
    print()
    display_seat_layout(flight_data[airline]['seat_layout'])
    row = int(input('Enter Row number from (1-5): '))
    if 1 <= row <= 5:
        column = input('Enter Seat Column (A-F): ').upper()
        if column in 'ABCDEF' and flight_data[airline]['seat_layout'][row - 1][ord(column) - ord('A')] == '*':
            flight_data[airline]['seat_layout'][row - 1][ord(column) - ord('A')] = 'X'
            passenger_name = input('Enter your name: ')
            with open('flightdetail.txt', 'a') as f:
                f.write(f'{passenger_name} {airline} Row {row} Seat {column}\n')
            print('Seat of ',passenger_name,'booked successfully.')
            print('>>>>>>>>>>>>>>>>>>>>>>>>have a safe flight<<<<<<<<<<<<<<<<<<<<<<')
        else:
            print('Seat is already booked.')
    else:
        print('Invalid row number please select a row from number 1 to 5.')

def cancel_booking(airline):
    display_seat_layout(flight_data[airline]['seat_layout'])
    row = int(input('Enter Row number from (1-5): '))
    if 1 <= row <= 5:
        column = input('Enter Seat Column (A-F): ').upper()
        if column in 'ABCDEF' and flight_data[airline]['seat_layout'][row - 1][ord(column) - ord('A')] == 'X':
            flight_data[airline]['seat_layout'][row - 1][ord(column) - ord('A')] = '*'
            print(f'Booking for Row {row} Seat {column} canceled.')
        else:
            print('Seat is already not booked .')
    else:
        print('Invalid row number.')

def save_flight_data(filename, data):
    with open(filename, 'w') as f:
        for airline, details in data.items():
            f.write(f'Airline: {airline}\n')
            f.write(f'Departure Time: {details["Departure"]}\n')
            f.write(f'Arrival Time: {details["Arrival"]}\n')
            
            f.write('--------------------------------------------------\n')

def show_flight_details():
    for airline, details in flight_data.items():
        print('-------------------------------------------------')
        print(f'Airline: {airline}')
        print(f'Departure Time: {details["Departure"]}')
        print(f'Arrival Time: {details["Arrival"]}')
        #display_seat_layout(seat_layout)
        print('--------------------------------------------------')

def add_flight():
    airline = input('Enter Airline Name: ')
    departure = input('Enter Departure Time: ')
    arrival = input('Enter Arrival Time: ')
    flight_data[airline] = {'Departure': departure, 'Arrival': arrival, 'seat_layout': [['*' for _ in range(6)] for _ in range(5)]}
    print('Flight added successfully.')

def remove_flight():
    airline = input('Enter Airline Name to Remove: ')
    if airline in flight_data:
        del flight_data[airline]
        print(f'Flight {airline} removed successfully.')
    else:
        print('Airline not found.')

def modify_flight():
    airline = input('Enter Airline Name to Modify: ')
    if airline in flight_data:
        departure = input('Enter New Departure Time: ')
        arrival = input('Enter New Arrival Time: ')
        flight_data[airline]['Departure'] = departure
        flight_data[airline]['Arrival'] = arrival
        print(f'Flight {airline} modified successfully.')
    else:
        print('Airline not found.')

def admin_interface():
    while True:
        print("------------------welcome admin---------------------")
        print()
        print("   1.  add a flights")
        print("   2.  remove a flight")
        print("   3.  modify a flight")
        print("   4.  display flights")
        print("   5.  Save and Exit")
        print()
        choice = input('Enter a number from 1 to 5: ')
        if choice == '1':
            add_flight()
        elif choice == '2':
            remove_flight()
        elif choice == '3':
            modify_flight()
        elif choice == '4':
            show_flight_details()
        elif choice == '5':
            save_flight_data('flightdetail.txt', flight_data)
            print('Flight data saved.')
            break
        else:
            print('Invalid choice. Please choose again.')
            admin_interface()
def user_menu():
    while True:
        print(">>>>>>>>>>>>>>>>>>>>>>welcome user<<<<<<<<<<<<<<<<<<<<<<")
        print("------------------------------------------------------------------")
        print("   1. to book a ticket")
        print("   2. to cancel a booking")
        print("   3. to show flight details")
        print("   4. to go back")
        print()
        choice=input("select an option")
        
        if choice == '1':
            print("welcome to ticket booking menu")
            print()
            airline = input('Enter Airline Name that you want to book: ')
            if airline in flight_data:
                book_a_seat(airline)
            else:
                print('Airline not found in our data.')
        elif choice == '2':
            print("welcome to booking canceling function")
            print()
            airline = input('Enter Airline Name from which you want to cancel the booking: ')
            print()
            if airline in flight_data:
                cancel_booking(airline)
            else:
                print('Airline not found.')
        elif choice == '3':
            show_flight_details()
        elif choice == '4':
            break
        else:
            print('Invalid choice. Please choose again.')
            user_menu()

def user_login():
    print("------------------------------------------------------------")
    print("welcome to user console")
    print()
    user=input("enter user name")
    print()
    password1=input("enter password")
    if user==("user") and password1==("user123"):
        user_menu()
    else:
        print("error!wrong username or password, tryagain")
        useradminlogin()


def admin_login():
    print("----------------------------------------------------")
    print("welcome to admin console")
    print()
    user=input("enter the admin name:")
    print()
    password2=input("enter the password:")
    if user==("admin") and password2==("admin123"):
        admin_interface()
    else:
        print("wrong password tryagain")
        




def useradminlogin():
    while True:
        print("NAME: SAJAWAL KHAN<<<<<>>>>>>'261942102'")
        print()
        print(">>>>>>>>>welcome to our flight registration system<<<<<<<<<<<")
        print()    
        print("press 1 for user login")
        print()
        print("press 2 for admin login"  )
        print()
        print("press 3 To  Exit this system ")
        print()
        choice = input(' select an option : ')
        if choice == '1':
            user_login()
        elif choice == '2':
            admin_login()
        elif choice == '3':
            print('Good bye from sajawal flight managing system')
            break
        else:
            print('Invalid choice. Please choose again.')
            useradminlogin()
            

useradminlogin()    


#work cited



#enumerate method taken from geek for geek plus the concept of ord










