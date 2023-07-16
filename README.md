# resume-api
<p align="center">
<img src=https://www.freeiconspng.com/uploads/resume-icon-png-10.png>
</p>

Build status: <br />
[![RESUME-API](https://github.com/jabbson/resume-api/actions/workflows/deploy.yml/badge.svg)](https://github.com/jabbson/resume-api/actions/workflows/deploy.yml)

**HOW TO USE:**
--
- Set a secret with the content of the [service account](https://cloud.google.com/iam/docs/service-accounts-create) json key (**GCP_SERVICE_ACCOUNT**)
- Set the following variables:
  - (**CLOUD_FUNCTION_NAME**): name of the Cloud Function to create
  - (**GCS_BUCKET_NAME**): name of the Cloud Storage bucket to create
  - (**GCS_FILE_NAME**): name of the file to save to the bucket
  - (**REGION**): the region where Cloud Function will be deployed
