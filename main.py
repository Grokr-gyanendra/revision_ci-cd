# def add(x,y):
#     return x+y

# def mul(x,y):
#     return x*y

# def sub(x,y):
#     return x-y

# def div(x,y):
#     if y == 0:
#         raise ValueError("Divide by 0 exception")
#     return x//y


from flask import Flask, request,jsonify

app = Flask(__name__)

@app.route('/')
def start():
    return "hii, welcome"

@app.route('/add')
def add():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({"ans": x+y})

@app.route('/sub')
def sub():
    x = int(request.args.get('x'))
    y = int(request.args.get('y'))
    return jsonify({"ans": x-y})

if '__name__' == '__main__':
    app.run()