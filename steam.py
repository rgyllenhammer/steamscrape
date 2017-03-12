import bs4 as bs
import urllib.request

url = 'http://store.steampowered.com/search/?specials=1&os=win'
page = urllib.request.urlopen(url).read()
soup = bs.BeautifulSoup(page, 'lxml')

imglist = []
datalist = []
titlelist = []
oldnewprices = []


def findimg(soup):
	for img in soup.find_all('div', {'class':'col search_capsule'}):
		imgcon = img.find('img')
		imgsource = imgcon['src']
		imglist.append(imgsource)


def findtitle(soup):
	for title in soup.find_all('div', {'class':'responsive_search_name_combined'}):
		titlecon = title.find('div', {'class':'col search_name ellipsis'})
		gametitle = titlecon.find('span', {'class':'title'}).text
		titlelist.append(gametitle)
	

def getprices(soup):
	for price in soup.find_all('div', {'class':'col search_price discounted responsive_secondrow'}):
		text = price.text
		priceslist = text.split('$')
		oldprice = priceslist[1].strip()
		newprice = priceslist[2].strip()
		oldnewprices.append([oldprice, newprice])


findimg(soup)
findtitle(soup)
getprices(soup)

for index in range(len(imglist)):
	datalist.append({

		'title':titlelist[index],
		'img':imglist[index],
		'oldprice':oldnewprices[index][0],
		'newprice':oldnewprices[index][1]

		})


f = open('steam.html', 'w+')
f.write('<html>')
f.write('<h1 align="center"> BROWSE WHICH STEAM GAMES ARE ON SALE WITHOUT SEEING ALL OF STEAM\'S ADS </h1>')
f.write('<body bgcolor="#ff69b4">')

for game in datalist:
	f.write('<img src="{}" </img>'.format(game['img']))
	f.write('<p> <b>GAME TITLE:</b> {} <br> <b>OLD PRICE:</b> {} <br> <b>PRICE CURRENTLY:</b> {} <br>'.format(game['title'], game['oldprice'], game['newprice']))
	f.write('<br><br><br>')

f.write('</body>')
f.write('</html>')
f.close()








	



