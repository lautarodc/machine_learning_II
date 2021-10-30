from db_management import create_table


heart_schema = """
row_timestamp TIMESTAMP NOT NULL,
age INT NOT NULL,
sex INT NOT NULL,
cp INT NOT NULL,
trestbps INT NOT NULL,
chol INT NOT NULL,
fbs INT NOT NULL,
restecg INT NOT NULL,
thalach INT NOT NULL,
exang INT NOT NULL,
oldpeak FLOAT NOT NULL,
slope INT NOT NULL,
ca INT NOT NULL,
thal INT NOT NULL,
target INT NOT NULL
"""


create_table(table="heart", schema=heart_schema)
