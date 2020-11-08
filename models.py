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

class bar:
  
  def dataperyear(self):
    todo_ref = db.collection('dataperyear')
    all_todos = [doc.to_dict() for doc in todo_ref.stream()]
    data = pd.DataFrame(all_todos)
    data.pop('ID') 
    return data

  def sumofpayment(self):
    data = bar.dataperyear(1)
    data = data.sumofpayment 
    return list(data)

  def year(self):
    data = bar.dataperyear(1)
    data = data.year 
    return list(data)
    
class scatter:
  def scatter(self):
      todo_ref = db.collection('scatter2')
      all_todos = [doc.to_dict() for doc in todo_ref.stream()]
      data = pd.DataFrame(all_todos)
      data.pop('ID')
      df = data.to_dict('records')
      return df