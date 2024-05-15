import pandas as pd

#Pandas part
data = pd.read_csv('fNamesUSANational.txt', header=None, delimiter=',')
data.columns = ['Name', 'Frequency', 'YOB']
data_grpd = data.groupby('YOB').apply(
  lambda x: x.sort_values('Frequency', ascending=False)).reset_index(drop=True)
#Reset index to avoid ambiguity
data_grpd['Rank'] = data_grpd.groupby('YOB')['Frequency'].rank(
  method='dense', ascending=False).astype(int)
#method = dense so that it doesn't skip ranks
print(data_grpd)

# Write output to a new text file
data_grpd.to_csv('fNamesUSANational_ranks.txt', index=False)
