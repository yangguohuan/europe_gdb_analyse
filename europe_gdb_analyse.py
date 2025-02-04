import pandas as pd
import plotly.graph_objs as go
from plotly.subplots import make_subplots

fig = make_subplots(1,2,subplot_titles=('各国最新GDP','近年各国GDP变化'))

df = pd.read_csv('Europe_GDP.csv')
#fig = go.Figure()
x = df['Year'].values.tolist()
countries = df.columns.values
countries = countries[1:]
for country in countries:
    fig.add_trace(go.Scatter(x=x, y=df[f'{country}'], mode='lines+markers', name=f'{country}'),row=1, col=2)
fig.add_trace(go.Bar(x=countries, y=df.iloc[:,-1], name='最新GDP'), row=1, col=1)
fig.update_layout(
    xaxis=dict(tickmode='array', tickvals=x, ticktext=x),
    yaxis=dict(tickformat='.2e'),
    xaxis_title="year",
    yaxis_title="GDP",
    template="plotly_white"
)
fig.show()