#!/usr/bin/python
# Include the Dropbox SDK
import dropbox

# Get your app key and secret from the Dropbox developer website
app_key = 'pp92jonnw43vmz8'
app_secret = 'il7w6zl9blvejok'
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)

class db(object):
    AT = ''
    client = 0
    
    def __init__(self, token):
        self.AT = token
        if token == -1:
            self.db_login()
        else:
            self.client = dropbox.client.DropboxClient(self.AT)

    def db_login(self):
        # Have the user sign in and authorize this token
        authorize_url = flow.start()
        print '1. Go to: ' + authorize_url
        print '2. Click "Allow" (you might have to log in first)'
        print '3. Copy the authorization code.'
        code = raw_input("Enter the authorization code here: ").strip()

        # This will fail if the user enters an invalid authorization code
        access_token, user_id = flow.finish(code)
        self.AT = access_token
        self.client = dropbox.client.DropboxClient(access_token)
        print 'linked account: ', self.client.account_info()

    def db_upload(self, user_file):
        f = open(user_file, 'rb')
        response = self.client.put_file('/' + user_file, f)
        print 'uploaded: ', response
    
    def db_download(self, user_file):
        f, metadata = self.client.get_file_and_metadata('/' + user_file)
        out = open(user_file, 'wb')
        out.write(f.read())
        out.close()
        print metadata