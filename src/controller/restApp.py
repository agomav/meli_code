import os
from threading import ExceptHookArgs




from flask import (
    Flask,
    g,
    render_template,
    Response,
    jsonify,
    redirect,
    request
)

from werkzeug.utils import secure_filename

from application.fileValidator import fileScanner
from application.fileReader import Reader
from infraestructure.apiconnection import MeLiAuthHandler as meli
from application.MeLiIntegrationService import MeliService

from configuration.configProvider import configurationServer
from application.errorReportService import errorGenerator




app = Flask(__name__)
prop=configurationServer()

@app.route('/ping', methods=['GET'])
def get_status():
     return jsonify({'response': 'pong!'})


@app.route('/meli_auth', methods=['GET'])
def auth():

     return redirect(meli.authHandler.get_auth_url())
      

@app.route("/get_token")
def get_token():
    print("got a request!")
    apiCode=request.args.get('code', '')
    print( "great! here is the initial code: !"+ apiCode)
    meliService=MeliService()
    meliService.auth_handler(apiCode)
    print("auth ready!!!!")
    return jsonify({'response': 'authentication ready!'})
   
    




@app.route('/upload', methods=['GET'])
def get_loader_window():
     return render_template('upload.html')



@app.route('/FileUploader', methods = ['POST'])
def upload_file():
    savePath="filesStorage"
    if 'filePath' not in request.files:
        return jsonify({'response': 'file request is not valid!'})
       
    myfile = request.files['filePath']
    
    if myfile.filename == "" :
        return jsonify({'response': 'file param cannot be empty!'})
    
    fileext=myfile.filename.rsplit('.', 1)[1].lower()
    response=''
    valid=fileScanner()
    read_file=Reader()
    err_check=errorGenerator()
    if valid.validate_file_extension(fileext):
      
      myfile.save(os.path.join(savePath,secure_filename(myfile.filename)))
      
      print("full path is: " + os.path.join(savePath,secure_filename(myfile.filename)))
      
      
      try:
        response=read_file.readFile(os.path.join(savePath,secure_filename(myfile.filename)))
      except Exception as ex:
          print(ex)
          return err_check.get_full_report()
      
      
      
      if response!="":
          response= "Some lines of the file has error. Here the details:" +response
          return response
      else:
          return  jsonify({'response': 'file procesed correctly!'})

    print ("here we goooo!!!")
    return err_check.get_full_report()




if __name__ == '__main__':
   # app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
     app.run(host=prop.getProperty('flask_server_host'), port=prop.getProperty('flask_server_port'))