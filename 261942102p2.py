#sajawal_khan_assignement_1_airplane management system


flist=[["sajawalair","9:00","5:00"],["turkishairline","5:00","3:00"]]



sajawalseat = [['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ]]

def sajawalairseat() :
    print('seat layout of sajawalairlnes')
    print('           A    B    C    D    E   F')                  
    for i in range(len(sajawalseat)):
        print('Row ',i+1,'.',sajawalseat[i])

        
turkishseat = [['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ],['*' ,'*' ,'*' ,'*' ,'*' ,'*'  ]]

def turkishairseat() :
    print('seat layout of turkishair')
    print('           A    B    C    D    E   F')                  
    for i in range(len(turkishseat)):
        print('Row ',i+1,'.',turkishseat[i])    
    print("--------------------------------------------------------")
#to select seat column i am creating a new functon to incline it with the rows 
def column_handle(i):
    if i in 'aA':
        return 1
    elif i in 'bB':
        return 2 
    elif i in 'Cc':
        return 3
    elif i in 'Dd':                                         
        return 4
    elif i in 'eE':
        return 5
    elif i in 'fF':
        return 6 
   
def booking_a_ticket():
    print("--------------------------------------------------------")
    print("1 .for sajawalairlines")
    print("2 .for turkishairlines")
    print("--------------------------------------------------------")
    inputbook=int(input("choose a airline"))
    if inputbook == 1:
        sajawalairseat()
        row = input('Enter Row(number)?: ')
        if row not in '12345':
            print('Incorrect Row')
            
        print("--------------------------------------------------------")
        column = input('Enter Seat Alphabet: ')
        if column not in 'abcdefABCDEF':
            print('Invalid SeatNO')
          
        o =sajawalseat[((int(row))-1)]

        if o[column_handle(column)-1] == 'X':
            print(' no availabilty')
            

        o[column_handle(column)-1] = 'X'
        m_name = input('Enter your name: ')

           
        f = open('flightdetail.txt','a')
        f.write(m_name)
        f.write(' SAJAWAL AIRLINES ')                    
        f.write(  row)                                             
        f.write(column)
        f.write('\n')
        f.close()
        print("--------------------------------------------------------")
        print("your seat booked successfully")
        print("--------------------------------------------------------")
        print("your details")
        print("your name        :",m_name)
        print("your row number  :",row)
        print("your seat number :",column)
        
        user_interface()            
          
    elif inputbook == 2:
        turkishairseat()
        row = input('Enter Row(numbers)?: ')
        if row not in '12345':
            print('Incorrect Rows')
            
        print("--------------------------------------------------------")
        column = input('Enter Seat Alphabet: ')
        if column not in 'abcdefABCDEF':
            print('Invalid SeatNO')
        
        o = turkishseat[((int(row))-1)]

        if o[column_handle(column)-1] == 'X':
            
            print(' not available')
            

        o[column_handle(column)-1] = 'X'
        M_name = input('Enter your name: ')

        
        f = open('flightdetail.txt','a')
        f.write(M_name)
        f.write(' TURKISH AIRLINE ')               
        f.write(row)
        f.write(column)
        f.write('\n')
        f.close()
        print("--------------------------------------------------------")
        print("seat booked successfully")
        print("--------------------------------------------------------")
        print("your details")
        print("your name        :",M_name)
        print("your row number  :",row)
        print("your seat number :",column)
        
        user_interface()


        
    else:
        print('Enter a valid input')
    
        
        
def cancel_booking():
    print("welcome to our cancel booking page")
    print("FROM WHICH FLIGHT YOU WANT TO CANCEL")
    print("press 1 for SAJAWAL AIRLINES")
    print("press 2 for TURKISH AIRLINES")
    print("press any other to go back")
        
    cancel_input=int(input("enter a number"))

    if cancel_input== 1:
        
        sajawalairseat()
        row = input('Enter Row(number)?: ')
        if row not in '12345':
            print('Incorrect Row')
            
        
        column = input('Enter Seat Alphabet: ')
        if column not in 'abcdefABCDEF':
            print('Invalid SeatNO')
        
        o = sajawalseat[((int(row))-1)]

        if o[column_handle(column)-1] == 'X':
            o[column_handle(column)-1] = '*'
            
            print("--------------------------------------------------------------")
            print("from row ",row," and seat number", column , "your booking cancelled")
            print("--------------------------------------------------------------")

            user_interface()
        else:
            print('that seat is empty')
            user_interface()
        
        

    elif cancel_input==2:
        
        turkishairseat()
        row = input('Enter Row(number)?: ')
        if row not in '12345':
            print('Incorrect Row')
            
        print("--------------------------------------------------------")
        column = input('Enter Seat Alphabet: ')
        if column not in 'abcdefABCDEF':
            print('Invalid SeatNO')

        o = turkishseat[((int(row))-1)]

        if o[column_handle(column)-1] == 'X':
            o[column_handle(column)-1] = '*'
            print("--------------------------------------------------------------")
           
            print("from row ",row," and seat number", column , "your booking cancelled")
            print("-----------------------------------------------------------------")
            
            user_interface()
        else:
            print('seat isnt booked')
            user_interface() 

    else:
        user_interface()
                
    


            
    
    




def user_interface():
    
    print("welcome user")
    print("------------------------------------------------------------------")
    print("   1. to book a ticket")
    print("   2. to cancel a booking")
    print("   3. to show flight details")
    print("   4. to go back")

    select2=int(input("Enter one of the corrosponding number"))
                
    if select2 == 1:
                
        booking_a_ticket()
    elif select2==2:
        cancel_booking()
    elif select2==3:
        
        def show_flight_details():
            for i in flist:
                print('NAME of airline: ',i[0])
                print('Departure  time: ',i[1])
                print('Arrival at the airport: ',i[2])
                print("-----------------------------------------------------")
            sajawalairseat()

            print()
            print("--------------------------------------------------------")
            print()

            turkishairseat()
        
        show_flight_details()
        user_interface()
    elif select2==4:
        useradminlogin()
        
    else:
        print("you clicked the wrong button")
        user_interface()

        
        


def user_login():
    print("welcome to user console")
    user=input("enter user name")
    password1=input("enter password")
    if user==("user") and password1==("user123"):
        user_interface()
    else:
        print("error!wrong username or password, tryagain")
        useradminlogin()

def generalseat() :
    seat_layout=[['*'for _ in range(6)]for _ in range(5)]
    
    print('seat layout')
    print('           A    B    C    D    E   F')                  
    for i in range(len(seat_layout)):
        print('Row ',i+1,'.',seat_layout[i])    

    print()







def load_flight_data(airport):
    
    flight_data = {}
    try:
        
        with open(airport, 'r') as file:
            current_flight = {}
            for line in file:
                line = line.strip()
                if line:
                    key, value = line.split(': ')
                    current_flight[key] = value
                else:
                    if current_flight:
                        flight_data[current_flight['Name']] = current_flight
                        current_flight = {}
    except FileNotFoundError:
        print("Flight data file not found.")
    return flight_data



def save_flight_data(airport, flight_data):
    with open(airport, 'w') as file:
        for flight in flight_data.values():
            for key, value in flight.items():
                file.write(f"{key}: {value}\n")
            file.write("\n")



def adding_flight(flight_data):
    
    name = input("Enter Flight name: ")
    departure = input("Enter departure time: ")
    arrival = input("Enter arrival time: ")
    new_flight = {'Name': name, 'Departure': departure, 'Arrival': arrival}
    flight_data[name] = new_flight
    print("--------------------------------------------------------")
    print("New Flight added successfully.")

    
    admin_interface()
    
def remove_a_flight(flight_data):
    name_to_remove = input("Enter the name of the flight to remove: ")
    print("----------------------------------------------------------")
    if name_to_remove in flight_data:
        del flight_data[name_to_remove]
        print("----------------------------------------------------------")
        print("Flight removed successfully.")
    else:
        print("Flight not found.")

    

    
    admin_interface() 
def modifying_a_flight(flight_data):
    name_to_modify = input("Enter the name of the flight to modify: ")
    if name_to_modify in flight_data:
        flight = flight_data[name_to_modify]
        flight['Name'] = input("Enter new Flight name: ")
        flight['Departure'] = input("Enter new departure time: ")
        flight['Arrival'] = input("Enter new arrival time: ")
        print("Flight data modified successfully.")
    else:
        print("Flight not found.")

    
    admin_interface() 
def display_flights(flight_data):
    
    for i in flist:
        
        print('NAME: ',i[0])
        print('Departure: ',i[1])
        print('Arrival: ',i[2])
        print("------------------------------------")
        generalseat()
    if not flight_data:
        print("No other flight data available.")
    else:
        for name, flight in flight_data.items():
            print(f"Flight Name: {name}")
            generalseat()
            for key, value in flight.items():
                print(f"{key}: {value}")
                
            print() 
            print()
    admin_interface()    

airport= "airport_detail.txt"
flight_data= load_flight_data(airport)




def admin_interface():
    
    
    
    
    
    print("------------------welcome admin---------------------")
    print()
    print("   1.  add a flights")
    print("   2.  remove a flight")
    print("   3.  modify a flight")
    print("   4.  display flights")
    
    print("   5.  save and go back to main menu")
    
    
    select3=int(input("Enter one of the corrosponding number:"))
    if select3==1:
        adding_flight(flight_data)
    elif select3==2:
        remove_a_flight(flight_data)
    elif select3==3:
        modifying_a_flight(flight_data)
    elif select3==4:
        display_flights(flight_data)
    elif select3==5:
        save_flight_data(airport, flight_data)
        useradminlogin()
    else:
        print("choose the correct option")
        admin_interface()
        


    
def admin_login():
    print("welcome to admin console")
    user=input("enter admin name:")
    password2=input("enter password:")
    if user==("admin") and password2==("admin123"):
        admin_interface()
    else:
        print("wrong password tryagain")
        
                                                                                                                                                                                    

    
    
def useradminlogin():
    print("NAME: SAJAWAL KHAN<<<<<>>>>>>'261942102'")
    print()
    print(">>>>>>>>>welcome to our flight registration system<<<<<<<<<<<")
    print()
    print("press 1 for user login")
    print()
    print("press 2 for admin login")
    print()
    print("press 3 to close the console")
    print()
    
    select1=int(input("please enter a number:"))
        
    

    if select1==1:
            
        user_login()
    elif select1==2:
            
        admin_login()
            
    elif select1==3:
            
        useradminlogin()
            
            
    else:
        
        print("you pressed invalid button")
        useradminlogin()
                    
useradminlogin()                    
