import pandas as pd
from db_management import populate_table


heart_df = pd.read_csv("heart.csv")
print(heart_df.head())
populate_table(table_name="heart", df=heart_df)

