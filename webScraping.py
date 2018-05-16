#!/usr/bin/env python2
# -*- coding: utf-8 -*-
""" Created on Sat Jan 6 19:17:41 2018 @author: hmasoudt """
from flask import jsonify
import requests
import bs4
from flask import Flask
from flask import request
from flask import session, redirect, url_for, escape, request
app = Flask(__name__)
@app.route("/", methods=['GET', 'POST'])
def hello():

    if request.method == 'POST':
                ID = request.values.get('ID') # Your form's
                if not ID == "":
                    urldata="URL_STRING"+ID
                    page=requests.get(urldata)
                    soup=bs4.BeautifulSoup(page.content)
                    names=soup.find_all("td")
                    if names :
                              params = dict(
                                      error=False,
                                      MIID=int(names[76].string),
                                      SID=int(names[75].string),
                                      Date=names[74].string,
                                      Amount=names[73].string)
                              jsonex=jsonify(params)
                              return jsonex
                    else:
                                params = dict(error=True,
                                              detail="wrong-value")

    
                    return jsonify(params)
                else:
                    params = dict(error=True,
                                   detail="empty")

      
                    return jsonify(params)





