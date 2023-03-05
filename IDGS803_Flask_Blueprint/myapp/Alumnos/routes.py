from flask import Blueprint
alumnos= Blueprint('alumnos',__name__)

@alumnos.route('/getalumn',methods=['GET'])
def getalumn():
    return{'key':'Alumnos'}