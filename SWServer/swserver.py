import webapp2
import urllib2
import json
import re
import sys
from episode_info import EpisodeInfo
sys.path.append('beautifulsoup')
from bs4 import BeautifulSoup as BS

last_watched = EpisodeInfo(season_num=4, episode_num=6)

def setLastWatched():
	pass

def fetchPage(url):
	request = urllib2.Request(url, headers={'User-Agent':'Magic Browser'})
	response = urllib2.urlopen(request)
	return response.read()	

def fetchSeriesLink(url, name):
	page = fetchPage(url+'/showlist/')
	found = re.search('a href=(\".*?\").*'+name, page)
	if found:
		return url + found.group(1)[1:-1]

def fetchNewEpisodes(url):
	episodes_found = []
	page_lines = fetchPage(url).split('\n')
	pattern_ep = 'title=.*S(\d\d)E(\d\d)'
	patterns_props = ['720p', 'KILLERS']
	for i, line in enumerate(page_lines):
		found = re.search(pattern_ep, line)
		if found:
			for prop in patterns_props:
				if prop not in line:
					found = None
					break
		if found:
			num_s = int(found.group(1))
			num_e = int(found.group(2))
			global last_watched
			if num_s >= last_watched.info['season_num'] and \
			   num_e > last_watched.info['episode_num']:
				links_soup = BS('\n'.join(page_lines[i+1:i+5]))
				link = links_soup.find(attrs={'title': 'Download Mirror #1'})['href']
				if link:
					episode = EpisodeInfo()
					episode.info['season_num']=num_s
					episode.info['episode_num']=num_e
					episode.info['video_link']=link
					print episode
					episodes_found.append(episode)
			elif not episodes_found:
				return None
			else:
				# last_watched = episodes_found[-1]
				return episodes_found

class MainPage(webapp2.RequestHandler):
    def get(self):
        self.response.headers['Content-Type'] = 'application/json'
        resource = 'http://eztv.it'
        series_name = 'Game of Thrones'
        slink = fetchSeriesLink(resource, series_name)
        episodes = fetchNewEpisodes(slink)

        self.response.write(json.dumps([ep.toJSON() for ep in episodes]))

application = webapp2.WSGIApplication([('/', MainPage), ], debug=True)
