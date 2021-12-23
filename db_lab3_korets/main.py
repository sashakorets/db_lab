import psycopg2
from matplotlib import pyplot as plt

username = 'sashakorets'
password = 'admin'
database = 'sashakorets_DB'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(conn))

query_1 = ''' 
        CREATE VIEW COUNTRY_COUNT AS
            select (country), count(country) from wines 
                join province on wines.region = province.region 
                join country on province.province = country.province 
                    group by country;'''

query_2 = ''' 
        CREATE VIEW PRICE_COUNT AS
            select wine_price, count(wine_price) from wines
                join province on wines.region = province.region
                join country on province.province = country.province
                    group by wine_price;'''

query_3 = ''' 
        CREATE VIEW POINTS_COUNT AS
            select wine_points, count(wine_points) from wines
                join province on wines.region = province.region
                join country on province.province = country.province
                    group by wine_points;'''

with conn:
  cur = conn.cursor()
  cur.execute('DROP VIEW IF EXISTS COUNTRY_COUNT')
  cur.execute(query_1)
  cur.execute('SELECT * FROM COUNTRY_COUNT')
  countries = []
  amount = []
  for row in cur:
    #print(row)
    countries.append(row[0])
    amount.append(row[1])
  figure, (bar_ax, pie_ax, bar_2_ax) = plt.subplots(1, 3, figsize=(22, 12))
  pie_ax.pie(amount, labels=countries, autopct='%1.1f%%')
  pie_ax.set_title('Кількість  вина у кожній країні')


  cur.execute('DROP VIEW IF EXISTS PRICE_COUNT')
  cur.execute(query_2)
  cur.execute('SELECT * FROM PRICE_COUNT')
  type = []
  elevation = []
  for row in cur:
    #print(row)
    type.append(row[0])
    elevation.append(abs(row[1]))
  bar_ax.bar(type, elevation, width=0.5)
  #bar_ax.set_xticklabels(type, rotation=35, ha='right')
  bar_ax.set_title('Мода цін на вина')
  bar_ax.set_xlabel('нон')
  bar_ax.set_ylabel("нон")


  cur.execute('DROP VIEW IF EXISTS POINTS_COUNT')
  cur.execute(query_3)
  cur.execute('SELECT * FROM POINTS_COUNT')
  country = []
  elevation = []
  for row in cur:
    #print(row)
    country.append(row[0])
    elevation.append(abs(row[1]))
  bar_2_ax.bar(country, elevation, width=0.5)
  bar_2_ax.set_title("мода значень оціники вина у таблиці")
  bar_2_ax.set_xlabel('нон')
  bar_2_ax.set_ylabel("нон")

  plt.show()