from datetime import datetime

dd = "Fri Nov 09 2018 14:41:35 GMT+0800"
GMT_FORMAT = '%a %b %d %Y %H:%M:%S GMT+0800'
print(datetime.strptime(dd, GMT_FORMAT).date())


