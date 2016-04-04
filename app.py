from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure
from bokeh.embed import components 
import Quandl, requests, pandas
import bokeh.plotting as bk
from bokeh.models import ColumnDataSource

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/graph', methods=['POST'])
def graph():
    symbol = request.form['ticker']
    print("Symbol %s" % symbol)

    qURL = 'https://www.quandl.com/api/v1/datasets/WIKI/'+ symbol + '.csv'
    print(qURL)
    df = pandas.read_csv(qURL)
    df['Date'] = pandas.to_datetime(df['Date'])
    df = df[['Date', 'Close']]
    source = ColumnDataSource()
    dtest = {}
    for col in df:
        dtest[col] = df[col]

    source = ColumnDataSource(data=dtest)

# bokeh plot
    TOOLS="pan,wheel_zoom,box_zoom,reset,save"
    p = bk.figure(title='Stock Price', tools=TOOLS,x_axis_type="datetime", plot_width=600, plot_height=300)
    p.line(y='Close', x='Date', source=source)
    script, div = components(p)
    return render_template('graph.html', script=script, div=div, ticker=symbol)

if __name__ == "__main__":
#    app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)
