Best Practises
Use .loc and .iloc method. Better than just conditional expression to access cells.
Use of .at and .iat is faster than other methods when accessing single cell.
.assign is useful when you wnat to set more than one column values. 
.assign is also useful when we want to chaining.e.g. df.assing(do one thing).(do second thing)

Selecting Single Column

df['x_loc'] or df.x_loc

Multiple Columns
df['x_loc', 'y_loc']
columns = ['x_loc', 'y_loc']
myslice = df[columns]

Filtering based on column name like
myslice = df.filter[like='loc']
myslice = df.filter[regxex='\d']

Using iloc and loc
df.iloc[4] or df.iloc[[2,6,8]]
df.iloc[1:4]
df.iloc[1:4, [2,4,5]]  # Selecting rows and columns
df.iloc[2,4] # Selecting single value

df.set_index('x_loc') # set column as index
df.set_index(['x_loc', 'y_loc'])  # Setting multiple columns as Index
df.loc[0.6] # When x_loc is indexer
df.loc[[0.6, 0.9, 1.2]]
df.loc[:, ['x_loc', 'y_loc']]

When using loc
df.loc[:] = Dataframe
df.loc[int] = Dataframe if you have more than one column and Series if you have only 1 column in the dataframe
df.loc[:, ["col_name"]] = Dataframe
df.loc[:, "col_name"] = Series

When Not using loc
df["col_name"] = Series
df[["col_name"]] = Dataframe

#While Operating on Dataframe, the index operations such as below row array. 
# This array index when used as input in iloc will also return a array.
# When you get array, to get value at individual cell, you need to use values[0]
#This will return single value.
val = df['col_name'].values[0]
#This will return array index
index = df.loc[df['x_loc' == 4]]['current_cell'].index
#Since index is also an array index, you will get array in below operation
mycell_array = df.iloc[index]['current_cell']
mycell = mycell_array.values[0] # Here we need to check if mycell_array is empty or not, using mycell_array.size == 0

row_number = df.index[4]

Query
df_filtered = df.query('salary>30000')
df_filtered = df[(df.salary >= 30000) & (df.year == 2017)]  # Query with Chaining
df.filter(regex='e$', axis=1)  # Using Filter, axis = 1 is column selection with regx
df.filter(like='bbi', axis=0)  # Using like, selecting rows containg word with bbi in it

iat and at are much faster than loc and iloc in selecting single values
x_val = 0.3
single_point = df.loc[x_val, 'y_loc']
single_point = single_point = df.af[x_val, 'y_loc']
df.at[501,'column_name']  #501 represents the row index.
timeit single_point = df.af[x_val, 'y_loc']  #knowing how much time this operatiion takes
single_point = df.iloc[rownum, colnum]
single_point = df.iat[rownum, colnum]


Setting new index
df.set_index('x_loc', inplace=True)

Setting Single Cell in Dataframe  # Use loc method
df_sim.loc[df_sim['x_loc']==0.0, 'occupied'] = True 
df.set_value(index, 'COL_NAME', value)
df.loc[conditional_index , [col name]]= <new value>


Manipulating columns
df.columns # Getting columns
x_loc_column_index = df.columns.get_loc('x_loc')
Rearranging columns
set(df.columns) = set(new_columns)

Dataframe Apply and Assign for new or old columns
df_sim['current_cell'] = df_sim.apply(lambda row: getInitCell(row, r, vel_at_entry) if row['x_loc'] == 0.0 else np.NaN, axis=1)
df.assign(temp_f=lambda x: x.temp_c * 9 / 5 + 32)
          temp_c  temp_f
Portland    17.0    62.6
Berkeley    25.0    77.0
df.assign(New_team = lambda x: df['Team']+'_GO',  
          Revised_Salary = lambda x: df['Salary']  
                             + df['Salary'] / 10)
# Assign allows chaining e.g. df.assign(some assign).(do something else)


Append and Concat 
Appending iteratively is costly. So create list, and append entire list to DataFrame.
Append returns new object, does not add to original one.
Conact is faster than Append. 

df = pd.DataFrame([[1, 2], [3, 4]], columns=['A', 'B'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns=['A', 'B'])
df_new = df.append(df2, ignore_index=True)

pd.concat([pd.DataFrame([i], columns=['A']) for i in range(5)],
          ignore_index=True)
          
You can also used iloc to append a row.
Getting row count - len(df.index), len(df), df.shape[0] or row,count = df.shape
index_next = len(df.index) + 1
pd.DataFrame.iloc[5,66, 'tutbulent', 'dense']

df_new = df.append({'x_loc' : 5 , 'y_loc' : 22} , ignore_index=True)
df_new = df.append(pd.Series([5, 22], index=df.columns ), ignore_index=True)
df_new = dfObj.append(listOfSeries , ignore_index=True)
df.iloc[2] = [5,66, 'tutbulent', 'dense']
df.loc['x_loc'] = [5,66, 'tutbulent', 'dense']  #x_loc is the index

Quick Reference
df.drop_duplicates(subset = 'x_loc')
df.isnull()
df.notnull()
df.dropna(how='all')  # if all columns are null
df.dropna(subset=['x_loc', 'y_loc'], how='any') #if any one is missing
df.dropna(subset=['x_loc', 'y_loc'], how='any')  # if both are missing

ufo['Shape Reported'].value_counts(dropna=False)  # value of each type
ufo['Shape Reported'].fillna(value='VARIOUS', inplace=True)
----------------------------------------
isin
s = pd.Series(['lama', 'cow', 'lama', 'beetle', 'lama',
               'hippo'], name='animal')
s.isin(['cow', 'lama']) # Returns boolean array
0     True
1     True
2     True
3    False
4     True
5    False

-------------------------------

Sorting
movies.sort_values('duration', ascending=False)
movies.sort_values(['duration', 'rating'], ascending=False)
drinks.continent.value_counts().sort_values()
drinks.continent.value_counts()['Africa']

Unique
df_sim.x_loc.unique()

Dictionary
dict = { '22': 'cell22', '33': 'cell33', '44': 'cell44' }
dict.hasKey('22')
dict.keys()
myval = dict.get('22') # will return value
myval = dict.get('99') # will return None
myval = dict.get('99', 'Custom No Value') # will return 'Custom No Value'
Creating Dictionary from Numpy Array
dict_cells = {dict_key: 'value'+str(i) for i, dict_key, i in enumerate(np_array)}

Pandas Dataframe to Numpy Array and then create dictionary
np_array = df_sim['loc'].to_numpy()
dict_cells = {dict_key: 'value'+str(i) for i, dict_key, i in enumerate(np_array)}  # create dictionary using enumerate


Saving the data to a file
df.to_csv('file1.csv') 
df.to_csv('file2.csv', header=False, index=False)
df.to_csv(r'C:\Users\Admin\Desktop\file3.csv', index=False) 

compression_opts = dict(method='zip',
                        archive_name='out.csv')
df.to_csv('out.zip', index=False,
          compression=compression_opts)
Many Options exists to save file.e.g. separator, date/decimal formats, line terminator,
compression, escapae character
