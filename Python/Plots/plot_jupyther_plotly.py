#########  PLOTLY ON PYTHON  #########

# import plotly and set it offline
import plotly
import chart_studio.plotly as py
import plotly.graph_objs as go 
plotly.offline.init_notebook_mode(connected=True)

import datetime
from datetime import timedelta
DATE_FORMAT = "%m/%d/%y %H:%M:%S"

# Creation of rectangular shapes for higlight data
#   It creates the grey shapes of the events to show them on the chart
shapes=[]
for i in range(0, frameEV.shape[0]):
    shapes.append({
            'type': 'rect',
            'xref': 'x',
            'yref': 'paper',
            'x0': datetime.datetime.strptime(dataframe.iloc[i,0]+' '+dataframe.iloc[i,1], DATE_FORMAT),
            'y0': 0,
            'x1': datetime.datetime.strptime(dataframe.iloc[i,0]+' '+dataframe.iloc[i,2], DATE_FORMAT),
            'y1': 1,
            'fillcolor': '#000000',
            'opacity': 0.2,
            'line': {
                'width': 0,
            }
        })

# Creation of line-charts with data and shapes-->Shapes are rectangular to highlight some part of the data
#   The data used are the ones in the interval [s:e]
def plotData(data, shapes, message='Message for debug', s=None, e=None):
    print(message)
    dataG= []
    
    # Defining data to plot
    dataG.append(go.Scatter(y=value[s:e],
                    x=data["timestamps"][s:e],
                    yaxis='y2',
                    opacity=op,
                    name=key))

    layout = dict(
        title=message,        
        width=1000,
        height=450,
        xaxis=dict(
            rangeselector=dict(),
            rangeslider=dict()
        ),
        yaxis=dict(
            title='y-axis-title'
        ),
        yaxis2=dict(
            title='y2-axis-title',
            overlaying='y',
            side='right'
        ),
        shapes=shapes
    )
    fig = dict(data=dataG, layout=layout)
    plotly.offline.iplot(fig)


