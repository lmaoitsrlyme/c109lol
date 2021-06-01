import statistics
import pandas as pd
import csv

df = pd.read_csv("student.csv")
readlist = df["reading score"].to_list()
mean = statistics.mean(readlist)
median = statistics.median(readlist)
mode = statistics.mode(readlist)

print("mean of the data is ", mean)
print("median of the data is ", median)
print("mode of the data is ", mode)

sd = statistics.stdev(readlist)
firstsd, firstsde = mean - sd, mean + sd
secondsd, secondsde = mean - (2*sd), mean + (2 * sd)
thirdsd, thirdsde   = mean - (3*sd), mean + (3 * sd)

print("Standard Deviation of this data is",sd)

sd1 = [result for result in readlist if result> firstsd and result< firstsde]
sd2 = [result for result in readlist if result> secondsd and result< secondsde]
sd3 = [result for result in readlist if result> thirdsd and result< thirdsde]

print("{}% Of data lies between 1 deviation".format(len(sd1) * 100 / len(readlist)))
print("{}% Of data lies between 2 deviations".format(len(sd2) * 100 / len(readlist)))
print("{}% Of data lies between 3 deviations".format(len(sd3) * 100 / len(readlist)))

