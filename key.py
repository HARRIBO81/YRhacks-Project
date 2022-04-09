import os


import os
##who ever is running the demo for the video will be needing to put in their api key.
def getEnv():
    return os.environ.get('GMAPS_API_KEY')
