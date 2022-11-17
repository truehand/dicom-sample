# dicom-sample

pip install -r requirements.txt 

Deploy DICOM:
https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/deploy-dicom-services-in-azure

Add your Azure user as a DICOM data owner after creating the service:
https://learn.microsoft.com/en-us/azure/healthcare-apis/configure-azure-rbac#assign-roles-for-the-dicom-service

Run the python script after changing the base_url with your service url (which you will obtain from the created service)

(Optional) Obtain an access token for running the curl commands:
token=$(az account get-access-token --resource=https://dicom.healthcareapis.azure.com --query accessToken --output tsv)
curl -X GET --header "Authorization: Bearer $token"  https://<workspacename-dicomservicename>.dicom.azurehealthcareapis.com/v<version of REST API>/changefeed

