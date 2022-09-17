from settings import FILES_PATH
import os
import datetime
date = '2019-03-21 00:30:05.823905'
files = os.listdir(FILES_PATH)
result = []
a = '2019-03-21'
for file in files:
    file_stat = os.stat(os.path.join(FILES_PATH, file))
    print(datetime.datetime.fromtimestamp(file_stat.st_ctime).date())
    b = a.split('-')
    print(datetime.date(b))


    # result.append(
    #     {
    #         'name': file,
    #         'ctime': datetime.utcfromtimestamp(file_stat.st_ctime),
    #         'mtime': datetime.utcfromtimestamp(file_stat.st_mtime)
    #     })
