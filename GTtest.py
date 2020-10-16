''' Testar no Google Colab'''
from pytrends.request import TrendReq
pytrend = TrendReq()

# Mais pesquisadas
df = pytrend.top_charts(2019, hl='pt-BR', tz=300, geo='GLOBAL')
df.head()

pytrend.build_payload(kw_list=['Coritiba FC'])
# Intereces por regiao
df = pytrend.interest_by_region()
df.head(50)

#df.reset_index().plot(x='geoName', y='Coritiba FC', figsize=(120, 5), kind ='bar') #Com grafico
