import urllib2
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt 

def scraper(day, month, year):

	home=[]
	road=[]
	for y in year:
		for m in month:
			for d in  day:
				cbballref = "https://www.sports-reference.com/cbb/boxscores/index.cgi?month="+str(month)+"&day="+str(day)+"&year=2017"
				page=urllib2.urlopen(cbballref)
				soup = BeautifulSoup(page, "html.parser")
				box= soup.find_all('table', class_='teams')
				print "day: " +str(day) + "   month: " + str(month) +"length of box: "+ str(len(box)) 
				for row in  box:
					cells = row.findAll('td',class_="right")
					road.append(str(cells[0].find(text=True)))
					home.append(str(cells[2].find(text=True)))
	intensity = [
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0],	
		[0,0,0,0,0,0,0,0,0,0]	
	]
	if len(home) != len(road):
		return False
	
	home = home *5
	road = road *5	
	for i in range(len(home)):
		home[i] = int(home[i][-1])
		road[i] = int(road[i][-1])
		intensity[road[i]][home[i]] += 1
	
	return intensity, home, road

def heatmap(intensiy, home, road):	
	x = [0,1,2,3,4,5,6,7,8,9]
	y = [0,1,2,3,4,5,6,7,8,9]
	x,y = np.meshgrid(x,y)
	extent=myplot(home,road, nb=16)
	ax2.imshow(heat, extent=extent, origin='lower', aspect='auto')	

#	intensity = np.array(intensity)
#	heatmap, xedges, yedges = np. histogram2d(home, road, bins=None)
#	extent = [xedges[0], xedges[1], yedges[0], yedges[-1]]
#	plt.clf()
#	plt.imshow(heatmap.T,extent=extent, origin='lower')
	plt.show()
	
#	plt.pcolormesh(x,y,intensity)
#	plt.colorbar()
#	plt.show()

def main():
	intensity, home, road = scraper([16-20],[3],[2017])
	heatmap(intensity, home, road)
	
#get request year, day month

main()
