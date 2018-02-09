import plotly
# from plotly.graph_objs import Scatter, Layout
import pandas as pd
import numpy as np
import plotly.plotly as py
import plotly.graph_objs as go



# df = pd.read_csv('line_data.csv')
df = pd.read_csv('line_data.csv', skipinitialspace=True, delimiter=',', encoding="utf-8-sig")
df.head()



trace1 = go.Scatter(
                    x=df['Time'], y=df['RX Packet Rate'], # Data
                    mode='lines', name='RX Packets Name' # Additional options
                   )
trace2 = go.Scatter(
                    x=df['Time'], y=df['Avg RX Packet Rate'], # Data
                    mode='lines', name='Avg RX Packet Rate Name' # Additional options
                   )



layout = go.Layout(title='Simple Plot from csv data',
                   plot_bgcolor='rgb(230, 230,230)')

fig = go.Figure(data=[trace1,trace2], layout=layout)

# Plot data in the notebook
# py.iplot(fig, filename='simple-plot-from-csv')

plotly.offline.plot(
  {
    "data": [trace1,trace2],
    "layout": layout
  },
  auto_open=False,
  filename="test.html"
)


