import csv
import psycopg2

username = 'sashakorets'
password = 'admin'
database = 'sashakorets_DB'
host = 'localhost'
port = '5432'

csv_out = 'Korets_DB.csv'


conn = psycopg2.connect(user=username, password=password, dbname=database, host = host, port = port)

with conn:
    cur = conn.cursor()
    cur.execute('''
            select * from wines 
                join province on wines.region = province.region 
                join country on province.province = country.province order by 1
            ''')
    fields = [x[0] for x in cur.description]
    with open(csv_out, 'w') as outfile:
        csv.writer(outfile).writerow(fields)
        for row in cur:
            csv.writer(outfile).writerow([str(x) for x in row])
