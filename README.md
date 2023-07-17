# resume-api
<p align="center">
<img src=https://www.freeiconspng.com/uploads/resume-icon-png-10.png>
</p>

Build status: <br />
[![RESUME-API](https://github.com/jabbson/resume-api/actions/workflows/deploy.yml/badge.svg)](https://github.com/jabbson/resume-api/actions/workflows/deploy.yml) <br />
[![CLEANUP](https://github.com/jabbson/resume-api/actions/workflows/cleanup.yml/badge.svg)](https://github.com/jabbson/resume-api/actions/workflows/cleanup.yml)

**HOW TO USE:**
--
- Fork the repository to have your own copy of the code
- Provision the [service account](https://cloud.google.com/iam/docs/service-accounts-create) in your GCP project
- Set the github secret (`GCP_SERVICE_ACCOUNT`) with the content of the service account json key
- Set the following github variables:
  - (`CLOUD_FUNCTION_NAME`): name of the Cloud Function to create
  - (`GCS_BUCKET_NAME`): name of the Cloud Storage bucket to create
  - (`GCS_FILE_NAME`): name of the file to save to the bucket
  - (`REGION`): the region where Cloud Function will be deployed

**(OPTIONAL) Push Notification via [Pushover](https://pushover.net/):**
--
If you would like to run a test on successful build, add the following variable:
- set the variable (`RUN_TESTS`) to `true`

If you would like to get push notifications on successful build or cleanup, add the following secrets and the variable:
- set the secret (`NOTIFY_TOKEN`) to match your pushover key token
- set the secret (`NOTIFY_USER`) to match your pushover user token
- set the variable (`NOTIFY`) to `true`
