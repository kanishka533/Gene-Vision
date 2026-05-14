from flask import Flask

app = Flask(**name**)

@app.route('/')
def home():
return "GeneScope Backend Running"

if **name** == '**main**':
app.run(debug=True)
