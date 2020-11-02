from flask import Flask, render_template
from flask import *
from models import lables, data
app = Flask(__name__)



#__________2012______________________
data_get_y2012 = data.data_get_y2012(1)
labels_get_y2012 = lables.labels_get_y2012(1)
@app.route('/y2012')
def y2012():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2012, labels=labels_get_y2012) 

#_____________2013___________________
data_get_y2013 = data.data_get_y2013(1)
labels_get_y2013 = lables.labels_get_y2013(1)
@app.route('/y2013')
def y2013():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2013, labels=labels_get_y2013, colors=colors) 

#_________________2014_______________
data_get_y2014 = data.data_get_y2014(1)
labels_get_y2014 = lables.labels_get_y2014(1)
@app.route('/y2014')
def y2014():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2014, labels=labels_get_y2014, colors=colors) 

#__________________2015_______________
data_get_y2015 = data.data_get_y2015(1)
labels_get_y2015 = lables.labels_get_y2015(1)
@app.route('/y2015')
def y2015():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2015, labels=labels_get_y2015, colors=colors) 

#__________________2016_______________
data_get_y2016 = data.data_get_y2016(1)
labels_get_y2016 = lables.labels_get_y2016(1)
@app.route('/y2016')
def y2016():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2016, labels=labels_get_y2016, colors=colors) 

#__________________2017_______________
data_get_y2017 = data.data_get_y2017(1)
labels_get_y2017 = lables.labels_get_y2017(1)
@app.route('/y2017')
def y2017():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2017, labels=labels_get_y2017, colors=colors) 

#__________________2018_______________
data_get_y2018 = data.data_get_y2018(1)
labels_get_y2018 = lables.labels_get_y2018(1)
@app.route('/y2018')
def y2018():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2018, labels=labels_get_y2018, colors=colors) 

#__________________2019_______________
data_get_y2019 = data.data_get_y2019(1)
labels_get_y2019 = lables.labels_get_y2019(1)
@app.route('/y2019')
def y2019():
    colors = ['red','orange','yellow','violet']
    return render_template('chart.html', values=data_get_y2019, labels=labels_get_y2019, colors=colors) 




#-----------------------------------------------scatter-------------------------------








@app.route('/')
def index():
  return render_template('index.html')

@app.route('/Quy')
def chart1():
  return render_template('quy.html')


if __name__ == '__main__':
	app.run()