import matplotlib.pyplot as plt
import csv

region_dict = {"EU":[], "US":[]}
for region in region_dict:
    file = open(region, "r")
    reader = csv.reader(file)
    region_dict[region] = next(reader)
    file.close()

print(region_dict)

plt.xlabel("ELO")
plt.ylabel("Frequency")
plt.title("ELO Distribution in US and EU")

plt.hist((region_dict["EU"], region_dict["US"]), 50)


plt.show()