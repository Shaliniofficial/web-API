from flask import Flask
app=Flask(__name__)
#variable rule
@app.route("/success/<score>")
def success(score):
    return" the person has passed and score is:"+score
@app.route("/fail/<score>")
def fail(score):
    return"the person has failed and the score is:"+score

if __name__=="__main__":
    app.run(debug=True)



