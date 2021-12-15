import psycopg2
import matplotlib.pyplot as plt

username = 'sashakorets'
password = 'admin'
database = 'sashakorets_DB'
host = 'localhost'
port = '5432'

query_1 = '''
select country, count(country) from wines join province on wines.region = province.region join country on province.province = country.province group by country;
'''
query_2 = '''
select wine_id, wine_price from wines join province on wines.region = province.region join country on province.province = country.province order by 1;
'''

query_3 = '''
select wine_points, count(wine_points) from wines join province on wines.region = province.region join country on province.province = country.province group by wine_points;
'''

con = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
print(type(con))

with con:

    cur = con.cursor()

    print('1.  ')
    cur.execute(query_1)
    countries = []
    amount = []
    for row in cur:
        print(row)
        countries.append(row[0])
        amount.append(row[1])

    figure, (bar_ax, pie_ax, bar_2_ax) = plt.subplots(1, 3, figsize=(22,12))
    pie_ax.pie(amount, labels=countries, autopct='%1.1f%%')
    pie_ax.set_title('Найбільші винні країни')

    print("\n2. ")
    cur.execute(query_2)
    type = []
    elevation = []
    for row in cur:
        print(row)
        type.append(row[0])
        elevation.append(abs(row[1]))

    bar_ax.bar(type, elevation, width=0.5)
    bar_ax.set_xticklabels(type, rotation=35, ha='right')
    bar_ax.set_title('price of more popular wines')
    bar_ax.set_ylabel("price in dollars")

    print("\n3. ")
    cur.execute(query_3)

    country = []
    elevation = []
    for row in cur:
        print(row)
        country.append(row[0])
        elevation.append(abs(row[1]))

    bar_2_ax.bar(country, elevation, width=0.5)
    bar_2_ax.set_xlabel('rating of wines')
    bar_2_ax.set_ylabel("count of wines")

    plt.show()