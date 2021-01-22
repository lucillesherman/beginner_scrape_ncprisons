from googleapiclient import discovery
from apiclient.http import MediaFileUpload

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"]="nc-prisons-covid-cases-9f729f29cec0.json"

drive_service = discovery.build('drive', 'v3')

def uploadFile(filename, filepath, mimetype, folderid):
    file_metadata = {'name': filename,
                     "parents": [folderid]
                     }
    media = MediaFileUpload(filepath,
                            mimetype=mimetype)
    file = drive_service.files().create(body=file_metadata,
                                        media_body=media,
                                        fields='id').execute()
    print('File ID: %s' % file('id'))
  
#sample to use it:
filename = '*.csv'
filepath = '/Users/user/Desktop/nopolitics/coronavirus_counts/nc_prison_counts/'
mimetype = 'csv'
folderid = '1m_MNvQw3szzCyGC0RFWCrUqSII4UPs3F' #ex:'1tQ63546ñlkmulSaZtz5yeU5YTSFMRRnJz'
uploadFile(filename, filepath, mimetype, folderid)

# file1 = drive.CreateFile({'title': 'Hello.txt'})  # Create GoogleDriveFile instance with title 'Hello.txt'.
# file1.SetContentString('Hello World!') # Set content of the file from given string.
# file1.Upload()

# file1['title'] = 'HelloWorld.txt' # Change title of the file.
# file1.Upload() # Update metadata.
# print('title: %s' % file1['title']) # title: HelloWorld.txt.

# file2 = drive.CreateFile('id')
# print('title: %s, mimeType: %s' % (file2['title'], file2['mimeType']))

# f = drive.CreateFile({'parent': '1m_MNvQw3szzCyGC0RFWCrUqSII4UPs3F'})
# f.SetContentFile('prisonactionscovid2020-07-16 18:00.csv') # Read local file
# f.Upload() # Upload it

#title: North Carolina State Prison Covid Cases
#id: 1m_MNvQw3szzCyGC0RFWCrUqSII4UPs3F

# def upload_file_to_specific_folder(self, folder_id, file_name):
# 	file_metadata = {'North Carolina State Prison Covid Cases': file_name, "parents": [{"1m_MNvQw3szzCyGC0RFWCrUqSII4UPs3F": folder_id, "kind": "drive#childList"}]}
# 	folder = self.drive.CreateFile(file_metadata)
# 	folder.SetContentFile("*.csv") #The contents of the file
# 	folder.Upload()

folder_list = drive.ListFile({'q': "trashed=false"}).GetList()
for folder in folder_list:
	print('folder title: %s, id: %s' % (folder['title'], folder['id']))