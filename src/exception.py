import sys 

def error_message_detail (error, error_detail:sys):
    ''' 
    We first put two underscores because exe_info gives us three important information
    & we are not interested in the first two   
    '''
    _,_,exc_tb=error.detail.exe_info() 

    # check documentation custom error handling in python to understand this 
    file_name= exc_tb.tb_frame.f_code.co_filename 

    error_message= "Error occured in python script [{0}] line number [{1}] error message [{2}]".format(
     file_name,exc_tb.tb_linen0,str(error))
    

    return error_message


# Declaring a new class that inherits from the "Exception" class
class CustomException (Exception):
    # constructor
    def __init__(self,error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message= error_message_detail(error_message, error_detail=error_detail)
    
    def __str__(self):
        return self.error_message
    
'''
    The value returned by error_message_detail function is assigned to class variable error_message
    
    error_detail is a parameter of sys module

    "sys" is a built-in module in Python that provides access to system-specific parameters and functions. 
    It provides information about the system and the environment in which the Python interpreter is running.
    '''