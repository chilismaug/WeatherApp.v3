import json
import os
import logging
from pprint import pprint as pp
from google.cloud import storage

def get_cities():
    file_name = "cities.json"

    # fallback data in case can't get cloud json
    here_data = [{'name':'Canberra'},
               {'name':'Kathmandu'},
               {'name':'Kyoto'},
               {'name':'Montreal'},
               {'name':'Quebec'},
               {'name':'Reykjavik'},
               {'name':'Timbuktu'},
               {'name':'Toronto'},
               {'name':'Vancouver'}]

#    jsonFile = os.path.join( "static", "data", filename)
#    jsonFile = os.path.join(os.path.split(__file__)[0], 'data/cities.json')

    # create Goo Cloud Storage client to get that json from
    try:
        # Configure this environment variable via app.yaml
        CLOUD_STORAGE_BUCKET = os.environ['CLOUD_STORAGE_BUCKET']
        CLOUD_STORAGE_FOLDER = "data"
        gcs = storage.Client()
        # Get the bucket that the file will be uploaded to.
        bucket = gcs.get_bucket(CLOUD_STORAGE_BUCKET)

        # the data file will be known as a blob to us henceforth
        myblob = bucket.get_blob(CLOUD_STORAGE_FOLDER + "/"+ file_name)

        print("we have blob!")
        print(myblob.name)

        b = myblob.download_as_string()
        print("what's in b?")
        print(b)

        try:
            file_data = json.loads(b)
        except:
            file_data = [{"name":"json file read failed"}]

        #print("what's in file_data?")
        #print(file_data)

        if len(file_data) > 0:
            data = file_data
        else:
            data = here_data
    except KeyError:
        data = here_data

    return data
