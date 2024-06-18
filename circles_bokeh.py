import pandas as pd
from bokeh.io import show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.layouts import column

dataset = pd.read_csv('dataset.csv', parse_dates=['date'])
states = (dataset[(dataset['location'] == 'New York') | (dataset['location'] == 'Texas')])

states = states[states['date'] <= '2022-04-29']

new_york_data = states[states['location'] == 'New York']
texas_data = states[states['location'] == 'Texas']

new_york_cds = ColumnDataSource(new_york_data)
texas_cds = ColumnDataSource(texas_data)

TOOLS = "box_select,lasso_select,reset,help"

fig = figure(tools=TOOLS, x_axis_type='datetime',
             height=300, width=600,
             title='Fully Vaccinated per 100 People',
             x_axis_label='Time', y_axis_label='Fully Vaccinated per 100 People')

fig.circle('date', 'people_fully_vaccinated_per_hundred', size=3, color='red',
         legend_label='Texas', source=texas_cds)
fig.circle('date', 'people_fully_vaccinated_per_hundred', size=3, color='blue',
         legend_label='New York', source=new_york_cds)

fig.legend.location = 'top_left'

fig1 = figure(tools=TOOLS, x_axis_type='datetime',
             height=300, width=600,
             title='Death Toll per 10,000 People',
             x_axis_label='Time', y_axis_label='Death Toll per 10,000 People')

fig1.circle('date', 'death_per_10Kpeople', size=3, color='red',
         legend_label='Texas', source=texas_cds)
fig1.circle('date', 'death_per_10Kpeople', size=3, color='blue',
         legend_label='New York', source=new_york_cds)
fig1.legend.location = 'top_left'

show(column(fig, fig1))
