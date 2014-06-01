__author__ = 'jc'

import sys
import urllib2
import libtorrent as lt
import time
import os
import json
from episode_info import EpisodeInfo

server_url = 'http://127.0.0.1:8080'


def new_episode_uploaded():
    response = urllib2.urlopen(server_url)
    ep_json = json.loads(response.read())[0]
    data = json.loads(ep_json)
    ep_info = EpisodeInfo(video_link=data['video_link'])
    return ep_info


def download_torrent_file(tf_url, tf_path):
    res = urllib2.urlopen(tf_url)
    tf = open(tf_path, 'w')
    tf.write(res.read())
    tf.close()


def download_episode(torrent_file_path, episode_path):
    session = lt.session()
    session.listen_on(6881, 6891)
    decoded = lt.bdecode(open(torrent_file_path, 'rb').read())
    tf_info = lt.torrent_info(decoded)
    ses_handler = session.add_torrent(tf_info, episode_path)

    states = ['Queued', 'Checking', 'Downloading metadata', 'Downloading', \
              'Finished', 'Seeding', 'Allocating', 'Checking fastresume']

    while not ses_handler.is_seed():
        status = ses_handler.status()
        state = states[status.state]
        progress = '%.2f%%' % (status.progress * 100)
        down_rate = '%.1f kb/s' % (status.download_rate / 1000)
        peers = status.num_peers
        print state+':', progress, '( down:', down_rate, '| peers:', peers, ')'
        time.sleep(1)
        os.system('clear')


def main():
    new_episode = None
    while True:
        new_episode = new_episode_uploaded()
        if new_episode:
            break

        time.sleep(60)

    tf_path = 'episode.torrent'
    download_torrent_file(new_episode.info['video_link'], tf_path)

    out_path = 'episode.mkv'
    download_episode(tf_path, out_path)

    pass


if __name__ == '__main__':
    sys.exit(main())
