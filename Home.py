# -*- coding: utf-8 -*-
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
import dash
import base64

from server import server
from german import app 





external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']
app = dash.Dash(name="test", external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

image_filename = 'C:/Users/marie/Desktop/m.png' # replace with your own image
encoded_image = base64.b64encode(open(image_filename, 'rb').read())


app.layout = html.Div(className="row justify-content-center", children= [
                html.H3(className="text-dark col-11 offset-1 mt-1", children="Bienvenue"),
    html.Div(className="row justify-content-center", children=[
       


        html.Div(className="col-6",children=[
                html.Hr(className="col-11 offset-1"),
                html.Div(className="p-5 ml-5 shadow",children=[
                html.Form([
                    
                           html.Img(src='data:image/png;base64,{}'.format(encoded_image))

                 
                  
                         ], className="row"),
                html.Hr(),
                dcc.Link( html.Button('Rediriger vers la banque de  "Allemagne" '), href='https://github.com/czbiohub/singlecell-dash/issues/new'),
                                html.Hr(),
html.A(html.Button('Submit feedback!', className='three columns'),
    href='/german/'),
                html.Button("valider", className="btn btn-success", id="action"),
                
                 ])
        
        ])
                 
    ])










]
)


app.run_server(debug = True,use_reloader=False)