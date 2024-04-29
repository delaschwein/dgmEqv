import pandas as pd
import plotly.graph_objects as go

# Define the data
data = [['2019-01-01', 200000, 205000, 210000, 195000],
        ['2019-02-01', 204000, 210000, 213000, 200000],
        ['2019-03-01', 210500, 215000, 218000, 205500],
        ['2019-04-01', 220000, 225000, 230000, 215000],
        ['2019-05-01', 226000, 235000, 238000, 220000],
        ['2019-06-01', 235000, 240000, 245000, 230000],
        ['2019-07-01', 245000, 250000, 255000, 240000],
        ['2019-08-01', 250500, 260000, 265000, 245000],
        ['2019-09-01', 260000, 265000, 270000, 255000],
        ['2019-10-01', 265500, 270000, 275000, 260000],
        ['2019-11-01', 270000, 275000, 280000, 265000],
        ['2019-12-01', 275500, 280000, 285000, 270000],
        ['2020-01-01', 280000, 285000, 290000, 275000],
        ['2020-02-01', 285500, 290000, 295000, 280000],
        ['2020-03-01', 290000, 295000, 300000, 285000],
        ['2020-04-01', 295500, 300000, 305000, 290000],
        ['2020-05-01', 300000, 305000, 310000, 295000],
        ['2020-06-01', 305500, 310000, 315000, 300000],
        ['2020-07-01', 310000, 315000, 320000, 305000],
        ['2020-08-01', 316000, 320000, 325000, 310000]]
df = pd.DataFrame(data, columns=['Date', 'Opening Price ($)', 'Closing Price ($)', 'High Price ($)', 'Low Price ($)'])

# Create the candlestick chart
fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                                     open=df['Opening Price ($)'],
                                     close=df['Closing Price ($)'],
                                     high=df['High Price ($)'],
                                     low=df['Low Price ($)'])])

# Update figure layout
fig.update_layout(title='Real Estate Housing Market Trends - Monthly Overview',
                  width=800,
                  height=600,
                  xaxis_range=['2019-01-01', '2020-08-01'],
                  yaxis_range=[190000, 330000])

# Save the figure
fig.write_image('/cpfs01/user/yehancheng/workspace/datasets/SimChartV2/demo/candlestick_plotly/png/129_202312302255.png')