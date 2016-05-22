from flask import Flask
app = Flask(__name__)
@app.route('/<chinese>')
def index(chinese):
    drive(chinese)

def drive(cmd):
    print cmd

app.run()#host='0.0.0.0')
print 'end'
