# Deploy

## Using docker

1. Install docker - [install docker](https://docs.docker.com/get-docker/)
2. Run docker dekstop to start docker daemon if on windows
3. Build docker image
```bash
cd app
docker build . -t <image-name>
```
4. Run docker container
```bash
docker run --rm -it -p 5000:5000 <image-name>
```

## Using virtualenv


1. Install virtualenv
```bash
pip install virtualenv
```
2. Generate virtualenv
```bash
virtualenv venv
```
2. Run virtualenv
```bash
cd venv
Scripts/Acivate
```
3. Run app.py
```bash
cd ../app
python app.py
```