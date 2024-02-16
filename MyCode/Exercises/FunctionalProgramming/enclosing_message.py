message = 'global'

def enclosing():
    #global message
    message = 'enclosing'
    
    def local():
        #global message
        #nonlocal no_such_name #Syntax Error
        nonlocal message
        message = 'local'

    print('enclosing message: ', message)
    local()
    print('enclosing message: ', message)

print('global message: ', message)
enclosing()
print('global message: ', message)

# try messing around with the above code
# use global and nonlocal at different parts
# predict output message based on which message is being changed




