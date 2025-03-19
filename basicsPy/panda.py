import pandas as pd

csv_path='file1.csv'
df=pd.read_csv(csv_path)
df.head()

data = [10, 20, 30, 40, 50]
s = pd.Series(data)
print(s)

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, 35, 28],
        'City': ['New York', 'San Francisco', 'Los Angeles', 'Chicago']}
df = pd.DataFrame(data)
print(df)
