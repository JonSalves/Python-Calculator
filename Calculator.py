import Addition,Subtraction,multiply,Division,Square,Squareroot

def read_file():
    try:
        with open("CalcMenu.txt") as file_read:
            fr = file_read.read()
            return fr
    except FileNotFoundError as fnf:
        print(f"Error handling file because {fnf}")

def caclOP():
    option = 0

    options_list = ["1", "2", "3", "4", "5", "6", "7"]
    
    menu_choices = read_file()

    while option not in options_list:

        print(menu_choices)

        option = input("Choose and option: ")

        if option not in options_list:
            print("Please enter a valing number")

    return option

main_Program = True

while main_Program:
    main_menu = caclOP()

    match main_menu:
        case "1":
            Addition.addition()

        case "2":
            Subtraction.subtraction()

        case "3":
            multiply.multiply()

        case "4":
            Division.divide()

        case "5": 
            Square.square()

        case "6":
            Squareroot.sqrroot()
        case _:
            # re-assign the  main_Program variable to False
            main_Program = False

input("Press 'Enter' to EXIT the Menu/App")