# Images backend

## Requirements

1. docker
2. docker-compose

## Tech/Framework used

1. python 3.9
2. django
3. djangorestframework
4. django-filter
5. django-storages
6. pillow
7. python-dotenv
8. pytest
9. boto3
10. OpenAPIv3
11. drf-spectacular


## Setting up dev environment

1. Create bucket in s3 (AWS) - make sure to turn off block all public access
2. Create and fill `.env` file (check `.envtemplate` file).
3. In terminal run `docker-compose up`
4. If everything is ok, your application should be available on host `http://127.0.0.1:8000/`. You should see swagger on main page.

## API endpoints
1. [GET] http://127.0.0.1:8000/api/images - returns paginated list of stored images
2. [GET] http://127.0.0.1:8000/api/images/<id> - returns single object 
3. [POST] http://127.0.0.1:8000/api/images/  - resize image according to given size, upload image on storage. Returns object of jsut uploaded iamge<br />
### Required fields: 
title - text<br />width - text<br />height - text<br />picture - file/image
### Suported image extensions:
1. jpg
2. jpeg
3. png
4. gif

## Tests

To run test type `pytest ...` # TODO: update this section!