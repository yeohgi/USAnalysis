import pandas as pd
import os

dirPath = "FormattedData/States/Female"

os.chdir(dirPath)

def rankFStateFiles(fileName, state):

  #Pandas part
  data = pd.read_csv("f" + state + "Names.txt", header=None, delimiter=',')
  data.columns = ['Name', 'Frequency', 'YOB']
  data_grpd = data.groupby('YOB').apply(
    lambda x: x.sort_values('Frequency', ascending=False)).reset_index(drop=True)
  #Reset index to avoid ambiguity
  data_grpd['Rank'] = data_grpd.groupby('YOB')['Frequency'].rank(
    method='dense', ascending=False).astype(int)
  #method = dense so that it doesn't skip ranks

  data_grpd = data_grpd.iloc[:-1]

  # Write output to a new text file
  data_grpd.to_csv("../Ranks/Female/rankfa" + state + "Names.txt", index=False)
  

for file in os.listdir():

  fileName = f'{file}'
  rankFStateFiles(fileName, file[1:3])