import json
import pickle
import numpy as np
import os

__gender = None
__data_columns = None
__model = None
__area = None
__married = None
__dependents = None
__employed = None
__education = None

def get_estimated(gender,married,dependents,education,employed,area,applicantincome,coapplicantincome,loanamount,loanamountterm,credithistory):
    try:
        loc_index_1 = __data_columns.index(gender.lower())
        loc_index_2 = __data_columns.index(married.lower())
        loc_index_3 = __data_columns.index(dependents.lower())
        loc_index_4 = __data_columns.index(education.lower())
        loc_index_5 = __data_columns.index(employed.lower())
        loc_index_6 = __data_columns.index(area.lower())
    except:
        loc_index_1 = -1
        loc_index_2 = -1
        loc_index_3 = -1
        loc_index_4 = -1
        loc_index_5 = -1
        loc_index_6 = -1

    x = np.zeros(len(__data_columns))
    x[0] = applicantincome
    x[1] = coapplicantincome
    x[2] = loanamount
    x[3] = loanamountterm
    x[4] = credithistory
    if loc_index_1 >= 0:
        x[loc_index_1] = 1
    if loc_index_2 >= 0:
        x[loc_index_2] = 1
    if loc_index_3 >= 0:
        x[loc_index_3] = 1
    if loc_index_4 >= 0:
        x[loc_index_4] = 1
    if loc_index_5 >= 0:
        x[loc_index_5] = 1
    if loc_index_6 >= 0:
        x[loc_index_6] = 1

    #return __model.predict([x])[0]
    result = __model.predict([x])
    if result == 1:
        return 'Loan Approved'

    return 'Loan Rejected'

def load_saved_artifacts():
    print('loading saved artifacts...')
    global __data_columns
    global __gender
    global __married
    global __dependents
    global __education
    global __employed
    global __area

    path = os.path.dirname(__file__)
    artifacts = os.path.join(path, "artifacts"),

    with open(artifacts[0] + "/columns.json", "r") as f:
        __data_columns = json.load(f)['data_columns']
        __gender = __data_columns[5:7]
        __married = __data_columns[7:9]
        __dependents = __data_columns[9:13]
        __education = __data_columns[13:15]
        __employed = __data_columns[15:17]
        __area = __data_columns[17:]

    global __model
    if __model is None:
        with open(artifacts[0] + "/loan_data_prediction.pickle","rb") as f:
            __model = pickle.load(f)
    print('loading saved artifacts end....')

def get_data_columns():
    return __data_columns

def get_gender():
    return __gender

def get_married():
    return __married

def get_dependents():
    return __dependents

def get_education():
    return __education

def get_employed():
    return __employed

def get_applicantarea():
    return __area

load_saved_artifacts()


if __name__ == "__main__":
#     load_saved_artifacts()
#     print(get_married())
#     print(get_gender())
#     print(get_married())
#     print(get_dependents())
#     print(get_education())
#     print(get_employed())
#     print(get_applicantarea())
    print(get_estimated("gender_male", "married_yes", "dependents_0", "education_graduate","self_employed_no", "property_area_rural", 5703, 0, 130, 130, 1))