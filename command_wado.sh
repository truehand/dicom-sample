curl --request GET "https://yourdicomurl.azurehealthcareapis.com/v1/studies/1.2.826.0.1.3680043.8.498.13230779778012324449356534479549187420" \
--header "Accept: multipart/related; type=\"application/dicom\"; transfer-syntax=*" \
--header "Authorization: Bearer $1" \
--output "suppressWarnings.txt"