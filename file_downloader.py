from urllib import request

goog_url = 'https://query1.finance.yahoo.com/v7/finance/download/GOOG?period1=1504285125&period2=1506877125&interval=1d&events=history&crumb=Do7p3/M5M0S'

def download_data(url):
   response = request.urlopen(url)
   file = response.read()
   url_str = str(file)
   lines = url_str.split("\\n")
   dest_url = r'goog.csv'
   fx = open(dest_url, "w")
   for line in lines:
      fx.write(line + "\n")
   fx.close()

download_data(goog_url)
