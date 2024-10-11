# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 13:46:45 2024

@author: Prorumus Marketing
"""

from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

# Lista global para armazenar os dados
data_list = []

# Rota principal que exibe a lista de dados
@app.route("/")
def index():
    return render_template("index.html", data_list=data_list)

# Rota que recebe os dados via URL e os armazena
@app.route('/add_data')
def add_data():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    
    if name and email and phone:
        # Adiciona os dados à lista
        data_list.append({
            'name': name,
            'email': email,
            'phone': phone
        })
        
    return redirect(url_for('index'))

if __name__=='__main__':
    app.run(debug=True)