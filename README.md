# resume-api
<p align="center">
<img src=https://www.freeiconspng.com/uploads/resume-icon-png-10.png>
</p>

Build status: <br />
[![RESUME-API](https://github.com/jabbson/resume-api/actions/workflows/deploy.yml/badge.svg)](https://github.com/jabbson/resume-api/actions/workflows/deploy.yml)

**HOW TO USE:**
--
- Set the secret (`GCP_SERVICE_ACCOUNT`) with the content of the [service account](https://cloud.google.com/iam/docs/service-accounts-create) json key
- Set the following variables:
  - (`CLOUD_FUNCTION_NAME`): name of the Cloud Function to create
  - (`GCS_BUCKET_NAME`): name of the Cloud Storage bucket to create
  - (`GCS_FILE_NAME`): name of the file to save to the bucket
  - (`REGION`): the region where Cloud Function will be deployed

**(OPTIONAL) Push Notification via [Pushover](https://pushover.net/):**
--
If you would like to get push notifications on successful build, add the following secrets and a variable:
- set the secret (`NOTIFY_TOKEN`) to match your pushover key token
- set the secret (`NOTIFY_USER`) to match your pushover user token
- set the variable (`RUN_TESTS`) to `true`
