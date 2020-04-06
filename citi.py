import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import csv
import pandas as pd
import plotly.graph_objs as go

df15 = pd.read_csv('valeursfoncieres-2015.csv', delimiter = '|',usecols=['CodePostal','ValeurFonciere','Section'],low_memory=False)
df15.ValeurFonciere = df15.ValeurFonciere.astype('str')
df15.ValeurFonciere = df15.ValeurFonciere.apply(lambda x: x.replace(",", ".")).astype(float)
moyenne_prix15 = df15.groupby('CodePostal').agg({'ValeurFonciere':["mean", "max", "count"]})
moyenne_prix15 = moyenne_prix15.reset_index(drop=False)
moyenne_prix15.CodePostal = moyenne_prix15.CodePostal.astype('int')

df16 = pd.read_csv('valeursfoncieres-2016.csv', delimiter = '|',usecols=['CodePostal','ValeurFonciere','Section'],low_memory=False)
df16.ValeurFonciere = df16.ValeurFonciere.astype('str')
df16.ValeurFonciere = df16.ValeurFonciere.apply(lambda x: x.replace(",", ".")).astype(float)
moyenne_prix16 = df16.groupby('CodePostal').agg({'ValeurFonciere':["mean", "max", "count"]})
moyenne_prix16 = moyenne_prix16.reset_index(drop=False)
moyenne_prix16.CodePostal = moyenne_prix16.CodePostal.astype('int')

df17 = pd.read_csv('valeursfoncieres-2017.csv', delimiter = '|',usecols=['CodePostal','ValeurFonciere','Section'],low_memory=False)
df17.ValeurFonciere = df17.ValeurFonciere.astype('str')
df17.ValeurFonciere = df17.ValeurFonciere.apply(lambda x: x.replace(",", ".")).astype(float)
moyenne_prix17 = df17.groupby('CodePostal').agg({'ValeurFonciere':["mean", "max", "count"]})
moyenne_prix17 = moyenne_prix17.reset_index(drop=False)
moyenne_prix17.CodePostal = moyenne_prix17.CodePostal.astype('int')

df18 = pd.read_csv('valeursfoncieres-2018.csv', delimiter = '|',usecols=['CodePostal','ValeurFonciere','Section'],low_memory=False)
df18.ValeurFonciere = df18.ValeurFonciere.astype('str')
df18.ValeurFonciere = df18.ValeurFonciere.apply(lambda x: x.replace(",", ".")).astype(float)
moyenne_prix18 = df18.groupby('CodePostal').agg({'ValeurFonciere':["mean", "max", "count"]})
moyenne_prix18 = moyenne_prix18.reset_index(drop=False)
moyenne_prix18.CodePostal = moyenne_prix18.CodePostal.astype('int')

df19 = pd.read_csv('valeursfoncieres-2019.csv', delimiter = '|',usecols=['CodePostal','ValeurFonciere','Section'],low_memory=False)
df19.ValeurFonciere = df19.ValeurFonciere.astype('str')
df19.ValeurFonciere = df19.ValeurFonciere.apply(lambda x: x.replace(",", ".")).astype(float)
moyenne_prix19 = df19.groupby('CodePostal').agg({'ValeurFonciere':["mean", "max", "count"]})
moyenne_prix19 = moyenne_prix19.reset_index(drop=False)
moyenne_prix19.CodePostal = moyenne_prix19.CodePostal.astype('int')

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



app.layout = html.Div([
    html.H6('Type de bien'),
    dcc.Dropdown( 
        id='page-3-dropdown',
        options=[{'label': i, 'value': i} for i in [ 'Maison ', 'Appartement']],
        value='LA',
        multi=True
    ),
    html.H6('Nb de pièces'),
    dcc.Dropdown(
        id='page-2-dropdown',
        options=[{'label': i, 'value': i} for i in [ '1', '2','3','4','5+']],
        value='LA',
        multi=True
    ),
    html.H6('Surface (en m2)'),
    html.Div([
    dcc.Input(id='id', placeholder="en m2", type='number', min=0)
]),
    html.H6('Budget (en €)'),
    html.Div([
    dcc.Input(id='id2', placeholder="en €", type='number', min=0)
]),
    html.H6('Code Postal'),
    html.Div([
    dcc.Dropdown(
        id='id3',
        options=[{'label': i, 'value': i} for i in moyenne_prix18['CodePostal'].unique()],
        value='1000',
        multi=False
    )
]),

    html.Div(id='display-selected-values'), html.Div(id='values')#,html.Div(id='section')
])



@app.callback(
    Output('display-selected-values', 'children'),
    [Input('page-3-dropdown', 'value'),
    Input('page-2-dropdown', 'value'),
    Input('id', 'value'),
    Input('id2', 'value'),
     Input('id3', 'value')])
def set_display_children(a, b,c,d,e):
    return u'Vous recherchez {} dans le {} ayant {} pièces avec une surface de {} m2. Votre budget se situe autour de {}€'.format(
        a,e, b,c,d
    )

@app.callback( Output('values', 'children'),
              [Input('id3', 'value')])
def cp(value):
    tsr15=moyenne_prix15[moyenne_prix15['CodePostal']==value]
    a15=tsr15.ValeurFonciere['mean']
    a15 = round(a15.iloc[0])
    a15=a15.astype('int')
    b15=tsr15.ValeurFonciere['count']
    b15 = b15.iloc[0]

    tsr16=moyenne_prix16[moyenne_prix16['CodePostal']==value]
    a16=tsr16.ValeurFonciere['mean']
    a16 = round(a16.iloc[0])
    a16=a16.astype('int')
    b16=tsr16.ValeurFonciere['count']
    b16 = b16.iloc[0]

    tsr17=moyenne_prix17[moyenne_prix17['CodePostal']==value]
    a17=tsr17.ValeurFonciere['mean']
    a17 = round(a17.iloc[0])
    a17=a17.astype('int')
    b17=tsr17.ValeurFonciere['count']
    b17 = b17.iloc[0]

    tsr18=moyenne_prix18[moyenne_prix18['CodePostal']==value]
    a18=tsr18.ValeurFonciere['mean']
    a18 = round(a18.iloc[0])
    a18=a18.astype('int')
    b18=tsr18.ValeurFonciere['count']
    b18 = b18.iloc[0]

    tsr19=moyenne_prix19[moyenne_prix19['CodePostal']==value]
    a19=tsr19.ValeurFonciere['mean']
    a19 = round(a19.iloc[0])
    a19=a19.astype('int')
    b19=tsr19.ValeurFonciere['count']
    b19 = b19.iloc[0]

    #a=a.iloc[:,:].values
    return('Moyenne de la valeur foncière sur la zone en 2015 : '+str(a15)+'€, en 2016 : '+str(a16)+'€, en 2017 : '+str(a17)+'€, en 2018 : '+str(a18)+'€, et en 2019 : '+str(a19)+'€. Le nombre de vente en 2015 :'+str(b15)+', en 2016 : '+str(b16)+', en 2017 : '+str(b17)+', en 2018 : '+str(b18)+' et en 2019 : '+str(b19))




if __name__ == '__main__':
    app.run_server(debug=True)