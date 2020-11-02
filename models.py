import os
from firebase_admin import credentials, firestore, initialize_app
import pdb
import firebase_admin
from firebase_admin import credentials
import pandas as pd
from flask import *

if not firebase_admin._apps:
    cred = credentials.Certificate('key.json')
    default_app = initialize_app(cred)
db = firestore.client()


class cloudFirestore:
  
  def get_y2012(self):
    todo_ref = db.collection('y2012')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    print(all_todos)
    return data

  def get_y2013(self):
    todo_ref = db.collection('y2013')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    return data

  def get_y2014(self):
    todo_ref = db.collection('y2014')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    return data

  def get_y2015(self):
    todo_ref = db.collection('y2015')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    return data

  def get_y2016(self):
    todo_ref = db.collection('y2016')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    return data

  def get_y2017(self):
    todo_ref = db.collection('y2017')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    return data

  def get_y2018(self):
    todo_ref = db.collection('y2018')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    return data


  def get_y2019(self):
    todo_ref = db.collection('y2019')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos, index = [0,1,2,3]) 
    return data


#-----------------------data--------------------------------
class data:

  def data_get_y2012(self):
      data = cloudFirestore().get_y2012().val
      return list(data)

  def data_get_y2013(self):
      data = cloudFirestore().get_y2013().val
      return list(data)

  def data_get_y2014(self):
      data = cloudFirestore().get_y2014().val
      return list(data)  

  def data_get_y2015(self):
      data = cloudFirestore().get_y2015().val
      return list(data)      

  def data_get_y2016(self):
      data = cloudFirestore().get_y2016().val
      return list(data)  

  def data_get_y2017(self):
      data = cloudFirestore().get_y2017().val
      return list(data)  

  def data_get_y2018(self):
      data = cloudFirestore().get_y2018().val
      return list(data)  

  def data_get_y2019(self):
      data = cloudFirestore().get_y2019().val
      return list(data)  

#-------------------------------labels-----------------------
class lables:
  
  def labels_get_y2012(self):
      data = cloudFirestore().get_y2012().ID
      return list(data)

  def labels_get_y2013(self):
      data = cloudFirestore().get_y2013().ID
      return list(data)

  def labels_get_y2014(self):
      data = cloudFirestore().get_y2014().ID
      return list(data)  

  def labels_get_y2015(self):
      data = cloudFirestore().get_y2012().ID
      return list(data)

  def labels_get_y2016(self):
      data = cloudFirestore().get_y2012().ID
      return list(data)

  def labels_get_y2017(self):
      data = cloudFirestore().get_y2012().ID
      return list(data)

  def labels_get_y2018(self):
      data = cloudFirestore().get_y2012().ID
      return list(data)

  def labels_get_y2019(self):
      data = cloudFirestore().get_y2012().ID
      return list(data)
#___________________________________Scatter__________________________
