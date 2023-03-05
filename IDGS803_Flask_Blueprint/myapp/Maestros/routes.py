from flask import Blueprint
maestros= Blueprint('maestros',__name__)

@maestros.route('/getmaestros',methods=['GET'])
def getmaestros():
    return{'key':'Maestros'}