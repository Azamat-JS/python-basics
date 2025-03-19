# try:
#     getfile = open('index.py', 'r')
#     getfile.write('First text')
# except IOError:
#     print('unable to open')
# except:
#     print('some other error')


try:
    getfile = open('index.py', 'r')
    getfile.write('First text')
except IOError:
    print('unable to open')
else:
    print('the file was written successfully')
finally:
    getfile.close()
    print('file is now closed')