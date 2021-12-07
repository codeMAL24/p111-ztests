import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random as r

df = pd.read_csv("data.csv")
data = df["id"].tolist()

mean = s.mean(data)
std = s.stdev(data)

print(f"This is the mean of the id: {mean}")
print(f"This is the std of the id: {std}")


def rsom(counter):
    dataSet = []
    for i in range(0,counter):
        ri = r.randint(0,len(data)-1)
        value = data[ri]
        dataSet.append(value)
    Smean = s.mean(dataSet)
    return Smean 

meanList = []
for i in range(0,1000):
    sm = rsom(100)
    meanList.append(sm)

mean = s.mean(meanList)
std = s.stdev(meanList)

print(f"This is the mean of the sample distribution: {mean}")
print(f"This is the std of the sample distribution: {std}")

fig = ff.create_distplot([meanList],["Student id"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
# fig.show()

#---------------------------------------------------------------------------------------------

std1s,std1e = mean - std, mean + std
std2s,std2e = mean - (2*std), mean + (2*std)
std3s,std3e = mean - (3*std), mean + (3*std)


df = pd.read_csv("data.csv")
data = df["url"].tolist()



meanS1 = s.mean(data)

fig = ff.create_distplot([meanList],["url"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
fig.add_trace(go.Scatter(x = [meanS1,meanS1],y = [0,0.17],mode = "lines",name = "mean of 1st intervention(ipad)"))
fig.add_trace(go.Scatter(x = [std1e,std1e],y = [0,0.17],mode = "lines",name = "1st std end"))
#fig.show()



df = pd.read_csv("data.csv")
data = df["title"].tolist()


meanS2 = s.mean(data)

fig = ff.create_distplot([meanList],["title"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
fig.add_trace(go.Scatter(x = [meanS2,meanS2],y = [0,0.17],mode = "lines",name = "mean of 2nd intervention(xtra classes))"))
fig.add_trace(go.Scatter(x = [std1e,std1e],y = [0,0.17],mode = "lines",name = "1st std end"))
fig.add_trace(go.Scatter(x = [std2e,std2e],y = [0,0.17],mode = "lines",name = "2nd std end"))
#fig.show()


df = pd.read_csv("data.csv")
data = df["subtitle"].tolist()


meanS3 = s.mean(data)

fig = ff.create_distplot([meanList],["subtitle"],show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean],y = [0,0.17],mode = "lines",name = "mean of sample"))
fig.add_trace(go.Scatter(x = [meanS3,meanS3],y = [0,0.17],mode = "lines",name = "mean of 3rd intervention(funSheet)"))
fig.add_trace(go.Scatter(x = [std1e,std1e],y = [0,0.17],mode = "lines",name = "1st std end"))
fig.add_trace(go.Scatter(x = [std2e,std2e],y = [0,0.17],mode = "lines",name = "2nd std end"))
fig.add_trace(go.Scatter(x = [std3e,std3e],y = [0,0.17],mode = "lines",name = "3rd std end"))

#fig.show()



zscore1 = (meanS1 - mean)/std
print(f"The zscore of the 1st intervention is {zscore1}")

zscore2 = (meanS2 - mean)/std
print(f"The zscore of the 2nd intervention is {zscore2}")

zscore3 = (meanS3 - mean)/std
print(f"The zscore of the 3rd intervention is {zscore3}")
 

