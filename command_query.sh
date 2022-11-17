curl --request GET "https://your_dicom_url.azurehealthcareapis.com/v1/studies?StudyInstanceUID=1.2.826.0.1.3680043.8.498.13230779778012324449356534479549187420" \
--header "Accept: application/dicom+json" \
--header "Authorization: Bearer $1"