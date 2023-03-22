from flask import Flask, request, Response, url_for, Blueprint
from flask_cors import CORS
from werkzeug.serving import run_simple
from werkzeug.middleware.dispatcher import DispatcherMiddleware
import json

import mysql_db as db

bp = Blueprint('burritos', __name__,
                        template_folder='templates')

@bp.route('/page',methods = ['POST', 'GET'])
def page():  # put application's code here
    args = request.args
    pageNum = int(args.get('pageNum')) if args.get('pageNum') != None else 1
    pageSize = int(args.get('pageSize')) if args.get('pageSize') != None else 10
    q = args.get('q') if args.get('q') != None else ''
    responseData = {
        "pageSize":pageSize,
        "pageNum":pageNum,
        "pageTotal": db.count(q),
        "data": db.selectPage((pageNum-1)*pageSize, pageSize, q)
    }
    response = {
        "code":200,
        "data":responseData
    }
    return Response(json.dumps(response),  mimetype='application/json')

@bp.route('/add',methods = ['POST', 'GET'])
def add():
    args = request.args
    obj = {
        'info': args.get('info'),
        'nickname': args.get('nickname'),
        'account': args.get('account'),
        'password': args.get('password'),
        'website': args.get('website'),
        'bind_email': args.get('bind_email'),
        'bind_phone': args.get('bind_phone'),
        'comment': args.get('comment')
    }
    db.insert(obj)
    response = {
        "code":200,
        "data":""
    }
    return Response(json.dumps(response),  mimetype='application/json')

@bp.route('/update',methods = ['POST', 'GET'])
def update():
    args = request.args
    obj = {
        'id': args.get('id'),
        'info': args.get('info'),
        'nickname': args.get('nickname'),
        'account': args.get('account'),
        'password': args.get('password'),
        'website': args.get('website'),
        'bind_email': args.get('bind_email'),
        'bind_phone': args.get('bind_phone'),
        'comment': args.get('comment')
    }
    db.update(obj)
    response = {
        "code":200,
        "data":""
    }
    return Response(json.dumps(response),  mimetype='application/json')

@bp.route('/delete',methods = ['POST', 'GET'])
def delete():  # put application's code here
    id = int(request.args.get('id'))
    db.deleteById(id)
    response = {
        "code":200,
        "data":""
    }
    return Response(json.dumps(response),  mimetype='application/json')

app = Flask(__name__, static_url_path="/")
# CORS configuation
CORS(app, supports_credentials=True)
app.register_blueprint(bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(host='0.0.0.0')
