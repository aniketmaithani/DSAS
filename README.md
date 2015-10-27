# DSAS (DJANGO based STUDENT AUTHENTICATION SYSTEM)

``` The following system implements a basic API which allows "TOKEN" based authentication and allows user (student) to submit/view their personal details ```

# Modules Used 

 The following modules/frameworks are used 
```## Django 1.8.x [Version is updated as per new release]```
```## Django Rest Framework [Version is updated as per new release]```
```## Djoser ```

# API Endpoints 

The DSAS contains the following API endpoints (primarily): 

1. ```/auth/register/```

Data Type : application/json

Call Type : POST 


``` request:

username
password 

```

```response:

status: HTTP_201_CREATED (success)

data:

{{ User.USERNAME_FIELD }}

{{ User._meta.pk.name }}

{{ User.REQUIRED_FIELDS }} ```




2. ```/auth/login/``` 

Data Type : application/json

Call Type : POST 

```request:
username
password

```

```response:
status: HTTP_200_OK (success)

data:

auth_token ```




3. ```/auth/activate/```

Data Type : application/json

Call Type : POST

```request:
uid
token (obtained in step 2)
```

```response:
response

status: HTTP_200_OK (success)
```



4. ```/studentinfo``` (requires Authorization)

Authorization Type : Token Authorization | 

Headers : 
Authorization : Token <token_key>

Call Type : POST 

```request:
{
    "full_name": "a",
    "course": "a",
    "year": "2015",
    "passout_year": "2015",
    "aggregate_percentage": 76 (Integer Type Only)
}
```

```response:
{
    "full_name": "a",
    "course": "a",
    "year": "2015",
    "passout_year": "2015",
    "aggregate_percentage": 76 (Integer Type Only)
}```


    
``` GET CALL to /studentinfo also supported provided you have Token Key ``` 
