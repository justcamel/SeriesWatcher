import webapp2
import urllib2
import re

def fetchPage(url):
	request = urllib2.Request(url, headers={'User-Agent':'Magic Browser'})
	response = urllib2.urlopen(request)
	return response.read()	

def fetchSeriesLink(url, name):
	page = fetchPage(url+'/showlist/')
	found = re.search('a href=(\".*?\").*'+name, page)
	if found:
		return url + found.group(1)[1:-1]

def fetchTorrentLink(url, season, episode):
	page_lines = fetchPage(url).split('\n')
	s = str(season) if season > 9 else '0'+str(season)
	e = str(episode) if episode > 9 else '0'+str(episode)
	pattern = 'title=.*'+'S'+s+'E'+e
	for i, line in enumerate(page_lines):
		if re.search(pattern, line):
			found = re.search('a href=(\".*?\").*', page_lines[i+4])
			if found:
				return url + found.group(1)[1:-1]

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'text/plain'
        resource = 'http://eztv.it'
        series_name = 'Game of Thrones'
        season = 4
        episode = 7
        slink = fetchSeriesLink(resource, series_name)
        tlink = fetchTorrentLink(slink, season, episode)
        self.response.write(tlink)

application = webapp2.WSGIApplication([('/', MainPage), ], debug=True)
