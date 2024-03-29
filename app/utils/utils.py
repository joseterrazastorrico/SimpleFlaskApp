import logging
import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def make_picture(training_data_filename, model, new_inp_np_arr, output_file):
    data = pd.read_pickle(training_data_filename)
    ages = data['Age']
    data = data[ages > 0]
    ages = data['Age']
    heights = data['Height']
    x_new = np.array(list(range(19))).reshape(19, 1)
    preds = model.predict(x_new)

    fig = px.scatter(x=ages, y=heights, title="Height vs Age of People", labels={'x': 'Age (years)',
                                                                                 'y': 'Height (inches)'})

    fig.add_trace(go.Scatter(x=x_new.reshape(
        19), y=preds, mode='lines', name='Model'))

    new_preds = model.predict(new_inp_np_arr)

    fig.add_trace(go.Scatter(x=new_inp_np_arr.reshape(len(new_inp_np_arr)), y=new_preds, name='New Outputs',
                             mode='markers', marker=dict(color='purple', size=20, line=dict(color='purple', width=2))))

    fig.write_image(output_file, width=800, engine='kaleido')
    fig.show()


def floats_string_to_np_arr(floats_str):
    """_summary_

    Args:
        floats_str (_type_): _description_
    """
    def is_float(string):
        try:
            float(string)
            return True
        except Exception as e:
            logging.error(e)
            return False

    floats = np.array([float(x) for x in floats_str.split(',') if is_float(x)])
    return floats.reshape(len(floats), 1)
