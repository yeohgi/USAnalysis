import os

dirPath = "../Unformatted Data/STATE SPECIFIC"

os.chdir(dirPath)

def readStateFiles(fileName, state):

  fStateNames = open("../../FormattedData/States/Female/f" + state + "Names.txt", 'w')
  mStateNames = open("../../FormattedData/States/Male/m" + state + "Names.txt", 'w')
  
  with open(fileName, 'r') as f:
    lines = f.readlines()

    fStateNames.write(f'Name,Frequency,YOB\n')
    mStateNames.write(f'Name,Frequency,YOB\n')

    for line in lines:
      
      part = line.strip().split(',')
      gender = part[1]
      year = part[2]
      name = part[3]
      freq = part[4]

      if(gender == "F"):
        fStateNames.write(f'{name},{freq},{year}\n')
        
      elif(gender == 'M'):
        mStateNames.write(f'{name},{freq},{year}\n')

    f.close()
    fStateNames.close()
    mStateNames.close()

for file in os.listdir():

  fileName = f'{file}'
  readStateFiles(fileName, file[0:2])
  