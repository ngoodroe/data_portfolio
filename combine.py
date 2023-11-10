import pandas as pd
import os

csv_folder = os.getcwd()


csv_files = [os.path.join(csv_folder, file) for file in os.listdir(csv_folder) if file.endswith('.txt')]
combine = pd.DataFrame()

for csv_file in csv_files:
    year = csv_file[37:-4]
    data = df2 = pd.read_csv(csv_file, names = ['Name','Gender','Count'],
                             index_col = ['Name','Gender'])
    data['Year'] = csv_file[37:-4]
    try:
        combine = combine.append(data)
    except:
        combine = data

    print(year)
    

    
#combined_data.to_csv('combined_name_data.csv', index=False)

'''

df = pd.read_csv('yob2022.txt',names=['Name','Gender','num'], index_col='Name')

csv_files[0][37:-4] is the year in the top file

df2 = pd.read_csv(c[1],names = ['Name','Gender',c[1][37:-4]]
		      , index_col = ['Name','Gender'])

df = pd.merge(df1,df2,on = ['Name','Gender'], how='outer')
'''
