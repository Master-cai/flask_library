from datetime import datetime, timedelta, date

from faker import Faker

faker = Faker()
time = faker.date_between(start_date='-100d', end_date='today')
print(time)
delte = timedelta(days=60)
# print(time + delte)
print(faker.date_between(start_date='-100d', end_date=time+delte))
print(date.today())