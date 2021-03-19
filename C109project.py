import plotly.express as px
import statistics
import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv



df = pd.read_csv("StudentsPerformance.csv")
ws = df["writing score"].to_list()
math = df["math score"].to_list()

mean_w = statistics.mean(ws)
mean_m = statistics.mean(math)
median_w = statistics.median(ws)
median_m = statistics.median(math)
mode_w = statistics.mode(ws)
mode_m = statistics.mode(math)
std_deviation_w = statistics.stdev(ws)
std_deviation_m = statistics.stdev(math)
print(mean_m ,mean_w , median_m ,median_w , mode_m ,mode_w , std_deviation_w, std_deviation_m)

sd1 = mean_m - std_deviation_m
sd_1 = mean_w - std_deviation_w
sd1_1 = mean_m + std_deviation_m
sd_11 = mean_w + std_deviation_w

data_count = 0

for item in math :
    if (item >= sd1 and item <= sd1_1):
        data_count = data_count + 1

per = (data_count * 100)/len(math)
print(per)

for item in ws :
    if (item >= sd_1 and item <= sd_11):
        data_count = data_count + 1

per = (data_count * 100)/len(math)
print(per)

sd2 = mean_m - 2 * std_deviation_m
sd_2 = mean_w - 2 * std_deviation_w
sd2_2 = mean_m + 2 * std_deviation_m
sd_22 = mean_w + 2 * std_deviation_w

data_count = 0

for item in math :
    if (item >= sd2 and item <= sd2_2):
        data_count = data_count + 1

per = (data_count * 100)/len(math)
print(per)

for item in ws :
    if (item >= sd_2 and item <= sd_22):
        data_count = data_count + 1

per = (data_count * 100)/len(ws)
print(per)

sd3 = mean_m - 3 * std_deviation_m
sd_3 = mean_w - 3 * std_deviation_w
sd3_3 = mean_m + 3 * std_deviation_m
sd_33 = mean_w + 3 * std_deviation_w

data_count = 0

for item in math :
    if (item >= sd3 and item <= sd3_3):
        data_count = data_count + 1

per = (data_count * 100)/len(math)
print(per)

for item in ws :
    if (item >= sd_3 and item <= sd_33):
        data_count = data_count + 1

per = (data_count * 100)/len(math)
print(per)


#fig = px.bar(x=sum,y=count)
fig = ff.create_distplot([sum],["result"])
fig.add_trace(go.Scatter(x=[mean_m, mean_m], y=[0, 0.17], mode="lines", name="MEAN1"))
fig.add_trace(go.Scatter(x=[mean_w, mean_w], y=[0, 0.17], mode="lines", name="MEAN2"))
fig.add_trace(go.Scatter(x=[sd1, sd1], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[sd_1, sd_1], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION_1"))
fig.add_trace(go.Scatter(x=[sd1_1, sd1_1], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[sd_11, sd_11], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION_1"))
fig.add_trace(go.Scatter(x=[sd2, sd2], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[sd_2, sd_2], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION_2"))
fig.add_trace(go.Scatter(x=[sd2_2, sd2_2], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[sd_22, sd_22], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION_2"))
fig.add_trace(go.Scatter(x=[sd3, sd3], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[sd_3, sd_3], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION_3"))
fig.add_trace(go.Scatter(x=[sd3_3, sd3_3], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 3"))
fig.add_trace(go.Scatter(x=[sd_33, sd_33], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION_3"))
fig.show()
