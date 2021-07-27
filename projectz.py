import pandas as pd
import plotly.figure_factory as pf
import plotly.graph_objects as pg
import statistics
import csv
import random

df = pd.read_csv('mediumdatapro.csv')
data = df["id"].tolist()

fig = pf.create_distplot([data],[""],show_hist=False)

fig.show()

population_mean = statistics.mean(data)
stdev = statistics.stdev(data)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index= random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

mean_list = []
for i in range(0,100):
    set_of_means= random_set_of_mean(30)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
meanaftethis = statistics.mean(mean_list)
print(meanaftethis)
print(std_deviation)

first_std_deviation_cmon, first_std_deviation_dontend = mean-std_deviation, mean+std_deviation
second_std_deviation_cmon, second_std_deviation_dontend = mean-(2*std_deviation), mean+(2*std_deviation)
third_std_deviation_cmon, third_std_deviation_dontend = mean-(3*std_deviation), mean+(3*std_deviation)

fig = ff.create_distplot([data], ["Number"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_cmon, first_std_deviation_cmon], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_dontend, first_std_deviation_dontend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_deviation_cmon, second_std_deviation_cmon], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_dontend, second_std_deviation_dontend], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))


data_1_std_deviation = [result for result in data if result > first_std_deviation_cmon and result < first_std_deviation_dontend]
data_2_std_deviation = [result for result in data if result > second_std_deviation_cmon and result < second_std_deviation_dontend]
data_3_std_deviation = [result for result in data if result > third_std_deviation_cmon and result < third_std_deviation_dontend]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("Standard deviation of this data is {}".format(std_deviation))
print("{}% of data lies within 1 standard deviation".format(len(data_1_std_deviation)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(data_2_std_deviation)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(data_3_std_deviation)*100.0/len(data)))

sample_mean = statistics.mean(mean)
fig = ff.create_distplot(sample_mean, ["Sample Mean"], show_hist=False)

z_score = (sample_mean - mean)/std_deviation
print("The Z Score is:",z_score)

fig.show()