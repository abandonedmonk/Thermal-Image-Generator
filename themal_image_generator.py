import plotly.graph_objs as go
from plotly.subplots import make_subplots
from numpy import random
import numpy as np
import os


# Wrote a function to generate data
def rand_num(val):
    # Set the size of the array
    rows = 7
    cols = 8

    # Generate a random array with values between 0 and 9
    random_array = random.randint(val, size=(rows, cols))

    # Mask some values as empty (None)
    empty_mask = random.choice([True, False], size=(rows, cols), p=[0.2, 0.8])
    array_with_empty = np.where(empty_mask, None, random_array)
    
    return array_with_empty

# The value can be changed as per the user's desire
data = rand_num(20)
print(data)

# Creating the heatmaps

# First type
fig = make_subplots(rows=2, cols=2, subplot_titles=('connectgaps = False',
                                                        'connectgaps = True'))

fig.add_trace(go.Contour(z=data, showscale=False, connectgaps=True), 1, 2)
fig.add_trace(go.Heatmap(z=data, showscale=False, zsmooth='best'), 2, 1)
fig.add_trace(go.Contour(z=data, showscale=False), 1, 1)
fig.add_trace(go.Heatmap(z=data, showscale=False, connectgaps=True, zsmooth='best'), 2, 2)

fig['layout']['yaxis1'].update(title='Contour map')
fig['layout']['yaxis3'].update(title='Heatmap')

# Second Type
fig2 = make_subplots(rows=1, cols=2,
                    subplot_titles=('Without Smoothing', 'With Smoothing'))

fig2.add_trace(go.Contour(z=data, line_smoothing=0), 1, 1)
fig2.add_trace(go.Contour(z=data, line_smoothing=0.85), 1, 2)

# Third Type
fig3 = go.Figure(data=go.Contour(z=data, contours_coloring = 'heatmap'))

# Displaying the Heatmaps
fig3.show()
fig2.show()
fig.show()