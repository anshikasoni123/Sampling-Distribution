import random
import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()

def random_sets_of_mean(counter):
    dataset = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    fig = ff.create_distplot([df],['READING TIME'],show_hist=False)
    fig.add_trace(go.Scatter(x=[mean,mean],y=[0,1],mode='lines',name='MEAN'))
    fig.show()

def setup():
    mean_list = []
    for i in range(0,100):
        sets_of_mean = random_sets_of_mean(30)
        mean_list.append(sets_of_mean)

    show_fig(mean_list)
    mean = statistics.mean(mean_list)
    print('Sampling Mean is :- ',mean)

setup()

population_mean = statistics.mean(data)
print('Population Mean is :- ',population_mean)
