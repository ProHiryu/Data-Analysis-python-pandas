# Data Analysis with pandas

## Basics

- Everytime you change your df, you should get an new df `df = df.set_index('Day',inplace=True)`

- `df.Visitors.tolist()`

- `np.array(df[['Visitors','Bounce Rate']]).tolist()`

## pandas IO

- [quandl - datasets](https://www.quandl.com)

- json, html, excel, csv, sql

- `df.rename(columns = ('before_Renmae':'after_rename'))` : rename the columns

- `df = pd.read_html(url)` : get all the dataframe, you need to find the target

## Concatenating and Appending Dataframes

- `s = pd.Series([], index = [])`

## Joining and Merging Dataframes

- [merge](http://pandas.pydata.org/pandas-docs/stable/merging.html) : vs join

- left right outer inner : inner is the default how

## Handling Missing Data

- `df.dropna(how='all',inplace=True)`

- `df.fillna(method='ffill',inplace=True)`

- `df.fillna(value=-99999,inplace=True)`
