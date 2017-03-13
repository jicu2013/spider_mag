#!/usr/bin/env python
import sys
def usage():
    print  "/.torrent_parse.py [torrent file name]"
def torrent_parse(torrent_filename):
    fp=open(torrent_filename,"r")
    torrent_buf=fp.read()
    print '[+]torrent_buf:\n%s' % (torrent_buf)
    len_torrent_buf=len(torrent_buf)

    _begin=0
    _end=0
    idx=0
    _tmp_len=0
    _tmp_item=" "
    while 1:
        if(torrent_buf[idx].isdigit()):
            #string
            # 3:abcl43:
            print "\n[+]find string at:%d"%(idx)
            _begin=idx
            _end = torrent_buf.find(':',idx)
            if _end==-1:
                print 'format_error_found at %d: obj_item bad end' % (idx)
                break
            _tmp_len = int(torrent_buf[_begin:_end])
            _tmp_item = torrent_buf[_end + 1:_end + 1 + _tmp_len]
            print "   s:%s" % (_tmp_item)
            idx=idx+_tmp_len+2

        elif(torrent_buf[idx]=='i'):
            #integer
            #i1234e
            print "\n[+]find integer obj at:%d"%(idx)
            _begin = idx+1
            _end = torrent_buf.find('e', idx)
            if _end==-1:
                print 'format_error_found at %d: obj_item bad end' % (idx)
                break
            _tmp_item = torrent_buf[_begin:_end]
            _tmp_len = int(len(_tmp_item))
            print "   i:%s" % (_tmp_item)
            idx = idx + _tmp_len + 2

        elif (torrent_buf[idx] == 'l'):
            #list
            #l4:test5:abcdee
            print "\n[+]find list at:%d" % (idx)
            _res = []
            _begin = idx+1
            _end = torrent_buf.find(':', _begin)
            while torrent_buf[_begin] != 'e':
                _tmp_len = int(torrent_buf[_begin:_end])
                _tmp_item = torrent_buf[_end + 1:_end + 1 + _tmp_len]
                idx = idx + _tmp_len + 2 + len(str(_tmp_len))

                _res.append(_tmp_item)
                _begin = _end + 1 + _tmp_len
                _end = torrent_buf.find(':', _begin)
            print "   %s"%(str(_res))

        elif(torrent_buf[idx]=='d'):
            #dictionaries
            # for_exp: d4:path3:C:/8:filename8:test.txte {"path"="C:/","filename"="test.txt"}
            print "\n[+]find dictionaries at:%d" % (idx)
            idx+=1
            while torrent_buf[idx]!='e' and torrent_buf[idx].isdigit():
                len_pair_1=int(torrent_buf[idx])
                pair_1=torrent_buf[idx+2:idx+2+len_pair_1]

                len_pair_2 =int(torrent_buf[idx+2+len_pair_1])
                pair_2=torrent_buf[idx+4+len_pair_1:idx+4+len_pair_1+len_pair_2]
                print "\t{%s=%s}"%(pair_1,pair_2)
                idx=idx+len_pair_1+len_pair_2+4
                #print "char:%s idx:%s" % (torrent_buf[idx], str(idx))
        else:
            print "format_error_found at:%d\n" % (idx)
            idx+=1
        if idx>=len_torrent_buf-2:
            print "\n[-]end of torrent"
            break
    fp.close()

def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    torrent_parse(sys.argv[1])
if __name__ == "__main__":
    #main()
    torrent_parse("/home/qqq/Desktop/test.t")