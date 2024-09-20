import sqlite3

conn = sqlite3.connect('healthcare.db')

conn.close()

import pandas as pd
df = pd.read_csv('https://data.cdc.gov/resource/saz5-9hgg.csv')

conn = sqlite3.connect('healthcare.db')

df.to_sql('health_data', conn, if_exists='replace', index=False)

conn.commit()
conn.close()

#test
conn = sqlite3.connect('healthcare.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM health_data LIMIT 5")

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()

#step3
conn = sqlite3.connect('healthcare.db')
query_1 = "select * from health_data where Jurisdiction = 'New York'"
df_query_1 = pd.read_sql_query(query_1, conn)
print(df_query_1)

query_2 = "select count(*) from health_data where Jurisdiction = 'New York'"
df_query_2 = pd.read_sql_query(query_2, conn)
print(df_query_2)

query_3 = "select Jurisdiction,sum(_1st_dose_allocations) from health_data group by Jurisdiction"
df_query_3 = pd.read_sql_query(query_3, conn)
print(df_query_3)

query_4 = "select _1st_dose_allocations from health_data where Jurisdiction = 'New York' order by _1st_dose_allocations desc limit 3"
df_query_4 = pd.read_sql_query(query_4, conn)
print(df_query_4)