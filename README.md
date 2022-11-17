## Azure DICOM Service 
# dicom-sample

[Deploy DICOM](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/deploy-dicom-services-in-azure)

[Add your Azure user as a DICOM data owner after creating the service](https://learn.microsoft.com/en-us/azure/healthcare-apis/configure-azure-rbac#assign-roles-for-the-dicom-service)


Install dependencies for the Python script **stow_and_wado.py**:
`pip install -r requirements.txt` 

Run the Python script after changing the base_url variable with your service url (which you will obtain from the created service). This Python script:

- deposits images in a study (provided under the *images* folder) -- the **stow** part
- and then allows you to retrieve instances under the study -- the **wado** part

Make sure to include the API version, **v1**, at the end of the base url as in:
`base_url = f"your_dicom_url.azurehealthcareapis.com/v1" # (line 10)` 

---
(Optional) Obtain an access token for running the curl commands:

`token=$(az account get-access-token --resource=https://dicom.healthcareapis.azure.com --query accessToken --output tsv)`

The above az command can be installed as described [here.](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

`curl -X GET --header "Authorization: Bearer $token"  https://<workspacename-dicomservicename>.dicom.azurehealthcareapis.com/v<version of REST API>/changefeed`

For your reference curl command examples are also provided. To run them you need an authentication token passed to the command:

`./command_stow.sh $token`