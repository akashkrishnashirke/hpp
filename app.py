from flask import Flask,request,jsonify,render_template #(jsonify use for convert result in json formate)
import numpy as np
import pickle
from utils import hpp


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    data = request.form
    print(data)
    print("*"*50)

    hpp_obj = hpp(data)
    result = hpp_obj.predict()

    #CRIM= data['CRIM']    # we use type casting for fixed [ValueError: dtype='numeric' is not compatible with arrays of bytes/strings.Convert your data to numeric values explicitly instead.]
    # CRIM= float(data['CRIM'])
    # ZN= float(data['ZN'])
    # INDUS= float(data['INDUS'])
    # CHAS= float(data['CHAS'])
    # NOX= float(data['NOX'])
    # RM= float(data['RM'])
    # AGE= float(data['AGE'])
    # DIS= float(data['DIS'])
    # RAD= float(data['RAD'])
    # TAX= float(data['TAX'])
    # PTRATIO= float(data['PTRATIO'])
    # B= float(data['B'])
    # LSTAT= float(data['LSTAT'])

    # array = np.array([CRIM ,ZN ,INDUS ,CHAS ,NOX ,RM ,AGE ,DIS ,RAD ,TAX ,PTRATIO ,B ,LSTAT ,],ndmin = 2)
    # print(array)
    # print("*"*50)

    # with open("model.pickle","rb") as file:
    #     model = pickle.load(file)
    
    #result = model.predict(array)             # result ha 36.20864376145233 yevadha sagale digit gheto so only 3 digit madhe show karanyasathi following
    # result = np.around(model.predict(array),2)   # result ==> 36.21
    # print(result)

                                            # so return madhe result ha json formate madhe pathavanyasthi following..
    #return jsonify({"House Price":result[0]})  # use [0] for fixed error  [TypeError: Object of type ndarray is not JSON serializable]
            # jar result ha front chyach page var show karayacha asel tar
    return render_template('index.html',pred = result)

if __name__ == "__main__":
    #app.run(debug = True) 
    app.run(host = '0.0.0.0',port = 8080,debug = False)  # bydefalt debug = False he false ch aasate so nahi write kele tari chalate