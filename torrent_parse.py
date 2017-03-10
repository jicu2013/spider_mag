#!/usr/bin/env python
import sys
def usage():
    print  "/.torrent_parse.py [torrent file name]"
def torrent_parse(torrent_filename):
    fp=open(torrent_filename,"r")
    torrent_buf=fp.read()
    len_torrent_buf=len(torrent_buf)
    idx=0
    while 1:
        if( (torrent_buf[idx].isdigit()   and \
             torrent_buf[idx+1]==':')     or \

            (torrent_buf[idx].isdigit()   and \
             torrent_buf[idx+1].isdigit() and \
             torrent_buf[idx+2].isdigit() and \
             torrent_buf[idx+3]==':' )    or \

            (torrent_buf[idx].isdigit()   and \
             torrent_buf[idx+1].isdigit() and \
             torrent_buf[idx+2].isdigit() and \
             torrent_buf[idx+3].isdigit() and \
             torrent_buf[idx+4] == ':')

            (torrent_buf[idx].isdigit()   and \
             torrent_buf[idx+1].isdigit() and \
             torrent_buf[idx+2].isdigit() and \
             torrent_buf[idx+3].isdigit() and \
             torrent_buf[idx+4].isdigit() and \
             torrent_buf[idx+5] == ':')
            ):
            #string
            str_content = torrent_buf[idx+2:idx+2+int(torrent_buf[idx])]
            print("string:%d,content:%s"%(int(torrent_buf[idx]),str_content))
            idx=idx+int(torrent_buf[idx])+2

        elif(torrent_buf[idx]=='i' and \
             torrent_buf[idx+1]==':'):



            print "integer"
            idx+=2
            _start=idx
            while torrent_buf[idx]!='e':
                idx+=1
            _end=idx
            print torrent_buf[_start:_end]
            idx+=1

        elif(torrent_buf[idx]=='d' and \
             torrent_buf[idx+1].isdigit() and \
             torrent_buf[idx+2]==':'):
            #dictionaries
            # for_exp: d4:path3:C:/8:filename8:test.txte {"path"="C:/","filename"="test.txt"}
            print "dictionaries"
            idx+=1
            while torrent_buf[idx]!='e' and torrent_buf[idx].isdigit():
                len_pair_1=int(torrent_buf[idx])
                pair_1=torrent_buf[idx+2:idx+2+len_pair_1]

                len_pair_2 =int(torrent_buf[idx+2+len_pair_1])
                pair_2=torrent_buf[idx+4+len_pair_1:idx+4+len_pair_1+len_pair_2]
                print "\t{%s=%s}"%(pair_1,pair_2)
                idx=idx+len_pair_1+len_pair_2+4
                print "char:%s idx:%s" % (torrent_buf[idx], str(idx))

        elif (torrent_buf[idx] == 'l' and \
              torrent_buf[idx + 1].isdigit() and \
              torrent_buf[idx + 2] == ':'):
            print "list"
            while torrent_buf[idx]!='e' and torrent_buf[idx].isdigit():
                len_pair_1=int(torrent_buf[idx])
                pair_1=torrent_buf[idx+2:idx+2+len_pair_1]

                len_pair_2 =int(torrent_buf[idx+2+len_pair_1])
                pair_2=torrent_buf[idx+4+len_pair_1:idx+4+len_pair_1+len_pair_2]
                print "\t{%s=%s}"%(pair_1,pair_2)
                idx=idx+len_pair_1+len_pair_2+4
                print "char:%s idx:%s" % (torrent_buf[idx], str(idx))

        else:
            print "format_error_found"
            idx+=1
        if idx>=len_torrent_buf-2:
            print "end of torrent"
            break
    fp.close()
def main():
    if len(sys.argv) != 2:
        usage()
        sys.exit(0)
    torrent_parse(sys.argv[1])
if __name__ == "__main__":
    #main()
    torrent_parse("/home/qqq/Desktop/test.torrent")