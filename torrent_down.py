#!/usr/bin/env python
import libtorrent as lt
import time
import os
import shutil
def exp1():
    down_dir = '//home//www//download'
    if os.path.exists(down_dir):
        shutil.rmtree(down_dir)
    os.makedirs(down_dir)
    ses = lt.session()
    ses.listen_on(6881, 6891)
    e = lt.bdecode(open("//home//www//Desktop//test1.torrent", 'rb').read())
    info = lt.torrent_info(e)
    #get file-info in torrent-stream
    info_hash = info.info_hash()
    name = info.name()
    total_size = info.total_size()
    #creation_date = info.creation_date()
    num_files = info.num_files()
    files = info.files()
    items = dict([(file.size,file.path) for file in files]).items()
    items.sort(reverse=True)
    '''
    files = os.path.split(items[0][1])[-1]+"$||$"+str(items[0][0])
    for i in items:
        files = files+"@||@"+os.path.split(i[1])[-1]+"$||$"+str(i[0])
    '''
    print "name: %s"%(name)
    print "total_size: %s MB"%(total_size/(1024*1024))
    print "num_files: %s"%(num_files)
    for i in items:
        print i[1]
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
    exp1()
if __name__ == "__main__":
    main()
