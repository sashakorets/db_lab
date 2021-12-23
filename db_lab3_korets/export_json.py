import json
import psycopg2

username = 'sashakorets'
password = 'admin'
database = 'sashakorets_DB'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

query = '''
    select *
	from wines 
		join province on wines.region = province.region 
	 	join country on province.province = country.province 
			order by 1;
'''

data = {}
with conn:
    cur = conn.cursor()
    cur.execute(query)
    rows = []
    fields = [x[0] for x in cur.description]
    for row in cur:
      rows.append(dict(zip(fields, row)))
    data = rows

with open('Korets_DB.json', 'w') as json_out:
  json.dump(data, json_out, default=str)