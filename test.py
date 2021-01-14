import pickle
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pickle
from pickle import load
from dash.dependencies import Input, Output
import numpy as np
import pandas
external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']
app = dash.Dash(name="test", external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True
with open('../knn.pkl','rb') as f:
    x= pickle.load(f)

print(x)

df=np.array([4,2,3,5]).reshape(1,4)
print(df)
print(x.predict(df)[0])



app.run_server(debug=True)