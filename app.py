from flask import Flask, render_template,jsonify
app=Flask(__name__)


jobs= [{"id": 1,"Job Title": "Data Analyst", "location": "Remote","salary":"Rs. 12,0000"},
     {
  "id": 2,
  "Job Title": "Data Scientist",
  "location": "Hybrid",
  "salary":"Rs. 15,0000"
},
{
  "id": 3,
  "Job Title": "Data Engineer",
  "location": "Mumbai, India",
  "salary":"Rs. 10,0000"
},
{
  "id": 1,
  "Job Title": "Business Analyst",
  "location": "Seattle, Wahington",
}]
@app.route("/")
def hello_world():
  return render_template("home.html", jobs=jobs)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(jobs)
if __name__=="__main__":
  app.run(host="0.0.0.0", debug=True)
