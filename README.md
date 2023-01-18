# Azure DICOM Service Python example to store (stow) and retrieve (wado) DICOMs

## What is this?
This is a sample Python code that can interact with the Azure DICOM Service. DICOM (Digital Imaging and Communications in Medicine) is the international standard to transmit, store, retrieve, print, process, and display medical imaging information, and is the primary medical imaging standard accepted across healthcare.

The script **stow_and_wado.py** will:
- test the connection between your client and the DICOM Service by requesting and printing the changefeed of your DICOM service
- deposit DICOM images from a study into the DICOM server (images are provided under the *images* folder) -- the **stow** part (**ST**ore **O**ver the **W**eb)
- and then retrieve instances under the same study stored on the DICOM server -- the **wado** part (**W**eb **A**ccess to **D**ICOM **O**bjects)

## How to get started

First step is to set up a DICOM Service in Azure: [Deploy DICOM](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/deploy-dicom-services-in-azure)

Next, [add your Azure user as a DICOM data owner after creating the service](https://learn.microsoft.com/en-us/azure/healthcare-apis/configure-azure-rbac#assign-roles-for-the-dicom-service)

In the main script, change the *base_url* variable with your service url (which you will obtain from the created service). 
Make sure to include the API version, **v1**, and to update the part `your_dicom_url` to reflect your service name, in the base url, as in:

`base_url = f"your_dicom_url.azurehealthcareapis.com/v1" # (line 10)` 

Your service URL can be located on the Azure portal, under your DICOM Service's Overview section.

In this example we are going to use the Azure CLI (command line interface) credentials for authentication. This was made possible by selecting the fourth credential mechanism in the `credential` variable on lines 19-20 (`credential.credentials[3]` in the code). The order of credentials available in the `credential` list may differ from one client to the other, so make sure you are using the CLI one by printing the credentials list first. Once we do that, then we can run `az login` in a terminal window and get authenticated on a browser window that will open, prior to running our Python script in the same terminal.

Finally, run the main Python script **stow_and_wado.py**

---
## Dependencies

Unless you already have az, you need to install it. above az command can be installed as described [here.](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt)

In your local environment, preferably create a new conda environment, and then install dependencies listed under **requirements.txt**:

`pip install -r requirements.txt` 

## Optional 

Obtain an access token for running the curl commands:

`token=$(az account get-access-token --resource=https://dicom.healthcareapis.azure.com --query accessToken --output tsv)`

For your reference curl command examples are also provided. To run them you need an authentication token passed to the command:

`./command_stow.sh $token`

This will show your changefeed (recent changes on the server):
`curl -X GET --header "Authorization: Bearer $token"  https://<workspacename-dicomservicename>.dicom.azurehealthcareapis.com/v<version of REST API>/changefeed`


---
## More details and documentation
Original tutorial can be found in the [Azure DICOM documentation](https://learn.microsoft.com/en-us/azure/healthcare-apis/dicom/dicomweb-standard-apis-python)

The example DICOM images included in this repository are from [GitHub repository for Azure DICOM server](https://github.com/microsoft/dicom-server/tree/main/docs/dcms)
