#--------- Flask settings
SERVER_HOST = 'azvargasproject3.azurewebsites.net' # Update this for the appropriate front-end website when up
SERVER_PORT = 80
FLASK_DEBUG = False # Do not use debug mode in prod

# Flask-Restplus settings
SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_404_HELP = True
API_VERSION = 'v1'

#-------- Azure constants

# API_URL format: "https://[FUNCTION_APP_NAME_GOES_HERE].azurewebsites.net"
API_URL = " https://azvargasproject3func.azurewebsites.net/api/"

# for local host if Azure functions served locally
#API_URL = "http://localhost:7071/api"
