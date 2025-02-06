import pandas as pd

# data = {
#     'Name': ['A', 'B', 'C'],
#     'Age': [19, 20, 21],
#     'City': ['x', 'y', 'z']
# }
data = {
    'Region': ['North', 'North', 'South', 'South', 'East', 'East'],
    'State': ['Delhi', 'Punjab', 'Tamil Nadu', 'Karnataka', 'TG', 'Odisha'],
    'Year': [2021, 2022, 2021, 2022, 2021, 2022],
    'Sales': [750000, 820000, 690000, 720000, 670000, 710000],
    'Profit': [95000, 102000, 85000, 91000, 77000, 88000]
}
df = pd.DataFrame(data)
print(df)
print(df.head(1))
df.set_index(['Region','State','Year'],inplace=True)
print(df)
print()
output=df.loc[('South','Tamil Nadu',2021),'Sales']
print(output)

df_sales=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal'],
                       'Sales':[1570000,1410000,1380000]})
df_profit=pd.DataFrame({'State':['Delhi','Tamil Nadu','West Bengal'],
                        'Profil':[185000,165000,155000]})
df_merged=pd.merge(df_sales,df_profit,on='State',how='inner')
print(df_merged)
# df_merged.to_csv("merged.csv",index=False)
# df=pd.read_csv("customers-100.csv")
# print(df)
# output=df.head(2)
# output.to_csv('output.csv',index=False)
# output.to_json('output.json',index=False)
# output.to_html('output.html',index=False)
# print(df.head().groupby('Email').count())
# df.set_index(['Region','State','Year'],inplace=True)
# print(df)



# df=pd.DataFrame(data)
# df.set_index(['r','s','y'],inplace=True)
# print(df)





