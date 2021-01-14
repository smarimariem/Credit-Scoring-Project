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
import plotly.graph_objs as go
import webbrowser

import dash
from server import server
#app = dash.Dash(name='german', sharing=True, server=server, url_base_pathname='/german')

external_stylesheets = ['https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css']
app = dash.Dash(name="test", external_stylesheets=external_stylesheets)
app.config.suppress_callback_exceptions = True

with open ('../german_knn3.pkl','rb') as file:
    data1 = load(file)

with open ('../mariemtest.pkl','rb') as file:
    data2 = load(file)
with open ('../german_CRT2.pkl','rb') as file:
    data3 = load(file)
with open ('../german_NB2.pkl','rb') as file:
    data4 = load(file)
with open ('../german_RF2.pkl','rb') as file:
    data5 = load(file)
with open ('../german_SVM2.pkl','rb') as file:
    data6 = load(file)
with open ('../german_XgBoost2.pkl','rb') as file:
    data7 = load(file)
    
with open ('../roc.pkl','rb') as file:
    d = load(file)

app.layout = html.Div(className="row justify-content-center", children= [

    html.Div(className="row justify-content-center", children=[
       


        html.Div(className="col-6",children=[
                html.H3(className="text-dark col-11 offset-1 mt-1", children="Formulaire d'un client de l'Allemagne à remplir :"),
                html.Hr(className="col-11 offset-1"),
                html.Div(className="p-5 ml-5 shadow",children=[
                html.Form([
                    
  html.Div(className="form-group col-8",children=[
                        html.Label("Credit Amount", htmlFor="id_credit"),
                        dcc.Input(type="number",id="id_credit", className="form-control", placeholder="Enter the credit amount"),
                        
                    ]),
                     html.Div(className="form-group col-8",children=[
                        html.Label("Duration in month", htmlFor="id_duration"),
                        dcc.Input(type="number",id="id_duration", className="form-control", placeholder="Enter the duration in month"),
                        
                    ]),
                     html.Div(className="form-group col-8",children=[
                        html.Label("Age in years", htmlFor="id_age"),
                        dcc.Input(type="number",id="id_age", className="form-control", placeholder="Enter your age in years"),
                        
                    ]),
                     html.Div(className="form-group col-8",children=[
                        html.Label("no checking account", htmlFor="id_cheking"),
                        dcc.Input(type="number",id="id_cheking", className="form-control", placeholder="Enter 1 if count is checking"),
                        
                    ]),
                     html.Div(className="form-group col-8",children=[
                        html.Label("installement rate of in percentage of disposable income", htmlFor="id_installement"),
                        dcc.Input(type="number",id="id_installement", className="form-control", placeholder="Enter your installement rate of in percentage of disposable income"),
                        ])
                  
                    
                   
                  
                ], className="row"),
                html.Hr(),
                html.Button("valider", className="btn btn-success", id="action"),
                html.Div(className="alert alert-primary text-center mt-4", children="please enter data to test if u are a good clent :p ...", id="output_msg"),
                
            ])
        
        ]),
      

     dcc.Graph(id='score_model',
                           figure=go.Figure(
                               data=[go.Pie(labels=['KNN', 'Logistic Regression',"CRT","RF","NB","SVM","XGBOOST"],
                                            values=[
                                                data1[1],data2[1],data3[1],data5[1],data4[1],data6[1],data7[1]
                                                ])],
                               layout=go.Layout(
                                   title='Score of Model')
                           )),

    dcc.Graph(
            id='roc',
                figure={
                    'data': [


                        {'x': d[0], 'y': d[1], 'type': 'scatter', 'name' :'XGBOOST  (area = %0.2f)'%d[14]},
                        {'x': d[2], 'y': d[3], 'type': 'scatter', 'name': 'CRT  (area = %0.2f)'%d[15]},
                        {'x': d[4], 'y': d[5], 'type': 'scatter', 'name': 'RF  (area = %0.2f)'%d[16]},
                        {'x': [0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1], 'y':[0,0.05,0.1,0.15,0.2,0.25,0.3,0.35,0.4,0.45,0.5,0.55,0.6,0.65,0.7,0.75,0.8,0.85,0.9,0.95,1], 'type': 'scatter' ,'color' : 'red' ,'mode':'markers', 'name': ' ' },
                        {'x': d[6], 'y': d[7], 'type': 'scatter', 'name': 'KNN (area = %0.2f)'%d[17]},
                        {'x': d[8], 'y': d[9], 'type': 'scatter', 'name': 'SVM  (area = %0.2f)'%d[18]},
                        {'x': d[10], 'y': d[11], 'type': 'scatter', 'name': 'NB (area = %0.2f)'%d[19]},
                        {'x': d[12], 'y': d[13], 'type': 'scatter', 'name': 'LR (area = %0.2f)'%d[20]},


                        
                    ],
                    'layout': {
                        'title': 'Classifiers ROC curves',
                        'xaxis':{'title':'True Positive Rate' },
                        'yaxis':{'title':'False Positive Rate' }
                               }
    

                } 
                
                     ),
        dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': ['Bad'], 'y': [300], 'type': 'bar', 'name': 'Bad'},
                {'x': ['Good'], 'y': [700], 'type': 'bar', 'name': u'Good'},
                
            ],
            'layout': {
                'title': 'Data Visualization'
            }
        }
    )    
  

    
                 
    ])
]
)



@app.callback(Output("output_msg","children"),[Input("action","n_clicks")],[
    State("id_credit","value"),
    State("id_duration","value"),
    State("id_age","value"),
    State("id_installement","value"),
    State("id_cheking","value")
   
    ])


def predict_customer(inp,id_credit,id_duration,id_age,id_installement,id_cheking):
    if inp is not None:
        df = np.array([id_credit,id_duration,id_age,id_installement,id_cheking]).reshape(1,5)

        print(df.shape)
        print( df)
        print( data1 )
        print( data1.predict(df)[0] )
        
        if  data1.predict(df)[0]==0:
            return "No,  bad client "
        else :
            return "Yes , good client"
    return "enter des données correctes "


f = open('home.html','w')

message = """<html>
<head>
    <link href="css/styles.css" rel="stylesheet" />

</head>
<body><div id="layoutSidenav_content">
        <main>


            <div class="sb-page-header pb-10 sb-page-header-dark bg-gradient-primary-to-secondary">
                <div class="container-fluid">
                    <div class="sb-page-header-content py-5">
                        <h1 class="sb-page-header-title">
                            <div class="sb-page-header-icon"><i data-feather="activity"></i></div>
                            <span>Bank Scoring</span>
                        </h1>
                        <div class="sb-page-header-subtitle">Dashboard</div>
                    </div>
                </div>
            </div>
            <div class="container-fluid mt-n10">
                <div class="row">
                    <div class="col-md-6">
                        <div class="card mb-4">
                            <div class="card-header">Area Chart Example</div>
                            <div class="card-body">
                                <div class="chart-area"><canvas id="myAreaChart" width="100%" height="30"></canvas></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-md-6">
                        <div class="card mb-4">
                            <div class="card-header">Bar Chart Example</div>
                            <div class="card-body">
                                <div class="chart-bar"><canvas id="myBarChart" width="100%" height="30"></canvas></div>
                            </div>
                        </div>
                    </div>
                </div>
                <div class="row">
                    <div class="col-xl-3 col-md-6">
                        <div class="card bg-primary text-white mb-4">
                            <div class="card-body">German Bank</div>
                            <div class="card-footer d-flex align-items-center justify-content-between">
                                <a class="small text-white stretched-link" href="#">View Details</a>
                                <div class="small text-white"><i class="fas fa-angle-right"></i></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-3 col-md-6">
                        <div class="card bg-warning text-white mb-4">
                            <div class="card-body">USA Bank</div>
                            <div class="card-footer d-flex align-items-center justify-content-between">
                                <a class="small text-white stretched-link" href="#">View Details</a>
                                <div class="small text-white"><i class="fas fa-angle-right"></i></div>
                            </div>
                        </div>
                    </div>
                    <div class="col-xl-3 col-md-6">
                        <div class="card bg-success text-white mb-4">
                            <div class="card-body">Taiwan Bank</div>
                            <div class="card-footer d-flex align-items-center justify-content-between">
                                <a class="small text-white stretched-link" href="#">View Details</a>
                                <div class="small text-white"><i class="fas fa-angle-right"></i></div>
                            </div>
                        </div>
                    </div>
                    </div>
            </main>
            </div></body>
</html>"""

f.write(message)
f.close()

#Change path to reflect file location
filename = 'C:/Users/marie/Desktop/Version_Marwa2/dash/' + 'home.html'
webbrowser.open_new_tab(filename)






app.run_server(debug = True,use_reloader=False)