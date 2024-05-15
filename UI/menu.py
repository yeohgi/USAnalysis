import functions

def menu():
  
  ch = 0

  print("\nWelcome to the name database!\n\nThis database is centered around names in the USA looking at them from both a national and state level.\n\nProvided are various functions to help manipulate and get a better understanding of the different names throughout the USA.\n\n")

  while ch != 7:

    print("Functions:\n")
    print("1. Display x amount of popular or unpopular names based on the year, location, and demographic\n")
    print("2. Display x amount of top names based on male to female ratio\n")
    print("3. Generate data for users choice of names according to their frequency in each year and visualize it on a graph\n")
    print("4. Generate data for a common names male and female frequency and visualizes it on a graph\n")
    print("5. Visualizes on a graph the rank of a name based on the location every year \n")
    print("6. Display similar name vairations with their corresponding score and total frequency\n")
    print("7. Exit\n")


    
    sCh = input("\nPlease input a number to select an option: ")

    if (sCh.isdigit() == True):
      ch = int(sCh)

    else:
      ch = 0
      print("Input is not an integer")

    if ch == 1:
      functions.popularNamesTwo()

    elif ch == 2:
      functions.nameMOrF()

    elif ch == 3:
      functions.compareNames()

    elif ch == 4:
      functions.graphCommonName()

    elif ch == 5:
      functions.graphRanks()

    elif(ch == 6):
      functions.similarNames()

    elif ch == 7:
      break

    else:
      print("Error! Entered value is not a valid selection please make a valid entry\n")

menu()


