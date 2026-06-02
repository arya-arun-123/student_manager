# entry point to te applicaction

print('hi world')

def main() :
    # to collect and save student details
    students = []
    status = True
    while status:
        print('======MENU=======')
        print('1. Add Student')
        print('2. Add Scholarship Student')
        print('3. View all Student')
        print('4. Exit')

        user_choice = input("Enter your choice : ")

        if(user_choice == '1') :
            ## methods to add students
            print("Student added successfully")
        elif(user_choice == '2') :
            ## methods to add scholarship students
            print("Scholarship Student added successfully")
        elif(user_choice == '3') :
            ##display entries in 'students'
            print("************************")
        elif(user_choice == '4') :
            status = False
            break       # used to break a loop (for or while)
        else :
            print("Please select a valid choice")
            

    
# initialize python project

if __name__ == '__main__' :
    main()