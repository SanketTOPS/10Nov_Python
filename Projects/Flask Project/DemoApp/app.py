from flask import Flask

app=Flask('__name__') #App Init.


@app.route('/')
def index():
    return "Hello Falsk!\nGood "

app.run(debug=True)

