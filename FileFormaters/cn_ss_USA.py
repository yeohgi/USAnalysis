import dask.dataframe as dd

sdf = dd.read_csv("../FormattedData/States/states.txt")

sdf = sdf.drop(['long'], axis=1)

for index, line in sdf.iterrows():

  shortName = str(line['short'])

  mdf = dd.read_csv("../FormattedData/States/Male/m" + shortName + "Names.txt")

  fdf= dd.read_csv("../FormattedData/States/Female/f" + shortName + "Names.txt")

  cdf = dd.merge(mdf, fdf, on = ['Name', 'YOB'], how='inner')

  cdf = cdf[['YOB', 'Name', 'Frequency_x', 'Frequency_y']]

  cdf = cdf.rename(columns={'Frequency_x' : 'mFrequency', 'Frequency_y' : 'fFrequency'})

  cdf['mForF'] = cdf['mFrequency']/cdf['fFrequency']

  cdf['mForF'] = cdf['mForF'].round(3)

  cdf.to_csv("../FormattedData/States/Common/c" + shortName + "Names.txt", index = False, single_file = True)