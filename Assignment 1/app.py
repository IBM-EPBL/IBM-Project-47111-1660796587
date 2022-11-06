from flask import Flask, render_template, url_for, request, 

app=Flask(__name__)


@app.route('/')

def home():
    return render_template('register.html')

@app.route("/conform",methods=['POST','GET'])
def register():
    if request.method=='POST':
        n=request.form.get('uname')
        a=request.form.get('phoneno')
        c=request.form.get('email')
        return render_template('conform.html',uname=n,phoneno=a,email=c)


if __name__=="__main__":
   app.run(debug=True)
