import plotly.graph_objs as go
from plotly.subplots import make_subplots
from numpy import random
import numpy as np
import os
import plotly.offline as po

'''
    Purpose:
    ---
    This function generates a random array with some empty (None) values based on the specified range.
    The generated array is used to create thermal heatmaps
    
    Input Arguments:
    ---
    `val`: An integer representing the upper limit for the random values in the array
    
    Returns:
    ---
    `array_with_empty`: A NumPy array with random values and some empty (None) elements
    
    Example call:
    ---
    data = rand_num(10)
'''

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

'''
    Purpose:
    ---
    This function creates a 2x2 subplot of thermal heatmaps using the provided data.
    It uses Plotly to generate contour maps and heatmaps with different settings.

    Input Arguments:
    ---
    `data`: A NumPy array containing the data for generating thermal heatmaps.

    Returns:
    ---
    `fig`: A Plotly figure containing the 2x2 subplot of thermal heatmaps.

    Example call:
    ---
    thermal_image = create_heatmap(data)
'''

def create_heatmap(data):
    fig = make_subplots(rows=2, cols=2, subplot_titles=('connectgaps = False',
                                                            'connectgaps = True'))

    fig.add_trace(go.Contour(z=data, showscale=False, connectgaps=True, line_smoothing=0.85), 1, 2)
    fig.add_trace(go.Heatmap(z=data, showscale=False, zsmooth='best'), 2, 1)
    fig.add_trace(go.Contour(z=data, showscale=False, line_smoothing=0.85), 1, 1)
    fig.add_trace(go.Heatmap(z=data, showscale=False, connectgaps=True, zsmooth='best'), 2, 2)

    fig['layout']['yaxis1'].update(title='Contour map')
    fig['layout']['yaxis3'].update(title='Heatmap')
    
    return fig

'''
    Purpose:
    ---
    This function saves a Plotly image to the specified directory with the given filename.

    Input Arguments:
    ---
    `image`: The Plotly figure or graph to be saved as an image.
    `directory`: The directory path where the image will be saved.
    `filename`: The name of the image file.

    Returns:
    ---
    None
    Just saves the image

    Example call:
    ---
    save_image(thermal_image, output_directory, "thermal_image_0")
'''

def save_image(image, directory, filename):
    if not os.path.exists(directory):
        os.makedirs(directory)
    path = os.path.join(directory, filename)
    po.plot(image, filename=path)

if __name__ == "__main__":
    ran = input("How many heatmaps do you want: \n ")
    ran = int(ran)
    
    for i in range (ran):
        val = input("How much range do you want (0 to ?): ")
        data = rand_num(val)
        output_directory = "Images"
        thermal_image = create_heatmap(data)
        save_image(thermal_image, output_directory, f"thermal_image_{i}")
