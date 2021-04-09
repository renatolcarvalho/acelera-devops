# Simple API for showcase DevOps techiniques

## How to run it locally

You'll need to have Docker installed. 

After being sure you have Docker properly settup, simple run the following commands:

```shell
docker build . -t acelera-devops
docker run -d -e PORT=8888 -p 8888:8888 acelera-devops
```

If it works, you'll be able to check it with 

```shell
echo $(curl -s http://localhost:8888/ping/$RANDOM)
```

You should see __pong:__ followed by a random number as the output.


## Google Build Steps

### Services

- Google Run
- Google Build
- Google Artefacts Registry

1. Install Python
2. Install GCloud CLI
3. Initializing the gcloud sdk
    - `gcloud init`
4. Creating new Docker repository
    - `	gcloud artifacts repositories create quickstart-docker-repo --repository-format=docker --location=us-central1 --description="Docker repository"`
5. Retrieving the project id
    - `gcloud config get-value project`
    - "acelera-308720"
6. Create yaml pipeline
    - Verify cloudbuild.yaml file.
7. Send the yaml to google build.
    - `gcloud builds submit --config cloudbuild.yaml`
8. Install Cloud Build in GitHub
    - Using connect to repository from Google build dashboard.
9. Create google run to read from the artifacts and configure the continuous delivery.

Force build.
