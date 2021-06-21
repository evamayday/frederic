import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()
from mysite.models import Post

with open("K_traffic.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for i,row in enumerate(rows):
		if i == 0:
			continue
		print(row[0], row[1], row[2], row[3])
		newdata = Post(
			K_time=str(row[0]),
			K_location=str(row[1]),
			K_death=str(row[2]),
			K_injure=str(row[3])
			)

		newdata.save()
	