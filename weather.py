from GoogleNews import GoogleNews
googlenews =GoogleNews()
# select the time period
googlenews =GoogleNews(period='7d')
# select the country
googlenews.search('INDIA')
result=googlenews.result()
for x in result:
    print("__"*50)
    print("TOPIC--",x['title'])
    print("UPLOADED--",x['date'])
    print("DESCRIPTION--",x['desc'])
    print("*FOR MORE DETAILS*")
    print("LINK=",x['link'])
