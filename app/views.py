from flask import Flask, render_template, Blueprint

app_routes =  Blueprint('app_routes', __name__)

@app_routes.route('/')
def index():
    return render_template('index.html')