

class ProcessErrorReport:

    err_line=''
    err_explain=''


    def __init__(self):
        pass


    def set_error_line(self, line):
        self.err_line=line
    
    def set_error_cause(self,cause):

        self.err_explain=cause
    
    def get_error_row(self):

        return ("line: ", self.err_line , " canot be processed. Caused by: ", self.err_explain, '\n')


