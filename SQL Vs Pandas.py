import pandas as pd
import sqlite3
# create and connect to database
connector = sqlite3.connect('test_result.db')

# View tables :
df= pd.read_sql('SELECT * FROM sweets', connector)
# print(df)
df.to_csv("Sweets.csv")

# Table with types of sweets and their ID.
ef=pd.read_sql('SELECT * FROM sweets_types', connector)
# print(ef)

# Table with a set of identifiers for the type of sweetness, storehouse and manufacturer.
ff=pd.read_sql('SELECT * FROM manufacturers_storehouses', connector)
# print(ff)

# Table with information about storehouses.
gf=pd.read_sql('SELECT * FROM storehouses', connector)
# print(gf)

# Table with information about manufacturers.
hf= pd.read_sql('SELECT * FROM manufacturers', connector)
# print(hf)

# Queries:
# Creating Pandas dataframes for basic SQL tables.
# get SQL tables as pandas dataframes
df_sweets = pd.read_sql("SELECT * FROM sweets;", connector)
df_sweets_types = pd.read_sql("SELECT * FROM sweets_types;", connector)
df_manufacturers_storehouses = pd.read_sql("SELECT * FROM manufacturers_storehouses", connector)
df_storehouses = pd.read_sql("SELECT * FROM storehouses", connector)
df_manufacturers = pd.read_sql("SELECT * FROM manufacturers", connector)

# Show the names of sweets which weight is 300:
# Pandas
# convert data type
df_sweets['weight'] = pd.to_numeric(df_sweets['weight'])
a=df_sweets[df_sweets.weight == 300].name
# print(a)
# SQL
pd.read_sql("SELECT name FROM sweets WHERE weight = '300'", connector)

# Show the names of sweets which cost is 100:
# Pandas
# convert data type
df_sweets['cost'] = pd.to_numeric(df_sweets['cost'])
b = df_sweets[df_sweets.cost == 100].name
# print(b)
# SQL
pd.read_sql("SELECT name FROM sweets WHERE cost = '100'", connector)

# Find a list of sweets that start with “M”:
# Pandas
c = df_sweets[df_sweets.name.str.startswith('M')].name
# print(c)
# SQL ('%' = any number of characters,  '_' = one character.
pd.read_sql("SELECT name FROM sweets WHERE name LIKE 'M%'", connector)

# Names of sweets that have a cost of 150 and a weight of 300
# Pandas
d = df_sweets[(df_sweets.cost == 150) & (df_sweets.weight == 300)].name
# print(d)
# SQL
pd.read_sql("SELECT name FROM sweets WHERE cost = '150' AND weight = '300'", connector)

# Names of sweets which cost is from 200 to 300:
# Pandas
e = df_sweets[df_sweets['cost'].between(200, 300)].name
# print(e)
# SQL
pd.read_sql("SELECT name FROM sweets WHERE cost BETWEEN '200' AND '300'", connector)

# Sort names of sweets by ID in descending order (The sample included sweets which cost is 200 and 300 inclusive):
# Pandas
f = df_sweets.sort_values(by='id', ascending=False).name
# print(f)
# SQL
pd.read_sql("SELECT name FROM sweets ORDER BY id DESC", connector)

# Find the name of the sweet with the highest price:
# Pandas
g = df_sweets[df_sweets.cost == df_sweets.cost.max()].name
# print(g)
# SQL
pd.read_sql("SELECT name FROM sweets WHERE cost = (SELECT MAX(cost) FROM sweets)", connector)

# Which cities have storehouses?:
# Pandas
h = df_storehouses['city'].unique()
print(h)
# SQL
pd.read_sql("SELECT DISTINCT city FROM storehouses", connector)

# Find manufacturers in more than one city:
# Pandas
i = df_manufacturers.groupby('name').name.count()[df_manufacturers.groupby('name').name.count() > 1]
# print(i)
# SQL
pd.read_sql("""
SELECT name, COUNT(name) as 'name_count' FROM manufacturers
GROUP BY name HAVING COUNT(name) > 1
""", connector)

# Find the names of all chocolates:
# Pandas
j = df_sweets.merge(df_sweets_types, left_on='sweets_types_id', right_on='id').query('name_y == "chocolate"').name_x
# print(j)
# SQL
pd.read_sql("""
SELECT sweets.name FROM sweets
JOIN sweets_types ON sweets.sweets_types_id = sweets_types.id
WHERE sweets_types.name = 'chocolate';
""", connector)

# Find the number of sweets for each type. In the response, display the name of the type and the quantity:
# Pandas
k = df_sweets.merge(df_sweets_types, left_on='sweets_types_id', right_on='id').groupby('name_y').id_x.count()
# print(k)
# SQL
pd.read_sql("""
SELECT sweets_types.name, COUNT(sweets.id) as 'sweets_count' FROM sweets
JOIN sweets_types ON sweets.sweets_types_id = sweets_types.id
GROUP BY sweets_types.name
""", connector)

# Find types of sweets that have more than 2 quantity:
# Pandas
df_sweets_sweets_types = pd.merge(df_sweets, df_sweets_types, left_on='sweets_types_id', right_on='id')
l = df_sweets_sweets_types.groupby('name_y').id_x.count()[df_sweets_sweets_types.groupby('name_y').id_x.count() > 2]
# print(l)
# SQL
pd.read_sql("""
SELECT sweets_types.name, COUNT(sweets.id) as 'sweets count' FROM sweets
JOIN sweets_types ON sweets.sweets_types_id = sweets_types.id 
GROUP BY sweets_types.name
HAVING COUNT(sweets.id) > 2;
""", connector)

# Which cities have storehouses with sweets “Milty”?:
# Pandas
df_sweets_manufacturers_storehouses = pd.merge(df_sweets,
                                               df_manufacturers_storehouses,
                                               left_on='manufacturer_id',
                                               right_on='manufacturers_id')
m = df_sweets_manufacturers_storehouses.merge(df_storehouses,
                                          left_on='storehouses_id',
                                          right_on='id').query('name_x == "Milty"').city
# print(m)
# SQL
pd.read_sql("""
SELECT storehouses.city FROM storehouses
JOIN manufacturers_storehouses ON storehouses.id = manufacturers_storehouses.storehouses_id
JOIN sweets ON sweets.manufacturer_id = manufacturers_storehouses.manufacturers_id
WHERE sweets.name = 'Milty'
""", connector)

# How many sweets are in each storehouse?:
# Pandas
df_storehouses_manufacturers_storehouses = pd.merge(df_storehouses,
                                                    df_manufacturers_storehouses,
                                                    how='left',
                                                    left_on='id',
                                                    right_on='manufacturers_id')
n = df_storehouses_manufacturers_storehouses.merge(df_sweets,
                                               how='left',
                                               left_on='manufacturers_id',
                                               right_on='manufacturer_id').groupby('name_x').id_y.count()
# print(n)
# SQL (LEFT JOIN is used so that storehouses with zero sweets are included in the selection.)
pd.read_sql("""
SELECT storehouses.NAME, COUNT(sweets.id) as 'sweets_count' FROM storehouses
LEFT JOIN manufacturers_storehouses ON storehouses.id = manufacturers_storehouses.storehouses_id
LEFT JOIN sweets ON sweets.manufacturer_id = manufacturers_storehouses.manufacturers_id
GROUP BY storehouses.NAME
""", connector)

# Find storehouses with more than 8 sweets:
# Pandas
df_storehouses_manufacturers_storehouses = pd.merge(df_storehouses,
                                                    df_manufacturers_storehouses,
                                                    how='left',
                                                    left_on='id',
                                                    right_on='manufacturers_id')
df_smss = df_storehouses_manufacturers_storehouses.merge(df_sweets,
                                                         how='left',
                                                         left_on='manufacturers_id',
                                                         right_on='manufacturer_id')
o = df_smss['name_x'].value_counts()[df_smss['name_x'].value_counts() > 8]
# print(o)
# SQL
pd.read_sql("""
SELECT storehouses.name, COUNT(sweets.id) as 'sweets_count' FROM storehouses
LEFT JOIN manufacturers_storehouses ON storehouses.id = manufacturers_storehouses.storehouses_id
LEFT JOIN sweets ON sweets.manufacturer_id = manufacturers_storehouses.manufacturers_id
GROUP BY storehouses.name
HAVING COUNT(sweets.id) > 8
""", connector)

# Selection
# Prepare an upload about the types of sweets produced since March 2022.
# The selection must contain the following attributes:
# - Type of sweet;
# - Number of sweets;
# - Number of sweets without sugar;
# - Number of sweets requiring freezing;
# - Number of sweets with manufacturer’s phone number and weight of 300 grams.
# Pandas
df_sweets_sweets_types = pd.merge(df_sweets, df_sweets_types, left_on='sweets_types_id', right_on='id')
df_sweets_sweets_types_manufacturers_storehouses = df_sweets_sweets_types.merge(df_manufacturers_storehouses,
                                                                                left_on='manufacturer_id',
                                                                                right_on='manufacturers_id')
df_sstmsm = df_sweets_sweets_types_manufacturers_storehouses.merge(df_manufacturers,
                                                                   left_on='manufacturers_id',
                                                                   right_on='id',
                                                                   suffixes=('_w', '_z'))
def my_agg(x):
    names = {
        'sweets_count': x[x.production_date >= '2022-03-01'].id_x.count(),
        'without_sugar': x[(x.production_date >= '2022-03-01') & (x.with_sugar == 0)].id_x.count(),
        'requires_freezing': x[(x.production_date >= '2022-03-01') & (x.requires_freezing == 1)].id_x.count(),
        'sweets_300g_phone': x[(x.production_date >= '2022-03-01') & (x.phone != '') & (x.weight == 300)].id_x.count(),
    }
    return pd.Series(names)
p = df_sstmsm.groupby('name_y').apply(my_agg)
print(p)
# SQL
pd.read_sql("""
SELECT sweets_types.name,
    COUNT(CASE WHEN production_date >= '2022-03-01' THEN 1 ELSE NULL END) as 'sweets_count',
    COUNT(CASE WHEN sweets.with_sugar = 0 
AND production_date >= '2022-03-01' THEN 1 ELSE NULL END) as 'without_sugar',
    COUNT(CASE WHEN sweets.requires_freezing = 1
AND production_date >= '2022-03-01' THEN 1 ELSE NULL END) as 'requires_freezing',
    COUNT(CASE WHEN manufacturers.name = 'Mishan' AND sweets.weight = 300
AND production_date >= '2022-03-01' THEN 1 ELSE NULL END) as 'sweets_300g_phone'
FROM sweets
JOIN sweets_types ON sweets.sweets_types_id = sweets_types.id
JOIN manufacturers_storehouses ON manufacturers_storehouses.manufacturers_id = sweets.manufacturer_id
JOIN manufacturers ON manufacturers.id = manufacturers_storehouses.manufacturers_id
GROUP BY sweets_types.name
""", connector)


# Conclusion
# It is possible to dump a table from an entire SQL database and then process it with Pandas,
# but it is better to make a complex SQL query and get the result immediately, because:
# 1.The load on the database will be less, since there is no need to unload the entire tables;
# 2.Uploading will be faster, since your machine will receive selected data, and not everything in a row;
# 3.Your machine will be less loaded.
