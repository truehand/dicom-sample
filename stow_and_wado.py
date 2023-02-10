import requests
import pydicom
from pathlib import Path
from urllib3.filepost import encode_multipart_formdata, choose_boundary
from azure.identity import DefaultAzureCredential

# there is already sample dicom files in the folder provided in this repository, but you can use your own
path_to_dicoms_dir = "./images"

base_url = f"https://your_dicom_url.dicom.azurehealthcareapis.com/v1"

study_uid = "1.2.826.0.1.3680043.8.498.13230779778012324449356534479549187420"; #StudyInstanceUID for all 3 examples
series_uid = "1.2.826.0.1.3680043.8.498.45787841905473114233124723359129632652"; #SeriesInstanceUID for green-square and red-triangle
instance_uid = "1.2.826.0.1.3680043.8.498.47359123102728459884412887463296905395"; #SOPInstanceUID for red-triangle

from azure.identity import DefaultAzureCredential
credential = DefaultAzureCredential()

#print ("Available credentials:")
#print(credential.credentials) # this can be used to find the index of the AzureCliCredential
print("Using " + str(credential.credentials[3]) + " to authenticate")
token = credential.credentials[3].get_token('https://dicom.healthcareapis.azure.com')

bearer_token = f'Bearer {token.token}'

def encode_multipart_related(fields, boundary=None):
    if boundary is None:
        boundary = choose_boundary()

    body, _ = encode_multipart_formdata(fields, boundary)
    content_type = str('multipart/related; boundary=%s' % boundary)

    return body, content_type

## PART 0 ##
# testing the connection by requesting the change feed
print ("Testing connection to Azure API for DICOM and retrieving change feed\n")
client = requests.session()
headers = {"Authorization":bearer_token}
url= f'{base_url}/changefeed'

response = client.get(url,headers=headers)
if (response.status_code != 200):
    print('Error! Likely not authenticated!')
else:
    print('Connection successful, printing change feed:')
    print(response.text)

## PART 1 ##
print("\n\nSTOW PART (STORE)\n")
#upload blue-circle.dcm
filepath = Path("./images").joinpath('green-square.dcm')

# Read through file and load bytes into memory 
with open(filepath,'rb') as reader:
    rawfile = reader.read()
files = {'file': ('dicomfile', rawfile, 'application/dicom')}

#encode as multipart_related
body, content_type = encode_multipart_related(fields = files)

headers = {'Accept':'application/dicom+json', "Content-Type":content_type, "Authorization":bearer_token}

url = f'{base_url}/studies'
response = client.post(url, body, headers=headers, verify=False)

print(response.text)

## PART 2 ##
# retrive all instances within study
print ("\n\nWADO PART (RETRIEVE)\n")
url = f'{base_url}/studies/{study_uid}'
headers = {'Accept':'multipart/related; type="application/dicom"; transfer-syntax=*', "Authorization":bearer_token}

response = client.get(url, headers=headers) #, verify=False)
import requests_toolbelt as tb
from io import BytesIO

mpd = tb.MultipartDecoder.from_response(response)
for part in mpd.parts:
    # Note that the headers are returned as binary!
    print(part.headers[b'content-type'])
    
    # You can convert the binary body (of each part) into a pydicom DataSet
    #   And get direct access to the various underlying fields
    dcm = pydicom.dcmread(BytesIO(part.content))
    print("Retrieving", dcm.PatientName)
    print(dcm.SOPInstanceUID)

## PART 3 ##
# retrive metadata of all instances within study
print ("\n\nWADO PART (QUERY METADATA)\n")
url = f'{base_url}/studies/{study_uid}/metadata'
headers = {'Accept':'application/dicom+json', "Authorization":bearer_token}

response = client.get(url, headers=headers) #, verify=False)
print(response.text)

## PART 4 ##
# search for series within study
print ("\n\nQIDO PART (SEARCH SERIES IN STUDY)\n")
url = f'{base_url}/studies/{study_uid}/series'
headers = {'Accept':'application/dicom+json', "Authorization":bearer_token}
params = {'SeriesInstanceUID':series_uid}

response = client.get(url, headers=headers, params=params) #, verify=False)
print(response.text)