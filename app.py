# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc 
import plotly.express as px
import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import plotly.io as pio
from dash.dependencies import Input, Output
from datetime import datetime, date, timedelta

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server

url = "standings.csv"

df = pd.read_csv(url)

df['datetime'] = pd.to_datetime(df['date'])

# drop nas
df = df[df['Team'].notna()]

available_teams = df['Team'].unique()

# set theme
pio.templates.default = "plotly_white"
# px.defaults.width = 500
px.defaults.height = 300
default_team = 'Anthony'
# chart
fig1 = px.line(df, x = "date", y = "FG%", color = "Team", title = "FG%")
fig2 = px.line(df, x = "date", y = "FT%", color = "Team", title = "FT%")
fig3 = px.line(df, x = "date", y = "3PM", color = "Team", title = "3PM")
fig4 = px.line(df, x = "date", y = "REB", color = "Team", title = "REB")
fig5 = px.line(df, x = "date", y = "AST", color = "Team", title = "AST")
fig6 = px.line(df, x = "date", y = "STL", color = "Team", title = "STL")
fig7 = px.line(df, x = "date", y = "BLK", color = "Team", title = "BLK")
fig8 = px.line(df, x = "date", y = "TO", color = "Team", title = "TO")
fig9 = px.line(df, x = "date", y = "PTS", color = "Team", title = "PTS")


# format charts
figs = [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9]

for fig in figs:
	# edit colors
	for d in fig['data']:
	    if d['name'] == default_team:
	        d['line']['color']='blue'
	        d['line']['width']=4
	    else:
	        d['line']['color']='lightgrey'
	        d['line']['width']=1


	fig.update_layout(
		# template= 'ggplot2',
		margin=dict(l=10, r=10, t=50, b=30),
		showlegend=False,
	    font_color="grey",
	    legend_title_font_color="green")
	fig.update_yaxes(title='', 
		visible=True, 
		showticklabels=True)
	fig.update_xaxes(title='', 
		visible=True, 
		showticklabels=True)

# app 	
app.layout = html.Div(children=[

    # All elements from the top of the page
    html.Div([
    	# title
		html.H1(children='Ya 3ayni Analytics'),
		# subtitle
		html.H4(children='''
            Advanced stats for ESPN fantasy league.
            '''),
		html.P('Last updated: Bas ommak tole3 3abela', style={'font-style': 'italic'})
			], 
			# end header class
			style={'text-align': 'center'}, 
			className = 'header'),

    html.Div([    
    
    	# dropdown 1
	    html.Div([
			html.Label('Select Team'),
			    dcc.Dropdown(
			    	id = 'team-selection',
					options=[{'label': i, 'value': i} for i in available_teams],
			        value='Ramzy'
			        ),
	    	], className = 'four columns'),

	    # dropdown 2
	    html.Div([
			html.Label('Select Type'),
			    dcc.Dropdown(
			    	id = 'chart-selection',
					options=[
						{'label':'Totals', 'value': 'totals'},
						{'label':'Per Game', 'value':'per_game'},
					],
			        value='totals'
			        ),
	    	], className = 'four columns'),

    	# dropdown 3
	    html.Div([
			html.Label('Select Dates'),
			    dcc.Dropdown(
			    	id = 'date-selection',
					options=[
						{'label':'Last 5', 'value': 'last5'},
						{'label':'Last 15', 'value': 'last15'},
						{'label':'Last 30', 'value': 'last30'},
						{'label':'Since Jan 1st', 'value': 'sincebeg'},

					],
			        value='last30'
			        ),

	    	], className = 'four columns'),

	    # end row
	   	], className='row'),

	  #   html.Div([
			# html.Label('Select Dates'), 
			# 	dcc.DatePickerRange(
   #                          id='datepickerrange',
   #                          start_date=df['date'].min(),
   #                          end_date=df['date'].max(),
   #                          min_date_allowed=df['date'].min(),
   #                          max_date_allowed=df['date'].max().date(),
   #                          display_format='D MMM YYYY'
   #                          ),
	  #   	], className = 'six columns'),

    # first row of charts
    html.Div([

		# fig1
        html.Div([
            dcc.Graph(
                id='graph1',
                figure=fig1
            ),  
        ], className='four columns'),

		# fig2
        html.Div([
            dcc.Graph(
                id='graph2',
                figure=fig2
            ),  
        ], className='four columns'),
       	
       	# fig3
        html.Div([
            dcc.Graph(
                id='graph3',
                figure=fig3
            ),  
        ], className='four columns'),

	   	], className='row'),


    # New Div for all elements in the new 'row' of the page
    html.Div([

			# fig1
	        html.Div([
	            dcc.Graph(
	                id='graph4',
	                figure=fig4
	            ),  
	        ], className='four columns'),

			# fig2
	        html.Div([
	            dcc.Graph(
	                id='graph5',
	                figure=fig5
	            ),  
	        ], className='four columns'),
	       	
	       	# fig3
	        html.Div([
	            dcc.Graph(
	                id='graph6',
	                figure=fig6
	            ),  
	        ], className='four columns'),

	    ], className='row'),

    # New Div for all elements in the new 'row' of the page
    html.Div([

			# fig1
	        html.Div([
	            dcc.Graph(
	                id='graph7',
	                figure=fig7
	            ),  
	        ], className='four columns'),

			# fig2
	        html.Div([
	            dcc.Graph(
	                id='graph8',
	                figure=fig8
	            ),  
	        ], className='four columns'),
	       	
	       	# fig3
	        html.Div([
	            dcc.Graph(
	                id='graph9',
	                figure=fig9
	            ),  
	        ], className='four columns'),

	    ], className='row'),

])

# produce 9 charts
@app.callback(
    Output('graph1', 'figure'),
    Output('graph2', 'figure'),
    Output('graph3', 'figure'),
    Output('graph4', 'figure'),
    Output('graph5', 'figure'),
    Output('graph6', 'figure'),
    Output('graph7', 'figure'),
    Output('graph8', 'figure'),
    Output('graph9', 'figure'),
    Input('team-selection', 'value'),
    Input('chart-selection', 'value'),
    Input('date-selection', 'value'))

# def update_date(n):
# 	return print('Last updated:', str(date.today()))

def update_dashboard(team_name, per_game, date_range):

	df = pd.read_csv(url)
	df['dates'] = pd.to_datetime(df['date'])

	if date_range == 'last5':
		df = df[df['dates'] > max(df['dates']) - timedelta(5)]
	elif date_range == 'last15':
		df = df[df['dates'] > max(df['dates']) - timedelta(15)]
	elif date_range == 'last30':
		df = df[df['dates'] > max(df['dates']) - timedelta(30)]

	# drop nas
	df = df[df['Team'].notna()]

	if per_game == 'per_game':
		categories = ['3PM', 'AST', 'REB', 'PTS', 'TO', 'STL', 'BLK']
		for cat in categories:
			df[cat] = df[cat] / df['GP']

	fig1 = px.line(df, x = "date", y = "FG%", color = "Team", title = "FG%")
	fig2 = px.line(df, x = "date", y = "FT%", color = "Team", title = "FT%")
	fig3 = px.line(df, x = "date", y = "3PM", color = "Team", title = "3PM")
	fig4 = px.line(df, x = "date", y = "REB", color = "Team", title = "REB")
	fig5 = px.line(df, x = "date", y = "AST", color = "Team", title = "AST")
	fig6 = px.line(df, x = "date", y = "STL", color = "Team", title = "STL")
	fig7 = px.line(df, x = "date", y = "BLK", color = "Team", title = "BLK")
	fig8 = px.line(df, x = "date", y = "TO", color = "Team", title = "TO")
	fig9 = px.line(df, x = "date", y = "PTS", color = "Team", title = "PTS")

	# format charts
	figs = [fig1, fig2, fig3, fig4, fig5, fig6, fig7, fig8, fig9]

	for fig in figs:
		# edit colors
		for d in fig['data']:
		    if d['name'] == team_name:
		        d['line']['color']='blue'
		        d['line']['width']=4
		    else:
		        d['line']['color']='lightgrey'
		        d['line']['width']=1
		fig.update_layout(
			# template= 'ggplot2',

			margin=dict(l=10, r=10, t=50, b=30),
			showlegend=False,
		    font_color="grey",
		    legend_title_font_color="green")
		fig.update_yaxes(title='', 
			visible=True, 
			showticklabels=True)
		fig.update_xaxes(title='', 
			visible=True, 
			showticklabels=True)
		
	return figs



if __name__ == '__main__':
    app.run_server(debug=True)

# app.layout = html.Div([
# 	# h1('Ya 3ayni Advanced Stats'),
# 	html.Label('Select Category'),
#     dcc.Dropdown(
#         options=[
#             {'label': 'REB', 'value': 'REB'},
#             {'label': '3PM', 'value': '3PM'},
#             {'label': 'AST', 'value': 'AST'}
#         ],
#         value='REB'
#     ),

#     dcc.Graph(
#         id='life-exp-vs-gdp',
#         figure=fig
#     )
# ])

# if __name__ == '__main__':
#     app.run_server(debug=True)