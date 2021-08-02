from  application.errorReport import ProcessErrorReport



class errorGenerator:

    errors=[]

    
    
    def __new__(self, *args, **kw):
        if not hasattr(self, '_instance'):
            orig = super(errorGenerator, self)
            self._instance = orig.__new__(self, *args, **kw)
        return self._instance
    
    
    
    def __init__(self):
        ""

    
    def add_row_error_report(self,line, cause):
        new_error=ProcessErrorReport()
        new_error.set_error_line(line)
        new_error.set_error_cause(cause+ '\n')
        self.errors.append(str(new_error.get_error_row()))
    
    def get_full_report(self):
        lines=''
        return lines.join(self.errors)
    
    def reset_errors(self):
        self.errors=[]
        

      