import json

class EpisodeInfo():
	info = {}

	def toJSON(self):
		if not self.info.items():
			return json.dumps({'not_found': 'true'})
		return json.dumps(self.info)

	def fromJSON(self, json_data):
		pass

	def __init__(self, series_name=None, season_num=None, \
					   episode_num=None, episode_name=None, \
					   release_date=None, video_link=None, \
					   subtitles_link=None):
		self.info['series_name'] = series_name
		self.info['season_num'] = season_num
		self.info['episode_num'] = episode_num
		self.info['episode_name'] = episode_name
		self.info['release_date'] = release_date
		self.info['video_link'] = video_link
		self.info['subtitles_link'] = subtitles_link

