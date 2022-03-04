import sqlite3
from pandas_datareader import wb

conn = sqlite3.connect("db/world_bank.db")
conn.row_factory=sqlite3.Row
#Electricity Use, Population Growth, Urban Purpulation, Renewal Energy output
indicators=['EG.USE.ELEC.KH.PC','SP.POP.GROW','SP.URB.TOTL','EG.ELC.RNEW.ZS']
countries = ['GHA','US']

data= wb.download(indicator=indicators,country=countries,start=1990,end=2020)
print(data)
cur = conn.cursor()
cur1 = conn.cursor()
# cur.execute("insert into countries (country_name,iso_name) values('Ghana','GHA')")
#conn.execute("insert into countries (country_name,iso_name) values('Togo','TOG')")
#conn.execute("insert into countries (country_name,iso_name) values('Benin','BEN')")
# cur.close()
#conn.commit()
cur1.execute('SELECT * FROM countries')
countries = cur1.fetchall()
countryList=[]

for country in countries:
    print(country[1])


