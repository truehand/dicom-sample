echo $1
curl --location --request POST "https://your_dicom_url.azurehealthcareapis.com/v1.0/studies/1.2.826.0.1.3680043.8.498.13230779778012324449356534479549187420" \
--header "Accept: application/dicom+json"  \
--header "Content-Type: multipart/related; type=\"application/dicom\"" \
--header "Authorization: Bearer $1" \
--form "file1=@./images/red-triangle.dcm;type=application/dicom" \
--trace-ascii "trace.txt"