import os
import pandas as pd
import dask.dataframe as dd
import matplotlib.pyplot as plt
import sys
import numpy as np
from IPython.display import Image
from fuzzywuzzy import fuzz


def printStateTable():
  
  df = dd.read_csv("../FormattedData/States/states.txt")
  
  df = df.head(52).to_string(index=False)
  
  print(df)

def validState(state):
  
  df = dd.read_csv("../FormattedData/States/statesLower.txt")
  
  df = df.head(52)
  
  dfL = df[df['long'] == state]
  
  dfS = df[df['short'] == state]
  
  match = 0
  
  if not dfL.empty:
    match = 1

  if not dfS.empty:
    match = 1

  return match

def validNameNational(name, char):

  df = dd.read_csv("../FormattedData/NATIONAL/" + char +
                   "NamesUSANational_ranks.txt")

  df = df[df['Name'] == name]

  if len(df) == 0:

    match = 0

  else:

    match = 1

  return match

def returnShortForm(state):

  df = dd.read_csv("../FormattedData/States/statesLower.txt")

  df = df.head(52)

  dfL = df[df['long'] == state]

  dfS = df[df['short'] == state]

  if not dfL.empty:
    returnShort = dfL.iloc[0, 1]

  elif not dfS.empty:
    returnShort = dfS.iloc[0, 1]

  else:
    returnShort = None

  returnShort = returnShort.upper()

  return returnShort

def popularNames():

  grabData = "../FormattedData/NATIONAL/"

  while True:

    sNumNames = input(
      "How many of the the top names do you wish to display (1-50): ")

    if sNumNames.isdigit() == True:

      numNames = int(sNumNames)

      if numNames >= 1 and numNames <= 50:

        break

      else:

        if numNames < 1: 

         print("Input is too low")

        else:

         print("Input is too high")

    else:
      print("Input is not a valid number")

  while True:

    sYear = input(
      "For what year would you like to search top names for (1880-2021): ")

    if sYear.isdigit() == True:

      year = int(sYear)

      if year >= 1880 and year <= 2021:

        break

      else:

        if year < 1880: 

         print("Input is too low")

        else:

         print("Input is too high")

    else:
      print("Input is not a valid number")
  
  while True:

    demographic = input(
      "Please select to search the male('m') or female('f') demographic: ")

    if demographic.lower() in ["male", "female", "m", "f"]:

      if demographic.lower() == 'm':

        mOrF = 'Male'

      else:

        mOrF = 'Female'

      break

    else:

      print("Invalid input please select male or female to continue")

  fileName = grabData + demographic[0].lower() + "NamesUSANational_ranks.txt"

  df = dd.read_csv(fileName)

  df = df[df['YOB'] == year]

  df = df.drop(['Frequency', 'YOB'], axis=1)

  df = df[['Rank', 'Name']]

  print(df.head(numNames).to_string(index=False))

  print("Here are the top " + str(numNames) + " " + mOrF + " names for the year " + str(year))

def popularNamesTwo():

  #Create empty lists
  statesToBeSearched = []

  stateFilesToBeSearched = []

  addMoreStates = "y"

  #Take input for number of names
  while True:

    sNumNames = input(
      "How many of the the top names do you wish to display (1-50): ")

    if sNumNames.isdigit() == True:

      numNames = int(sNumNames)

      if numNames >= 1 and numNames <= 50:

        break

      else:

        if numNames < 1: 

         print("Input is too low")

        else:

         print("Input is too high")

    else:
      print("Input is not a number")

  #Would you like to see the most popular or least popular names?
  while True:

    mostOrLeast = input(
      "Would you like to see the most popular or least popular names('most' / 'm' or 'least / 'l'): ")

    if mostOrLeast.lower() in ["most", "least", "m", "l"]:

      break

    else:

      print("Invalid input please select most or least to continue")

  #Take input to decide if user wants state spefific or national data
  while True:

    stateSpecific = input(
      "Would you like to search National Data or State Specific Data (input 'national' or 'state'): "
    )

    if stateSpecific.lower() in ["state", "national", "s", "n"]:

      break

    else:

      print("Invalid input please select national or state to continue")

  #Since state datas starts at 1910 instead of 1880 we need to allow for differences in presented range of years that can be searched
  if stateSpecific[0].lower() == 'n':

    minYear = 1880

  else:

    minYear = 1910

  #Take input for first year
  while True:

    sYear = input(
      "Select the first year would you like to start searching from: (" +
      str(minYear) + "-2021): ")

    if sYear.isdigit() == True:

      year1 = int(sYear)

      if year1 >= minYear and year1 <= 2021:

        break

      else:

        if year1 < minYear: 

         print("Input is too low")

        else:

         print("Input is too high")

    else:
      print("Input is not a valid number")

  #Take input for second year and it must be greater or equal to the first year to ensure list can be sorted with extra if statements
  while True:

    sYear = input(
      "Select the second year would you like to start searching from: (" +
      str(year1) + "-2021): ")

    if sYear.isdigit() == True:

      year2 = int(sYear)

      if year2 >= year1 and year2 <= 2021:

        break

      else:

        if year2 < year1: 

         print("Input is too low")

        else:

         print("Input is too high")

    else:
      print("Input is not a valid number")

  #Take input for decision between searching male or female data
  while True:

    demographic = input(
      "Please select to search the male('m') or female('f') demographic: ")

    if demographic.lower() in ["male", "female", "m", "f"]:

      break

    else:

      print("Invalid input please select male or female to continue")

  #In an effort to build a file name a file path must be made, so we build decide whether to move to the Male or Female folder based off previous user input
  if demographic[0].lower() == "m":

    mOrF = "Male"

  else:

    mOrF = "Female"

  #If the user selected state specific
  if stateSpecific[0] == 's':

    #Call function to print all states with short forms
    printStateTable()
    print("Here is a list of states!")

    #This block of code takes user input to build a list of states that the user wants to search
    while True:

      #If the user does not want to add more states then the loop will break
      if addMoreStates[0] == 'n':

        break

      #Takes input for a the name or short form of a state
      stateName = input(
        "One at a time please input states you would like to add to the search: "
      )

      #If the user inputs a valid state name or short form which is verified by a function
      if validState(stateName.lower()) == 1:

        #Then a function takes the valid state name and returns its short form regardless if it was in long or short form before
        stateName = returnShortForm(stateName.lower())

        #Once the short form is returned then it is added to a list to be used later to build file names
        if stateName not in statesToBeSearched:

          statesToBeSearched.append(stateName)
          print("Valid State")

        else:
          print("State has already been added")

        #Takes input to decide whether user would like to add another state to the list
        while True:

          addMoreStates = input("Would you like to add another state('y' for yes or 'n' for no)?  ")

          if addMoreStates.lower() in ["yes", "no", "y", "n"]:

            break

          else:

            print("Invalid input please select 'y' or 'n' to continue")

      #If the state is not valid the loop is repeated and the user is prompted to enter another state until it is valid, this is done to ensure the program has atleast one file that exists that it can read from
      else:

        print("Invalid State. Please refer to the states list and try again")

    #print(statesToBeSearched)

    #For every state in the list, e.g. TX UT, the file path and file name is constructed and added to a new list containing the file name of each state the user selected
    for stateFileName in statesToBeSearched:

      tempFileName = "../FormattedData/States/" + mOrF + "/" + demographic[
        0] + stateFileName + "Names.txt"

      stateFilesToBeSearched.append(tempFileName)

    #print(stateFilesToBeSearched)

    #Define a blank dataframe with columns as Name and Frequency
    df = pd.DataFrame(columns=["Name", "Frequency"])

    #Define the master dataframe as a dask dataframe, needed so that mdf can be compared in (if len(mdf) == 0: )
    mdf = dd.from_pandas(df, npartitions=1)

    #For each file name in the list of state files to be searched
    for stateFileName in stateFilesToBeSearched:

      #Set a dataframe equal to a dataframe of the most recent read file
      df = dd.read_csv(stateFileName)

      #Get rid of lines where year is outside of the span given by the user, in this case anytime before year1
      df = df[df['YOB'] >= year1]

      #Get rid of lines where year is outside of the span given by the user, in this case anytime after year2
      df = df[df['YOB'] <= year2]

      #Get rid of the year of birth column, we do not need it anymore now that our information is filtered
      df = df.drop(['YOB'], axis=1)

      #Now we have a dataframe that has many repeat names and frequencies for years that are gone, df.groupby will group all the repeated names together and sum frequencies for each name
      df = df.groupby('Name')['Frequency'].sum().reset_index()

      #If the mdf is empty then we can set our the master dataframe equal to state dataframe, there is no need to copy anything over any other way
      if len(mdf) == 0:

        mdf = df

      else:

        #In the case that we have multiple states files we are iterating over then we take the grouped dataframe and merge it with our master dataframe on the name column with (on='Name)', this means we will now have two frequencies, Frequency_x and Frequency_y. (how='outer') allows for names that are not in the orignal data frame to be added to the dataframe by including rows from both dataframes and not only the master dataframe
        mdf = dd.merge(mdf, df, on='Name', how='outer')

        #Empty rows are filled to zero for good measure to avoid calculation errors
        mdf = mdf.fillna(0)

        #A new column named Frequency is made and contains the sum of Frequency_x and Frequency_y
        mdf['Frequency'] = mdf['Frequency_x'] + mdf['Frequency_y']

        #Now that we have Frequency as the sum of Frequency_x and Frequency_y the two columns are useless and can be dropped
        mdf = mdf.drop(['Frequency_x', 'Frequency_y'], axis=1)

    #Sort rows in ascending or descending Frequencys such that the most or least popular name is at the top of the dataframe
    if mostOrLeast[0] == 'l':

      mdf = mdf.sort_values('Frequency', ascending=True)

      mOrL = 'least'

    else:

      mdf = mdf.sort_values('Frequency', ascending=False)

      mOrL = 'most'

    #For some reason Frequency is turned into a decimal during this process and it can be reassigned to a int to drop the .0
    mdf['Frequency'] = mdf['Frequency'].astype(int)

    #The dataframe is complete and the top names can be printed using head to print the top N names and (index=false) to get rid of index numbers
    if len(mdf) == 0:

      print("The name you have searched for does not exist or does not exist given spefifications.")

    else:

      print(mdf.head(numNames).to_string(index=False))

      print("Here are the " + str(numNames) + " " + mOrL + " popular " + mOrF.lower() + " names for your selected span of years [" + str(year1) + "-" + str(year2) + "] using state data ", end = "")

      print("[" + ", ".join(str(stateName) for stateName in statesToBeSearched) + "]")

  #If the user selected national
  elif stateSpecific[0] == 'n':

    #Build the file name based on users previous input
    fileName = "../FormattedData/NATIONAL/" + demographic[
      0] + "NamesUSANational_ranks.txt"

    #Since we are reading one file the master dataframe can be set equal to a dataframe of the most recent read file
    mdf = dd.read_csv(fileName)

    #Get rid of lines where year is outside of the span given by the user, in this case anytime before year1
    mdf = mdf[mdf['YOB'] >= year1]

    #Get rid of lines where year is outside of the span given by the user, in this case anytime after year2
    mdf = mdf[mdf['YOB'] <= year2]

    #Get rid of the year of birth column, we do not need it anymore now that our information is filtered
    mdf = mdf.drop(['YOB', 'Rank'], axis=1)

    #Now we have a dataframe that has many repeat names and frequencies for years that are gone, df.groupby will group all the repeated names together and sum frequencies for each name
    mdf = mdf.groupby('Name')['Frequency'].sum().reset_index()

    #Sort rows in ascending or descending Frequencys such that the most or least popular name is at the top of the dataframe
    if mostOrLeast[0] == 'l':

      mdf = mdf.sort_values('Frequency', ascending=True)

    else:

      mdf = mdf.sort_values('Frequency', ascending=False)

    #For some reason Frequency is turned into a decimal during this process and it can be reassigned to a int to drop the .0
    mdf['Frequency'] = mdf['Frequency'].astype(int)

    #The dataframe is complete and the top names can be printed using head to print the top N names and (index=false) to get rid of index numbers
    if len(mdf) == 0:

      print("The name you have searched does not exist or does not exist given the specifications")

    else:

      print(mdf.head(numNames).to_string(index=False))

      print("Here are the top " + str(numNames) + " " + mOrF.lower() + " names for your selected span of years [" + str(year1) + "-" + str(year2) + "] using national data")

def graphName():

  plt.close('all')

  statesToBeSearched = []

  stateFilesToBeSearched = []

  x_vals = []

  y_vals = []

  addMoreStates = "y"

  while True:

    givenName = input("Please input the name you would like to search for: ")

    yesOrNo = input("Are you sure you would like to search for " + givenName +
                    " ('y' for yes or 'n' for no): ")

    if yesOrNo.lower() in ["yes", "no", "y", "n"]:

      if yesOrNo[0].lower() == 'y':

        break

    else:

      print("Invalid input please select yes or no to continue")

  while True:

    demographic = input(
      "Please select to search the male('m') or female('f') demographic: ")

    if demographic.lower() in ["male", "female", "m", "f"]:

      break

    else:

      print("Invalid input please select male or female to continue")

  if (validNameNational(givenName.capitalize(), demographic[0].lower()) == 0):

    print(
      "The name you have searched for does not exist. The function will be exited."
    )

    return

  while True:

    stateSpecific = input(
      "Would you like to search National Data or State Specific Data (input 's' or 'n'): "
    )

    if stateSpecific.lower() in ["state", "national", "s", "n"]:

      break

    else:

      print("Invalid input please select national or state to continue")

  if stateSpecific[0] == 's':

    printStateTable()

    while True:

      if addMoreStates[0] == 'n':

        break

      stateName = input(
        "One at a time please input states you would like to add to the search: "
      )

      if validState(stateName.lower()) == 1:

        stateName = returnShortForm(stateName.lower())

        if stateName not in statesToBeSearched:

          statesToBeSearched.append(stateName)
          print("Valid State")

        else:
          print("State has already been added")

        while True:

          addMoreStates = input("Would you like to add another state('y' for yes or 'n' for no)?  ")

          if addMoreStates.lower() in ["yes", "no", "y", "n"]:

            break

          else:

            print("Invalid input please select yes or no to continue")

      else:

        print("Invalid State. Please refer to the states list and try again")

    if demographic[0].lower() == "m":

      mOrF = "Male"

    else:

      mOrF = "Female"

    for stateFileName in statesToBeSearched:

      tempFileName = "../FormattedData/States/" + mOrF + "/" + demographic[
        0] + stateFileName + "Names.txt"

      stateFilesToBeSearched.append(tempFileName)

    df = pd.DataFrame(columns=["Name", "Frequency"])

    mdf = dd.from_pandas(df, npartitions=1)

    for stateFileName in stateFilesToBeSearched:

      df = dd.read_csv(stateFileName)

      df = df[df['Name'] == givenName.capitalize()]

      if len(mdf) == 0:

        mdf = df

      else:

        mdf = dd.merge(mdf, df, on=['YOB', 'Name'], how='inner')

        mdf = mdf.fillna(0)

        mdf['Frequency'] = mdf['Frequency_x'] + mdf['Frequency_y']

        mdf = mdf.drop(['Frequency_x', 'Frequency_y'], axis=1)

    mdf['Frequency'] = mdf['Frequency'].astype(int)

    if len(mdf) == 0:

      print("The name you have searched for does not exist or does not exist given spefifications.")

    else:

      print(mdf.head(len(mdf)).to_string(index=False))

      print("Here is the graph and longitudinal data for " + givenName + " using state data ")

      print("[" + ", ".join(str(stateName) for stateName in statesToBeSearched) + "]")

  elif stateSpecific[0] == 'n':

    fileName = "../FormattedData/NATIONAL/" + demographic[
      0] + "NamesUSANational_ranks.txt"

    mdf = dd.read_csv(fileName)

    mdf = mdf[mdf['Name'] == givenName.capitalize()]

    mdf = mdf.drop(['Rank'], axis=1)

    mdf['Frequency'] = mdf['Frequency'].astype(int)
    
    if len(mdf) == 0:

      print("The name you have searched for does not exist")

    else:

      print(mdf.head(len(mdf)).to_string(index=False))

      print("Here is the graph and longitudinal data for " + givenName + " using national data ")

  for index, line in mdf.iterrows():

    pFrequency = int(line['Frequency'])

    pYOB = int(line['YOB'])

    x_vals.append(pYOB)

    y_vals.append(pFrequency)

  plt.plot(x_vals, y_vals, label = 'Frequency of ' + givenName, color = 'red')

  plt.legend()

  plt.xlabel("Year")

  plt.ylabel("Frequency")

  plt.title(givenName.capitalize())

  plt.savefig('../UI/Images/graph.png')

def graphRanks():

  plt.close('all')

  statesToBeSearched = []

  stateFilesToBeSearched = []

  x_vals = []

  y_vals = []

  addMoreStates = "y"

  while True:

    givenName = input("Please input the name you would like to search for: ")

    yesOrNo = input("Are you sure you would like to search for " + givenName +
                    "('y' for yes or 'n' for no): ")

    if yesOrNo.lower() in ["yes", "no", "y", "n"]:

      if yesOrNo[0].lower() == 'y':

        break

    else:

      print("Invalid input please select yes or no to continue")

  while True:

    demographic = input("Please select to search the male('m') or female('f') demographic: ")

    if demographic.lower() in ["male", "female", "m", "f"]:

      break

    else:

      print("Invalid input please select male or female to continue")

  if (validNameNational(givenName.capitalize(), demographic[0].lower()) == 0):

    print(
      "The name you have searched for does not exist. The function will be exited."
    )

    return

  while True:

    stateSpecific = input(
      "Would you like to search National Data or State Specific Data (input 'national' or 'state'): "
    )

    if stateSpecific.lower() in ["state", "national", "s", "n"]:

      break

    else:

      print("Invalid input please select national or state to continue")

  if stateSpecific[0] == 'n':

      fileName = "../FormattedData/NATIONAL/" + demographic[0] + "NamesUSANational_ranks.txt"

      mdf = dd.read_csv(fileName)

      mdf = mdf[mdf['Name'] == givenName.capitalize()]

      print(mdf.head(len(mdf)).to_string(index=False))

      print("Here is the graph and longitudinal data for " + givenName + " using national data ")

  elif stateSpecific[0] == 's':

    printStateTable()

    while True:

      if addMoreStates[0] == 'n':

        break

      stateName = input(
        "One at a time please input states you would like to add to the search: "
      )

      if validState(stateName.lower()) == 1:
        
        stateName = returnShortForm(stateName.lower())

        if stateName not in statesToBeSearched:

          statesToBeSearched.append(stateName)
          print("Valid State")

        else: 
          print("State has already been added")

        while True:

          addMoreStates = input("Would you like to add another state('y' for yes or 'n' for no)?  ")

          if addMoreStates.lower() in ["yes", "no", "y", "n"]:

            break

          else:

            print("Invalid input please select yes or no to continue")

      else:

        print("Invalid State. Please refer to the states list and try again")

    if demographic[0].lower() == "m":

      mOrF = "Male"

    else:

      mOrF = "Female"

    for stateFileName in statesToBeSearched:

      tempFileName = "../FormattedData/States/" + mOrF + "/" + demographic[0].lower() + stateFileName + "Names.txt"

      stateFilesToBeSearched.append(tempFileName)

    df = pd.DataFrame(columns=["Name", "Frequency"])

    mdf = dd.from_pandas(df, npartitions=1)

    for stateFileName in stateFilesToBeSearched:

      df = dd.read_csv(stateFileName)

      if len(mdf) == 0:

        mdf = df

      else:

        mdf = dd.merge(mdf, df, on=['YOB', 'Name'], how='inner')

        mdf = mdf.fillna(0)

        mdf['Frequency'] = mdf['Frequency_x'] + mdf['Frequency_y']

        mdf = mdf.drop(['Frequency_x', 'Frequency_y'], axis=1)

    mdf = mdf.sort_values(['YOB', 'Frequency'], ascending=[True, False])

    mdf = mdf.compute()

    mdf['Rank'] = mdf.groupby('YOB')['Frequency'].rank(method='dense', ascending=False)

    mdf['Frequency'] = mdf['Frequency'].astype(int)

    mdf['Rank'] = mdf['Rank'].astype(int)

    mdf = mdf[mdf['Name'] == givenName.capitalize()]

    if len(mdf) == 0:

      print("The name you have searched for does not exist or does not exist given spefifications.")

    else:

      print(mdf.head(len(mdf)).to_string(index=False))

      print("Here is the graph and longitudinal data for " + givenName + " using state data ")

      print("[" + ", ".join(str(stateName) for stateName in statesToBeSearched) + "]")
    
  for index, line in mdf.iterrows():

    pRank = int(line['Rank'])

    pYOB = int(line['YOB'])

    x_vals.append(pYOB)

    y_vals.append(pRank)

  plt.plot(x_vals, y_vals, label = 'Rank of ' + givenName, color = 'red')

  plt.legend()

  plt.xlabel("Year")

  plt.ylabel("Rank")

  plt.title(givenName.capitalize())

  plt.savefig('../UI/Images/graph.png')
  
def graphCommonName():

  plt.close('all')

  statesToBeSearched = []

  stateFilesToBeSearched = []

  x_vals = []

  y1_vals = []

  y2_vals = []

  addMoreStates = "y"

  while True:

    givenName = input("Please input the common name you would like to search for: ")

    yesOrNo = input("Are you sure you would like to search for " + givenName +
                    "('y' for yes or 'n' for no): ")

    if yesOrNo.lower() in ["yes", "no", "y", "n"]:

      if yesOrNo[0].lower() == 'y':

        break

      else:

        print("Invalid input please select yes or no to continue")

  while True:

    stateSpecific = input(
      "Would you like to search National Data or State Specific Data (input 'national' or 'state'): "
    )

    if stateSpecific.lower() in ["state", "national", "s", "n"]:

      break

    else:

      print("Invalid input please select national or state to continue")

  if stateSpecific[0] == 's':

    printStateTable()

    while True:

      if addMoreStates[0] == 'n':

        break

      stateName = input(
        "One at a time please input states you would like to add to the search: "
      )

      if validState(stateName.lower()) == 1:

        stateName = returnShortForm(stateName.lower())

        if stateName not in statesToBeSearched:

          statesToBeSearched.append(stateName)
          print("Valid State")

        else:
          print("State has already been added")

        while True:

          addMoreStates = input("Would you like to add another state('y' for yes or 'n' for no)?  ")

          if addMoreStates.lower() in ["yes", "no", "y", "n"]:

            break

          else:

            print("Invalid input please select yes or no to continue")

      else:

        print("Invalid State. Please refer to the states list and try again")

    for stateFileName in statesToBeSearched:

      tempFileName = "../FormattedData/States/Common/c" + stateFileName + "Names.txt"

      stateFilesToBeSearched.append(tempFileName)

    df = pd.DataFrame(columns=["YOB", "Name", "mFrequency", "fFrequency", "mForF"])

    mdf = dd.from_pandas(df, npartitions=1)

    for stateFileName in stateFilesToBeSearched:

      df = dd.read_csv(stateFileName)

      df = df[df['Name'] == givenName.capitalize()]

      df = df.drop(['mForF'], axis=1)

      if len(mdf) == 0:

        mdf = df

      else:

        mdf = dd.merge(mdf, df, on=['YOB', 'Name'], how='inner')

        mdf = mdf.fillna(0)

        mdf['mFrequency'] = mdf['mFrequency_x'] + mdf['mFrequency_y']

        mdf['fFrequency'] = mdf['fFrequency_x'] + mdf['fFrequency_y']

        mdf = mdf.drop(['mFrequency_x', 'mFrequency_y'], axis=1)

        mdf = mdf.drop(['fFrequency_x', 'fFrequency_y'], axis=1)

    mdf['mFrequency'] = mdf['mFrequency'].astype(int)

    mdf['fFrequency'] = mdf['fFrequency'].astype(int)

    mdf['mForF'] = mdf['mFrequency']/mdf['fFrequency']

    mdf['mForF'] = mdf['mForF'].round(3)

    if len(mdf) == 0:

      print("The name you have searched for does not exist or does not exist given spefifications.")

    else:

      print(mdf.head(len(mdf)).to_string(index=False))

      print("Here is the graph and longitudinal data for " + givenName + " using state data ")

      print("[" + ", ".join(str(stateName) for stateName in statesToBeSearched) + "]")

  elif stateSpecific[0] == 'n':

    mdf = dd.read_csv("../FormattedData/NATIONAL/cNamesUSANational_ranks.txt")

    mdf = mdf[mdf['Name'] == givenName.capitalize()]

    if len(mdf) == 0:

      print("The name you have searched for does not exist")

    else:

      print(mdf.head(len(mdf)).to_string(index=False))

      print("Here is the graph and longitudinal data for " + givenName + " using national data ")

  for index, line in mdf.iterrows():

    pYOB = int(line['YOB'])

    pmF = int(line['mFrequency'])

    pfF = int(line['fFrequency'])

    x_vals.append(pYOB)

    y1_vals.append(pmF)

    y2_vals.append(pfF)

  plt.plot(x_vals, y1_vals, label = 'Male Frequency', color = 'blue')

  plt.plot(x_vals, y2_vals, label = 'Female Frequency', color = 'pink')

  plt.legend()

  plt.xlabel("Year")

  plt.ylabel("Frequency")

  plt.title(givenName.capitalize())

  plt.savefig('../UI/Images/graph.png')
  
def nameMOrF():

  statesToBeSearched = []

  stateFilesToBeSearched = []

  addMoreStates = "y"

  while True:

    sNumNames = input(
      "How many of the the top names do you wish to display (1-50): ")

    if sNumNames.isdigit() == True:

      numNames = int(sNumNames)

      if numNames >= 1 and numNames <= 50:

        break

      else:

        if numNames < 1: 

         print("Input is too low")

        else:

         print("Input is too high")

    else:
      print("Input is not a valid number")

  while True:

    mOrF = input(
      "Would you like to see the most masculine or feminine common names (\"m\" for masculine or \"f\" for feminine): ")

    if mOrF.lower() in ["masculine", "feminine", "m", "f"]:

      break

    else:

      print("Invalid input please select masculine or feminine to continue")

  while True:

    stateSpecific = input(
      "Would you like to search National Data or State Specific Data (input 'n' for national' or 's' for state): "
    )

    if stateSpecific.lower() in ["national", "state", "s", "n"]:

      break

    else:
      print("Invalid input please enter a national or state")

  if stateSpecific[0].lower() == 'n':

    minYear = 1880

  else:

    minYear = 1910

  while True:

    sYear = input(
      "Select the year you would like to search: (" +
      str(minYear) + "-2021): ")

    if sYear.isdigit() == True:

      year = int(sYear)

      if year >= minYear and year <= 2021:

        break

      else:

        if year < minYear: 

         print("Input is too low")

        else:

         print("Input is too high")

    else:
      print("Input is not a valid number")

  if stateSpecific[0] == 's':

    printStateTable()

    while True:

      if addMoreStates[0] == 'n':

        break

      stateName = input(
        "One at a time please input states you would like to add to the search: "
      )

      if validState(stateName.lower()) == 1:
        
          

        stateName = returnShortForm(stateName.lower())

        if stateName not in statesToBeSearched:

          statesToBeSearched.append(stateName)
          print("Valid State")

        else:
          print("State has already been added")

        while True:

          addMoreStates = input("Would you like to add another state ('y' for yes or 'n' for no): ")

          if addMoreStates.lower() in ["yes", "no", "y", "n"]:

            break

          else:

            print("Invalid input please select yes or no to continue")
            
      else:

        print("Invalid State. Please refer to the states list and try again")

    for stateFileName in statesToBeSearched:

      tempFileName = "../FormattedData/States/Common/c" + stateFileName + "Names.txt"

      stateFilesToBeSearched.append(tempFileName)

    df = pd.DataFrame(columns=["YOB", "Name", "mFrequency", "fFrequency", "mForF"])

    mdf = dd.from_pandas(df, npartitions=1)

    for stateFileName in stateFilesToBeSearched:

      df = dd.read_csv(stateFileName)

      df = df.drop(['mForF'], axis=1)

      if len(mdf) == 0:

        mdf = df

      else:

        mdf = dd.merge(mdf, df, on=['YOB', 'Name'], how='inner')

        mdf = mdf.fillna(0)

        mdf['mFrequency'] = mdf['mFrequency_x'] + mdf['mFrequency_y']

        mdf['fFrequency'] = mdf['fFrequency_x'] + mdf['fFrequency_y']

        mdf = mdf.drop(['mFrequency_x', 'mFrequency_y'], axis=1)

        mdf = mdf.drop(['fFrequency_x', 'fFrequency_y'], axis=1)

    mdf['mFrequency'] = mdf['mFrequency'].astype(int)

    mdf['fFrequency'] = mdf['fFrequency'].astype(int)

  elif stateSpecific[0] == 'n':

    mdf = dd.read_csv("../FormattedData/NATIONAL/cNamesUSANational_ranks.txt")

  mdf = mdf[mdf['YOB'] == year]

  mdf['mForF'] = mdf['mFrequency']/mdf['fFrequency']

  mdf['mForF'] = mdf['mForF'].round(3)

  mdf['fForM'] = mdf['fFrequency']/mdf['mFrequency']

  mdf['fForM'] = mdf['fForM'].round(3)

  if mOrF[0] == 'f':

    mdf = mdf.sort_values('mForF', ascending=True)

  else:

    mdf = mdf.sort_values('mForF', ascending=False)

  if len(mdf) == 0:

    print("Data is empty due to state specifications")

  else:

    print(mdf.head(numNames).to_string(index=False))

def compareNames():

  plt.close('all')

  namesToBeGraphed = []

  statesToBeSearched = []

  stateFilesToBeSearched = []

  addMoreStates = "y"

  count = 0

  while True:

    givenName = input("Please input a name you would like to graph: ")

    yesOrNo = input("Are you sure you would like to graph " + givenName +
                    " ('y' for yes or 'n' for no): ")

    if yesOrNo.lower() in ["yes", "no", "y", "n"]:

      if yesOrNo[0].lower() == 'y':

        if givenName not in namesToBeGraphed:
          
          namesToBeGraphed.append(givenName)
          count = count + 1
          
          if count == 5:
            print("Maximum names reached continuing function...")
            break

        else:
          print("Name has already been added")

        while True:

          yesOrNo = input("Would you like to add another name ('y' for yes or 'n' for no): ")

          if yesOrNo.lower() in ["yes", "no", "y", "n"]:

            break

          else:

            print("Invalid input please select yes or no to continue")

        if yesOrNo[0].lower() == 'n':

          break

    else:

      print("Invalid input please select yes or no to continue after entering the name you would like to add")
  
  while True:

    demographic = input(
      "Please select to search the male('m') or female('f') demographic: ")

    if demographic.lower() in ["male", "female", "m", "f"]:

      break

    else:

      print("Invalid input please select male or female to continue")

  for name in namesToBeGraphed:

    if (validNameNational(givenName.capitalize(), demographic[0].lower()) == 0):

      print("The name " + name + " does not exist. The function will be exited.")

      return

  while True:

    stateSpecific = input(
      "Would you like to search National Data or State Specific Data (input 'national' or 'state'): "
    )

    if stateSpecific.lower() in ["state", "national", "s", "n"]:

      break

    else:

      print("Invalid input please select national or state to continue")

  if stateSpecific[0] == 's':

    printStateTable()

    while True:

      if addMoreStates[0] == 'n':

        break

      stateName = input(
        "One at a time please input states you would like to add to the search: "
      )

      if validState(stateName.lower()) == 1:

        stateName = returnShortForm(stateName.lower())

        if stateName not in statesToBeSearched:

          statesToBeSearched.append(stateName)
          print("Valid State")

        else:
          print("State has already been added")

        while True:

          addMoreStates = input("Would you like to add another state('y' for yes or 'n' for no)?  ")

          if addMoreStates.lower() in ["yes", "no", "y", "n"]:

            break

          else:

            print("Invalid input please select yes or no to continue")

      else:

        print("Invalid State. Please refer to the states list and try again")

    if demographic[0].lower() == "m":

      mOrF = "Male"

    else:

      mOrF = "Female"

    for stateFileName in statesToBeSearched:

      tempFileName = "../FormattedData/States/" + mOrF + "/" + demographic[
        0] + stateFileName + "Names.txt"

      stateFilesToBeSearched.append(tempFileName)

    df = pd.DataFrame(columns=["Name", "Frequency"])

    mdf = dd.from_pandas(df, npartitions=1)

    for name in namesToBeGraphed:

      mdf = {}

      x_vals = []

      y_vals = []

      for stateFileName in stateFilesToBeSearched:

        df = dd.read_csv(stateFileName)

        df = df[df['Name'] == name.capitalize()]

        if len(mdf) == 0:

          mdf = df

        else:

          mdf = dd.merge(mdf, df, on=['YOB', 'Name'], how='inner')

          mdf = mdf.fillna(0)

          mdf['Frequency'] = mdf['Frequency_x'] + mdf['Frequency_y']

          mdf = mdf.drop(['Frequency_x', 'Frequency_y'], axis=1)

      mdf['Frequency'] = mdf['Frequency'].astype(int)

      if len(mdf) == 0:

        print("The name " + name + " does not exist")

      else:

        print(mdf.head(len(mdf)).to_string(index=False))

        print("Given above is the longitudinal data for " + name + " using state data", end = "")

        print("[" + ", ".join(str(stateName) for stateName in statesToBeSearched) + "]")

      for index, line in mdf.iterrows():

        pFrequency = int(line['Frequency'])

        pYOB = int(line['YOB'])

        x_vals.append(pYOB)

        y_vals.append(pFrequency)

      plt.plot(x_vals, y_vals, label = 'Frequency of ' + name)

  elif stateSpecific[0] == 'n':

    fileName = "../FormattedData/NATIONAL/" + demographic[
      0] + "NamesUSANational_ranks.txt"

    for name in namesToBeGraphed:

      x_vals = []

      y_vals = []
      
      mdf = dd.read_csv(fileName)

      mdf = mdf[mdf['Name'] == name.capitalize()]

      mdf = mdf.drop(['Rank'], axis=1)

      mdf['Frequency'] = mdf['Frequency'].astype(int)
    
      if len(mdf) == 0:

        print("The name " + name + " does not exist")

      else:

        print(mdf.head(len(mdf)).to_string(index=False))

        print("Given above is the longitudinal data for " + name + " using national data")

      for index, line in mdf.iterrows():

        pFrequency = int(line['Frequency'])

        pYOB = int(line['YOB'])

        x_vals.append(pYOB)

        y_vals.append(pFrequency)

      plt.plot(x_vals, y_vals, label = 'Frequency of ' + name)

  plt.legend()

  plt.xlabel("Year")

  plt.ylabel("Frequency")

  plt.title("Given Names")

  print("Here is the graph for the given names")

  plt.savefig('../UI/Images/graph.png')

def similarNames():

  mFileName = "../FormattedData/NATIONAL/mNamesUSANational_ranks.txt"

  fFileName = "../FormattedData/NATIONAL/fNamesUSANational_ranks.txt"

  mdf = dd.read_csv(mFileName)

  fdf = dd.read_csv(fFileName)

  mdf = mdf.drop(['YOB', 'Rank'], axis=1)

  fdf = fdf.drop(['YOB', 'Rank'], axis=1)

  pdf = dd.concat([mdf, fdf])

  pdf = pdf.fillna(0)

  pdf = pdf.groupby('Name')['Frequency'].sum().reset_index()

  pdf['Frequency'] = pdf['Frequency'].astype(int)

  while True:

    givenName = input("Please input the name you would like to search for: ")

    yesOrNo = input("Are you sure you would like to search for " + givenName +
                    " ('y' for yes or 'n' for no): ")

    if yesOrNo.lower() in ["yes", "no", "y", "n"]:

      if yesOrNo[0].lower() == 'y':

        break

    else:

      print("Invalid input please select yes or no to continue")

  pdf['Score'] = pdf['Name'].apply(lambda x: fuzz.token_sort_ratio(x, givenName), meta=('Name', 'int64'))

  pdf = pdf[pdf['Score'] >= 91]

  pdf = pdf.sort_values(['Score', 'Frequency'], ascending=[False, False])

  if len(pdf) == 0:

    print("The name '" + givenName + "' does not have any similar names")

  else:

    print(pdf.head(len(pdf)).to_string(index=False))
  
  

  

