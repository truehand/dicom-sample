## Azure DICOM Service Python example to store (stow) and retrieve (wado) DICOMs

First step is to set up a DICOM Service in Azure: [Deploy DICOM](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/deploy-dicom-services-in-azure)

Next, [add your Azure user as a DICOM data owner after creating the service](https://learn.microsoft.com/en-us/azure/healthcare-apis/configure-azure-rbac#assign-roles-for-the-dicom-service)

In your local environment, preferably create a new conda environment, and then install dependencies listed under **requirements.txt**:

`pip install -r requirements.txt` 

Run the main Python script **stow_and_wado.py** after changing the *base_url* variable with your service url (which you will obtain from the created service). 

The script **stow_and_wado.py** will:
- test the connection by requesting and printing the changefeed of your DICOM service
- deposit DICOM images from a study into the DICOM server (images are provided under the *images* folder) -- the **stow** part (**ST**ore **O**ver the **W**eb)
- and then retrieve instances under the same study stored on the DICOM server -- the **wado** part (**W**eb **A**ccess to **D**ICOM **O**bjects)

Make sure to include the API version, **v1**, and to update the part `your_dicom_url` to reflect your service name, in the base url, as in:

`base_url = f"your_dicom_url.azurehealthcareapis.com/v1" # (line 10)` 

Your service URL can be located on the Azure portal, under your DICOM Service's Overview section.

---
(Optional) Obtain an access token for running the curl commands:

`token=$(az account get-access-token --resource=https://dicom.healthcareapis.azure.com --query accessToken --output tsv)`

The above az command can be installed as described [here.](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

For your reference curl command examples are also provided. To run them you need an authentication token passed to the command:

`./command_stow.sh $token`

This will show your changefeed (recent changes on the server):
`curl -X GET --header "Authorization: Bearer $token"  https://<workspacename-dicomservicename>.dicom.azurehealthcareapis.com/v<version of REST API>/changefeed`


---
Original tutorial can be found in the [Azure DICOM documentation](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicomweb-standard-apis-python)

The example DICOM images included in this repository are from [GitHub repository for Azure DICOM server](https://github.com/microsoft/dicom-server/tree/main/docs/dcms)
