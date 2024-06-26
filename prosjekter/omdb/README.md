# Deploy

> First set up /app/configs/settings.py by adding the file and adding the following code

```python
key="" #your key as a string
url=f"http://www.omdbapi.com/?apikey={key}"
```

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

3. Run virtualenv

```bash
cd venv
Scripts/Acivate
```

4. Run app.py

```bash
cd ../app
pip install -r requirements.txt
python app.py
```
