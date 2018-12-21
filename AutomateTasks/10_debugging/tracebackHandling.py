# traceback handling: extract it as a string using the traceback module
# saving traceback in a .txt file

import traceback

try:
    raise Exception('This is an error message')
except:
    errorFile = open('errorInfo.txt', 'w')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print('The traceback info was written to errorInfo.txt')
