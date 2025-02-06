# import csv
# import os
import pandas as pd
# csv_filename = "user_data.csv"

# headers = ["Name", "Age", "City"]

# if not os.path.exists(csv_filename):
#     with open(csv_filename, mode="w", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow(headers)

# def add_entry():
#     name = input("Enter Name: ")
#     age = input("Enter Age: ")
#     city = input("Enter City: ")

#     with open(csv_filename, mode="a", newline="") as file:
#         writer = csv.writer(file)
#         writer.writerow([name, age, city])

#     print("Data added successfully!")

# while True:
#     add_entry()
#     more = input("Do you want to add another entry? (y/n): ")
#     if more != "y" or more !='Y':
#         break

# print("CSV file successfully created!")

df=pd.read_csv("user_data.csv")
print(df)
output=df.head(2)
output.to_csv('real.csv',index=False)
output.to_json('real.json',index=False)
output.to_html('real.html',index=False)
print(df.head().groupby('City').count())
