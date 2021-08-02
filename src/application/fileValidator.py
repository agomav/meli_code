from configuration.configProvider import configurationServer
from  application.errorReportService import errorGenerator


class fileScanner:

  ALLOWED_EXTENSIONS=''
  MAX_FILE_SIZE=''

  def __init__(self):
      config=configurationServer()
      self.MAX_FILE_SIZE=config.getProperty('max_file_size')
      self.ALLOWED_EXTENSIONS=config.getProperty('file_allowed_extensions').split(',')
      self.err_new=errorGenerator()
      

  def validate_file_extension(self,file_ext):
    validate= False
    if file_ext in self.ALLOWED_EXTENSIONS:
        validate=True
    else:
        self.err_new.add_row_error_report('',"File extension no supported in current config")
    return validate
  


  def validate_file_encoding(self,file_enc):
    validate= False
    ALLOWED_ENCODINGS={'UFT-8','ISO-25678'}
    if file_enc in ALLOWED_ENCODINGS:
        validate=True
    return validate
  

  


 

