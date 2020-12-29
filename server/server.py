from flask import Flask, request, jsonify, render_template
#import util #run in local
import server.util as util #this for deployment

#app = Flask(__name__)
app = Flask(__name__, static_url_path="/client", static_folder='../client', template_folder="../client")

@app.route('/', methods=['GET'])
def index():
    if request.method == "GET":
        return render_template("app.html")

@app.route('/get_gender', methods=['GET'])
def get_gender():
    response = jsonify({
        'gender': util.get_gender()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/applicantarea', methods=['GET'])
def get_applicantarea():
    response = jsonify({
        'area': util.get_applicantarea()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_married', methods=['GET'])
def get_married():
    response = jsonify({
        'married': util.get_married()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_education', methods=['GET'])
def get_education():
    response = jsonify({
        'education': util.get_education()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_dependents', methods=['GET'])
def get_dependents():
    response = jsonify({
        'dependents': util.get_dependents()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/get_employed', methods=['GET'])
def get_employed():
    response = jsonify({
        'employed': util.get_employed()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/predict_loan', methods=['POST'])
def predict_loan():
    gender = request.form['gender']
    married = request.form['married']
    dependents = request.form['dependents']
    education = request.form['education']
    employed = request.form['employed']
    area = request.form['area']
    applicantincome = int(request.form['applicantincome'])
    coapplicantincome = int(request.form['coapplicantincome'])
    loanamount = int(request.form['loanamount'])
    loanamountterm = int(request.form['loanamountterm'])
    credithistory = int(request.form['credithistory'])

    response = jsonify({
        'estimated_loan': util.get_estimated(gender,married,dependents,education,employed,area,applicantincome,coapplicantincome,loanamount,loanamountterm,credithistory)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    print("Starting python flask for loan prediction...")
    ##print(util.get_estimated("gender_male", "married_yes", "dependents_0", "education_graduate", "self_employed_no", "property_area_rural", 5703, 0.0, 130.0, 130.0, 1))
    app.run(debug=True)


