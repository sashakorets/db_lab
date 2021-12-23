import csv
import psycopg2

username = 'sashakorets'
password = 'admin'
database = 'sashakorets_DB'
host = 'localhost'
port = '5432'


INPUT_CSV_FILE = 'winemag-data_first150k.csv'

query_0 = '''
DELETE FROM wines;
DELETE FROM province;
DELETE FROM country;
'''

query_1 = '''
INSERT INTO country (province,country) VALUES (%s, %s)
'''
query_2 = '''
INSERT INTO province (region,province) VALUES (%s, %s)
'''
query_3 = '''
INSERT INTO wines (wine_id,wine_name,wine_points,wine_price,region) VALUES (%s, %s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

with conn:
    cur = conn.cursor()

    #first table
    cur.execute(query_0)
    province = []
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['province'] in province or row['province'] == "" or row['province'] == None:
                continue
            else:
                province.append(row['province'])
                values = (row['province'], row['country'])
                cur.execute(query_1, values)

    #second table
    region = []
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['region_1'] in region or row['region_1'] == "" or row['region_1'] == None:
                continue
            else:
                region.append(row['region_1'])
                values = (row['region_1'], row['province'])
                cur.execute(query_2, values)

    #third table
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        for idx, row in enumerate(reader):
            if row['region_1'] == "" or row['designation'] == "" :
                continue
            elif row['price'] == "" or not row['price'].isnumeric():
                continue
            elif row['points'] == "" or not row['points'].isnumeric():
                continue
            elif len(row['designation']) > 255 or len(row['region_1']) > 49:
                continue
            elif "'" in row['designation'] or '"' in row['designation']:
                continue
            else:
                values = (int(row["id"]), row['designation'], int(row['points']), int(row['price']), row['region_1'])
                cur.execute(query_3, values)

    conn.commit()