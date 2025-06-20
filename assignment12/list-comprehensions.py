import pandas as pd

df = pd.read_csv("../csv/employees.csv")

full_names = [row['first_name'] + " " + row['last_name'] for _, row in df.iterrows()]
print("All names:")
print(full_names)

names_with_e = [name for name in full_names if "e" in name]
print("\nNames with 'e':")
print(names_with_e)