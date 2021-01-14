# -*- coding: utf-8 -*-
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pickle
from pickle import load
import numpy as np
import pandas
import dash

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']
app = dash.Dash(name="test", external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

with open ('../ib.pkl','rb') as file:
    data = load(file)


app.layout = html.Div(className="row justify-content-center", children= [

    html.Div(className="row justify-content-center", children=[
       


        html.Div(className="col-6",children=[
                html.H3(className="text-dark col-11 offset-1 mt-1", children="Formulaire USA à remplir :"),
                html.Hr(className="col-11 offset-1"),
                html.Div(className="p-5 ml-5 shadow",children=[
                html.Form([
                    
                     html.Div(className="form-group col-8",children=[
                        html.Label("Number of major derogatory reports", htmlFor="DEROG"),
                        dcc.Input(type="number",id="DEROG", className="form-control", placeholder="Enter the Number of major derogatory reports"),
                        
                     ]),
                     html.Div(className="form-group col-8",children=[
                        html.Label("Number of delinquent credit lines", htmlFor="DELINQ"),
                        dcc.Input(type="number",id="DELINQ", className="form-control", placeholder="Enter the Number of delinquent credit lines"),
                        
                     ]),
                     html.Div(className="form-group col-8",children=[
                        html.Label("Debt-to-income ratio", htmlFor="DEBTINC"),
                        dcc.Input(type="number",id="DEBTINC", className="form-control", placeholder="Debt-to-income ratio"),
                        
                     ]),
                     html.Div(className="form-group col-8",children=[
                        html.Label("Age of oldest trade line in months", htmlFor="CLAGE"),
                        dcc.Input(type="number",id="CLAGE", className="form-control", placeholder="Enter the Age of oldest trade line in months"),
                     ])
                  
                    
                  
                ], className="row"),
                html.Hr(),
                html.Button("valider", className="btn btn-success", id="action"),
                html.Div(className="alert alert-primary text-center mt-4", children="please enter data to test if u are a good clent :p ...", id="output_msg"),
                
            ])
        
         ])
         ,
         dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1], 'y': [93.1], 'type': 'bar', 'name': 'KNN'},
                {'x': [2], 'y': [84.01], 'type': 'bar', 'name': u'Random Forest'},
                {'x': [3], 'y': [91.298], 'type': 'bar', 'name': u'DecisionTree'},
                {'x': [4], 'y': [99.124], 'type': 'bar', 'name': u'Xgboost'},
            ],
            'layout': {
                'title': 'Score of Model'
            }
        }
    )        
    ])
]
)



@app.callback(Output("output_msg","children"),[Input("action","n_clicks")],[
    State("DEROG","value"),
    State("DELINQ","value"),
    State("DEBTINC","value"),
    State("CLAGE","value")
   
    ])


def predict_customer(inp,DEROG,DELINQ,DEBTINC,CLAGE):
    if inp is not None:
        df = np.array([DEROG,DELINQ,DEBTINC,CLAGE]).reshape(1,4)

        print(df.shape)
        
        df2=np.array([4,2,3,5]).reshape(1,4)
        print( df)
        print( data )
        print( data.predict(df)[0] )

        if  data.predict(df2)[0]==0:
            return "No,  bad client "
        else :
            return "Yes , good client"
    return "enter des données correctes "







app.run_server(debug = True,use_reloader=False)