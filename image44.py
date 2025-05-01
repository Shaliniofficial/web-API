from flask import Flask,render_template,request,redirect,url_for,jsonify
app=Flask(__name__)
#use of get and post
@app.route("/form",methods=["GET","POST"])
def form():
    if request.method=="GET":
        return render_template('form.html')
    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])
        average_marks=(maths+science+history)/3
        res=""
        if average_marks>=50:
            res="success"
        else:
            res="failure"
        return redirect(url_for(res,score=average_marks))
    @app.route('/api',method=['post'])
    def calculate_sum():
        data=request.get_json()
        a_val=float(dict(data)['a'])
        b_val=float(dict(data)['b'])
        return jsonify(a_val+b_val)

        #return render_template('form.html',score=average_marks)



if __name__=="__main__":
    app.run(debug=True)
