#!/usr/bin/env python
import libtorrent as lt
import time
import os
import shutil

def exp():

    down_dir = '//home//www//download'
    if os.path.exists(down_dir):
        shutil.rmtree(down_dir)
    os.makedirs(down_dir)


    ses = lt.session()
    ses.listen_on(6881, 6891)
    e = lt.bdecode(open("//home//www//Desktop//test1.torrent", 'rb').read())
    info = lt.torrent_info(e)
    h = ses.add_torrent(info, down_dir)
    while (not h.is_seed()):
        s = h.status()
        state_str = ['queued', 'checking', 'downloading metadata', \
                     'downloading', 'finished', 'seeding', 'allocating', 'checking fastresume']
        print s.download_rate
        print '%.2f%% complete (down: %.1f kb/s up: %.1f kB/s peers: %d) %s' % \
              (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000, \
               s.num_peers, state_str[s.state])

        time.sleep(1)



def main():
    print " "
    exp()


if __name__ == "__main__":
    main()
