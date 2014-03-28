#!/usr/bin/python

import dropbox
import json

# Only works with dropbox so far
def mkdir():

    try:
        with open('.virtualcloud') as userjson:
            userclouds = json.load(userjson)
    except IOError:
        print "Please login first!"
        sys.exit()

    db_tokens = userclouds["dropbox"]

    try:
        dirName = raw_input("Enter the name of the folder you'd like to create: ")
        #Hard coded client key. BAD! How do I fetch from JSON?
        dropbox.client.DropboxClient("YaiET0Jc82AAAAAAAAAAARAcR7-gfebqxbP4Zl32D_THrwRf_0DSjA6QECqfLOcy", locale=None, rest_client=None).file_create_folder(dirName)

    except dropbox.rest.ErrorResponse:
        raise



