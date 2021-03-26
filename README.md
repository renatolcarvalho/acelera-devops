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
echo $(curl -s __http://localhost:8888/ping/$RANDOM)
```

You should see __pong:__ followd by a random number as the output.
