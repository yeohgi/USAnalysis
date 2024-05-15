import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np


def common_names():
  # Load the first file for female names
  file1 = pd.read_csv('../FormattedData/NATIONAL/fNamesUSANational_ranks.txt',
                      header=None,
                      names=['Name', 'Frequency', 'YOB', 'Rank'],
                      dtype={
                        'Frequency': int,
                        'YOB': int,
                        'Rank': int
                      },
                      skiprows=1)

  # Load the second file for male names
  file2 = pd.read_csv('../FormattedData/NATIONAL/mNamesUSANational_ranks.txt',
                      header=None,
                      names=['Name', 'Frequency', 'YOB', 'Rank'],
                      dtype={
                        'Frequency': int,
                        'YOB': int,
                        'Rank': int
                      },
                      skiprows=1)

  # Prompt the user to enter the range of years
  start_year = int(input("Enter the start year: "))
  end_year = int(input("Enter the end year: "))

  # Filter the data for the specified range of years using the query method
  file1 = file1.query('@start_year <= YOB <= @end_year')
  file2 = file2.query('@start_year <= YOB <= @end_year')

  # Merge the two files on the Name column and calculate the ratio
  merged = pd.merge(file1, file2, on='Name', suffixes=('_f', '_m'))
  merged['Ratio(m/fm)'] = merged['Frequency_m'] / merged['Frequency_f']

  # Group by name and sum the frequencies and ratios
  grouped = merged.groupby('Name').agg({
    'Frequency_f': 'sum',
    'Frequency_m': 'sum',
    'Ratio(m/fm)': 'sum'
  }).reset_index()

  # Ask user on what basis they want to rank the names
  rank_basis = input(
    "On what basis do you want ranks, masculine names or feminine names.. For masculine press m / for feminine press f : "
  )
  if rank_basis.lower() == "m":
    grouped['Rank'] = grouped['Ratio(m/fm)'].rank(ascending=False,
                                                  method='min')
    grouped.sort_values(by='Rank', inplace=True)
  elif rank_basis.lower() == "f":
    grouped['Rank'] = grouped['Ratio(m/fm)'].rank(ascending=True, method='min')
    grouped.sort_values(by='Rank', inplace=True)

  pd.options.display.float_format = '{:.2f}'.format

  # Print the results
  print(grouped)

  while True:
    check_name = input("Check for a certain name (y/n): ")
    if check_name.lower() == 'y':
      name = input('Enter a name: ')
      if name in grouped['Name'].values:
        row = grouped[grouped['Name'] == name].iloc[0]
        mfreq = row['Frequency_m']
        ffreq = row['Frequency_f']
        ratio = row['Ratio(m/fm)']
        print("{:<5} {:<5} {:<5} {:<5}".format("NAME", "M_freq", "F_freq",
                                               "RATIO(m/f)"))
        print(f"{name}, {mfreq}  ,  {ffreq}  ,   {ratio:.2f} ")
      else:
        print(f"{name} not found in common names.")
    else:
      break


def common_names():
  # Set the chunksize for reading CSV files
  chunksize = 10000

  # Prompt the user to enter a range of years
  start_year = int(input("Enter start year: "))
  end_year = int(input("Enter end year: "))

  # Read the first file in chunks with explicit data types
  df1_chunks = pd.read_csv(
    '../FormattedData/NATIONAL/fNamesUSANational_ranks.txt',
    dtype={
      'Name': str,
      'Frequency': int,
      'YOB': int,
      'Rank': int
    },
    chunksize=chunksize)

  # Read the second file in chunks with explicit data types
  df2_chunks = pd.read_csv(
    '../FormattedData/NATIONAL/mNamesUSANational_ranks.txt',
    dtype={
      'Name': str,
      'Frequency': int,
      'YOB': int,
      'Rank': int
    },
    chunksize=chunksize)

  # Merge the two dataframes on the 'Name' column to find common names
  common_names = set()
  for df1 in df1_chunks:
    for df2 in df2_chunks:
      # Filter the dataframes to include only the specified year range
      df1_filtered = df1[(df1['YOB'] >= start_year) & (df1['YOB'] <= end_year)]
      df2_filtered = df2[(df2['YOB'] >= start_year) & (df2['YOB'] <= end_year)]
      common_names.update(
        set(pd.merge(df1_filtered, df2_filtered, on='Name')['Name'].tolist()))

  print(common_names)


# Define function to read data from text file
def read_data(file_path, name):

  x_vals = []
  y_vals = []

  with open(file_path, 'r') as f:
    next(f)  #skip first line
    for line in f:
      x, y, xU, yU = line.strip().split(',')
      if (x == name):
        x_vals.append(int(xU))
        y_vals.append(int(y))

  return x_vals, y_vals


# Define function to generate line graph visualization
def generate_line_graph(x_vals, y_vals, name):
  plt.plot(x_vals, y_vals)
  plt.xlabel("Year")
  plt.ylabel("Frequency")
  plt.title(name)
  plt.show()
  return 0


# Get user input for file path and title
qName = input("Do you want to search for a male or female name? (M/F) ")

if (qName.lower() == 'f'):
  name = input("Enter the name: ")
  x_vals, y_vals = read_data(
    "FormattedData/NATIONAL/fNamesUSANational_ranks.txt", name)
elif (qName.lower() == 'm'):
  name = input("Enter the name: ")
  x_vals, y_vals = read_data(
    "FormattedData/NATIONAL/mNamesUSANational_ranks.txt", name)

#Calling
generate_line_graph(x_vals, y_vals, name)
