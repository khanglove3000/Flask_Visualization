from flask import Flask, render_template
from flask import *
from models import bar, scatter
app = Flask(__name__)


data_bar = bar.sumofpayment(1)
labels_bar = bar.year(1)
@app.route('/bar')
def bar():
    return render_template('bar.html', values=data_bar, labels=labels_bar)

@app.route('/line')
def line():
    return render_template('line.html', values=data_bar, labels=labels_bar)

@app.route('/pie')
def pie():
    return render_template('pie.html', values=data_bar, labels=labels_bar)

data_scatter = scatter.scatter(1)
@app.route('/scatter')
def scatter():
    return render_template('scatter.html', values = data_scatter)
if __name__ == '__main__':
	app.run()