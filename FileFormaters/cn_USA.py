import dask.dataframe as dd

mdf = dd.read_csv("../FormattedData/NATIONAL/mNamesUSANational_ranks.txt")

fdf= dd.read_csv("../FormattedData/NATIONAL/fNamesUSANational_ranks.txt")

cdf = dd.merge(mdf, fdf, on = ['Name', 'YOB'], how='inner')

cdf = cdf.drop(['Rank_x', 'Rank_y'], axis=1)

cdf = cdf[['YOB', 'Name', 'Frequency_x', 'Frequency_y']]

cdf = cdf.rename(columns={'Frequency_x' : 'mFrequency', 'Frequency_y' : 'fFrequency'})

cdf['mForF'] = cdf['mFrequency']/cdf['fFrequency']

cdf['mForF'] = cdf['mForF'].round(3)

cdf.to_csv('../FormattedData/NATIONAL/cNamesUSANational_ranks.txt', index = False, single_file = True)