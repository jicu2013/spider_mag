#!/usr/bin/env python
import libtorrent as lt
import time
import os
import shutil

def exp1():
    ses = lt.session()
    ses.listen_on(6881, 6891)
    down_dir = '//home//qqq//download'
    if os.path.exists(down_dir):
        shutil.rmtree(down_dir)
    os.makedirs(down_dir)

    params = {
        'save_path': '//home//qqq//download',
        'storage_mode': lt.storage_mode_t(2),
        'paused': False,
        'auto_managed': True,
        'duplicate_is_error': True}
    link = "magnet:?xt=urn:btih:6e5bbd0399a401c1316760ed13bcc76712467d5a&dn=%E7%97%85%E6%AF%92%E5%85%A5%E4%BE%B5.Pandemic.2016.720p.WEB-DL.DD5.1.H264.Chs%2BEng-homefei"
    handle = lt.add_magnet_uri(ses, link, params)
    ses.start_dht()

    print 'downloading metadata...'
    while (not handle.has_metadata()):
        print 'sleep 3 secs...'
        time.sleep(3)
    print 'got metadata, starting torrent download...'
    while (handle.status().state != lt.torrent_status.seeding):
        s = handle.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                     'downloading', 'finished', 'seeding', 'allocating']
        print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s %.3' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
               s.num_peers, state_str[s.state], s.total_download / 1000000)
        time.sleep(5)

def main():
    exp1()

if __name__ == "__main__":
    main()
