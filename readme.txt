This readme provides documentation on the entire program.

LEGEND: 

  SECTION 1 SETUP

    -Libaries Used

    -Execution

  SECTION 2 FILE FORMATTERS

  SECTION 3 FUNCTIONS

  SECTION 4 MISC

    -Images & Graphs

    -Helper Functions

    -Archive Folder

  SECTION 5 User Input and Validating Input

  SECTION 6 Runtime Do-Nots

SECTION 1 SETUP:

  Step 1. Download USAnalysis.zip

  Step 2. Find USAnalysis on your machine and extract the contents into a single folder

  Step 3. Make sure the latest version fo python (python 3.10.8) is downloaded, if unable some functioning version pf python

  Step 4. Guarentee the following libraries are functional on your machine or IDE (this step will vary by system and IDE)

    -os

    -pandas

    -dask.dataframe

    -matplotlib.pyplot

    -sys

    -numpy

    -IPython.display

    -fuzzywuzzy

    Another way to view this information could be through packages (python3):

    -Flask Version 2.2.3

    -matplotlib Version 3.7.1

    -ipython Version 8.12.0

    -pandas Version 2.0.0

    -dask Version 2023.3.2

    -numpy Version 1.24.2

    -fuzzywuzzy Version 0.18.0

    -urllib3 Version 1.26.15

  Step 5. Open desired IDE and navigate to the UI directory in the terminal (Machine->Folder->UI)

  Step 6. Once inside UI type 'python menu.py' to run the program

SECTION 2 FILE FORMATTERS:

  USAnalysis contains 6 unique file formatters. All file formatters are build spefific to the folder structure and can be run using 'python "filename".py'

    1. n_USA & ss_USA: Takes unformatted National and State data from the /Unformatted Data/ directory and outputs to subfolders within the /FormattedData/ directory. Each text file is formatted as follows 'Name,Frequency,YOB'

    2. r_n_m_USA & r_n_f_USA: Takes male and female formatted National data from /FormattedData/ and adds ranks. Each formatter for male and female outputs one new file in the same directory. Each text file is formatted as follows 'Name,Frequency,YOB,Rank'

    3. cn_USA & cn_ss_USA: Takes male and female formatted National data from /FormattedData/ and outputs a text file with common names in the same directory. The file is formatted as follows 'YOB,Name,mFrequency,fFrequency,mForF'

  SECTION 3 FUNCTIONS:

  def menu():
    Per the function name this function acts as a menu. The function introduces the program with a brief welcome message, then uses  
    a while loop in the form of a number system prompting the user to enter a number that corresponds to a function (specific    
    functions talked about later). Input is then verefied twice once to ensure the input is in fact a positive integer than again to
    make sure the positive integer is one of the specified choices the menu provides (number 1 through 9) through a chain of if, 
    elif and else statements. Based off the input (at this point assuming valid) the function will run the corresponding function     
    then repeat the while loop or if the exit command (8) is entered terminate the program.

  def popularNamesTwo():
    This function is called upon a user input of 1 from the menu function. It will then accumulate user input (how many names to 
    output, find the least or most popular names, whether to use state(s) specific or national data and the range of years to be     
    looked at) from the given user input it will print out the x most / least popular names and their frequencies based on the 
    geographical region(s) entered for the time frame. Upon completion of the function the program will 
    return to the menu function.

  def nameMOrF():
    This function is called upon a user input of 2 from the menu function. It will then accumulate user input (how many names to 
    output, whether to find the common names between genders that are the most male or female dominant, whether to look at state(s)   
    or national data, and the year to be searched), then providing a list of x amount of common names (at least 1 male and 1 female 
    person have the name) in a given region by a given year that have either the highest ratio male:female or the lowest ratio 
    male:female(i.e. highest ratio female:male). Upon completion the function returns to the menu.
    
    *Note: If multiple states are to be entered the data is only considered if within the state itself the male and female version of 
    a name are found. Ex. If 2 states are given Arizona (AZ) and New York (NY) for some year and the name Terry is found in the       
    female and male data for Arizona those values will be taken into consideration where if in New york it is only found for one of
    male or female those values won't be taken into consideration as the name isn't common within the state. Upon completion the 
    function returns to the menu.

  def compareNames():
    This function is called upon a user input of 3 from the menu function. It will then accumulate user input (the different names to 
    compare (graph) - up to a maximum of 5 to prevent output from overcrowding, which group of names to look at male or female and
    whether to look at state(s) or national data), based on this for each name entered (again up to 5) 2 pieces of information will 
    be provided a line graph of frequency vs year (a seperate line for each name) (see Images and Graphs in section 4) and for each 
    name will provide each year and its corresponding frequency as well (textile form of graph). Upon completion the function returns 
    to the menu.

  def graphCommonName():
    This function is called upon a user input of 4 from the menu function. It will then accumulate user input (the name to 
    search for and what geographical region state(s) or national). Given the user input the function will provide 2 forms of output,
    first a graph of frequency vs year with 2 lines showing the disparities between people given the name as female and as males. The
    function also outputs the data for the name for each year - male frequency, female frequency and male to female ratio. Upon 
    completion the function returns to the menu.

  def graphRanks():
    This function is called upon a user input of 5 from the menu function. It will then accumulate user input (the name to 
    search for, what group male or female and what geographical region state(s) or national). The function than performs 2 outputs
    one in the form of a graph showing rank over time of the name searched for the specific region and gender, as well as a table of
    the names rank for the search specifications for each year. Upon completion the function returns to the menu.

  def similarNames():
    This function is called upon a user input of 6 from the menu function. It will then ask the user for a name to search. The
    function will only look at the national data over the course of the length of time (1880 - 2021) and based on the name any 
    additional name within a pre-set score of similarity will be displayed as well along with each names frequency, ultmately,
    printing a table of all names similar / different variations of the name and sort them based of similarity, then by frequency.
    Upon completion the function returns to the menu.

SECTION 4 MISC:

  IMAGES AND GRAPHS:

    Anytime a graph is made it will be output to the /Images/ directory within /UI/ as graph.png. Note that graph.png is always being overwritten. If you would like to permentantly save it you can rename the graph or move it to a different directory on your machine.

  HELPER FUNCTIONS:

    Helper functions are used in many of our functions.

    def printStateTable():

      This function prints the state table with long and short forms by using premade files in the /States/ directory.

    def validState(state)
  
      This function takes a long or short form of a state and return a 1 if the state is valid and 0 otherwise. This function uses stateslower.txt in the /States/ directory.

    def validNameNational(name, char): 

      This function takes two parameters, name and char, where name is a given name and char is an m or f to spefific which file of the national files needs to be read. It returns a 1 if the input is valid and 0 otherwise.

    def returnShortForm(state):

      This function takes a short or long form of a state and returns the states short form. This function uses stateslower.txt in the /States/ directory.

  ARCHIVE FOLDER:

    The /Archive/ directory is a folder for code we wanted to keep for good measure but is not used. This folder can be deleted manually by the user if they would like.

Section 5 User Input and Validating Input:

  Integer / number input: Number input is validated using the isdigit() function checking whether the input is in fact a digit.
  If so the input will be cast to an int and then using if statements making sure it is within the desired range. This is all done 
  through a while loop.

  Text input (non-integer): Similarily, a while loop is used to validate input. All input is tested with the lowercase letters through
  the variable name.lower. Then an if statement checks if the input is any of the valid / appropriate inputs (variable name in [""])
  

  SECTION 6 Runtime Do-Nots:

    Do Not unplug / shutdown computer or any chords connected to the computer or wifi system

    Do Not enter input when not prompted, i.e function is calculating output and there is a 1 to 2 second break in between the
    last input and output

    Do Not exit the program other than through option 7 (exit) in the menu

  

  


