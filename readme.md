# Moodle - Git

## Run

``` bash

python main.py

```

## Main config
`./configs/man.json`

```json5
{
  "github":{...},
  "moodle":{...},
  "googleSheet":{...},
}

```

## GitHub

```json5
{
  "credentials": {
        "accessToken": "accessToken" /* accessToken for GitHub user */
        },
        "label": { /* config for PullRequest labels */
            "defaultTemplate": "#Moodle", /* key word for moodle labels */
            "defaultColor": "c4c", /* ddefault color label */
            "config": [
                [
                    [0, 30], /* from 0% to 30% (1% = (raw-min)/(max-min)) */
                    {
                        "color": "ff3d00",
                        "template": "Не сдали ({raw}/{max})", /* template, available variables: raw,min,max */
                        "description": "можно написать, но видно вроде только в настройках"
                    }
                ],
                ...
            ]
        }
}
```

## Moodle

```json5

{
    "baseUrl": "http://e.moevm.info", /* base url for requests */
    "credentials": {
        "username": "", /* optional, not used now  */
        "password": "", /* optional, not used now  */
        "token": "" /* access token */
    }
},
```

### How to get Moodle accessToken?

Request:

```bash
curl --location --request GET 'http://e.moevm.info/login/token.php?username=<username>&password=<password>&service=moodle_mobile_app'
```

Response:

```json5
{
    "token": "someaccesstoken", /* the value we need */
    "privatetoken": null
}
```

## Google Sheets


```json5

{
    "id": "", /* id of table  with users Names and Github logins */
        "headers": { /* table headers  */
            "fio": "ФИО",
            "email": "Email",
            "github": "github",
            "username": "username",
            "group": "Группа"
        }
},
```

## Run config

`./configs/run.json`

```json5
{
    "moodle": {
        "courseId": 47, /* course id */
        "quizId": 552 /* quiz id (lesson) */
    },
    "github": {
        "repo": "UserName/repo", /* link to github repo */
        "prRegex": "^(\\w*)_(lr1)$" /* Regex for PullRequest titles */
    }
}

```
