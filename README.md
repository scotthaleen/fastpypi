
Example of simple private pypi package repo with fastapi and nginx

## Run

```
docker-compose up --build
```


## build package

```
cd package
poetry run build
```

## register package

```
cd package
curl -X 'POST' \
  'http://localhost:8080/api/v1/repo/package' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'f=@dist/fastpypi-package-0.1.0.tar.gz;type=application/x-gzip'
```

## install package
```
pip install -U --no-deps --trusted-host localhost --extra-index-url=http://localhost:8080/repo fastpypi-package
```


### Links

https://packaging.python.org/tutorials/packaging-projects/<br/>
https://python-poetry.org/

## Repo

http://localhost:8080/repo/

## Api

http://localhost:8080/api/docs/


