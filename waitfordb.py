import MySQLdb

from time import sleep

dbhost='mysql'
dbuser='zhang'
dbpasswd='zhang'
dbname = 'YOLO'

while True:
    try:
        con = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=dbname)
        break
    except Exception as ex:
        print('mySQL not available - sleeping...\n')
        sleep(4)

print("mySQL seems to be there... might still be in installation... so let's wait some more")
sleep(4)

while True:
    try:
        con = MySQLdb.connect(host=dbhost, user=dbuser, passwd=dbpasswd, db=dbname)
        break
    except Exception as ex:
        print('mySQL not available - sleeping...\n')
        sleep(4)

    print("Finally... mySQL seems to be ready!")
