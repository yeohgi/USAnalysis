import os

#TO RUN CODE: python /FileFormaters/n_USA2.py
#Decently quick time to finish

count = 1880

#Define paths for unformated data and formated data
grabData = "Unformatted Data/NATIONAL"
moveData = "FormattedData/NATIONAL"

#Open formated data files for writing in a speficied directory
with open(os.path.join(moveData, "fNamesUSANational.txt"), "w") as fNationalNames, \
open(os.path.join(moveData, "mNamesUSANational.txt"), "w") as mNationalNames:

  #Loop through data between 1880 and 2021
  while (count < 2022):
    #Loop through files in the grabData directory
    for filename in os.listdir(grabData):
      #Checks if the data being read is valid // checks for garbage
      if filename.startswith(f"yob{count}") and filename.endswith('.txt'):
        #If the file is not garbage open the file for reading
        with open(os.path.join(grabData, filename), 'r') as f:
          #Read all lines and return as a list
          lines = f.readlines()

        #Loop through read lines
        for line in lines:
          #Define order for name, gender, and frequency
          name, gender, frequency = line.strip().split(',')
          #Refine frequency as an int just incase
          frequency = int(frequency)

          #Determine whether to write in male or female file
          if gender == 'M':
            mNationalNames.write(f'{name},{frequency},{count}\n')

          if gender == 'F':
            fNationalNames.write(f'{name},{frequency},{count}\n')

    #Update year
    count += 1
