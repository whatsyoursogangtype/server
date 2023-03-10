# server

Applion page for server

<img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white">

- [초기 셋팅](#초기-셋팅) <br>
- [실행](#실행) <br>

## 초기 셋팅

### 1. 로컬 레포지토리 생성

```
git clone https://github.com/whatsyoursogangtype/server.git
```

### 2. 가상 환경 생성 및 실행

- Windows

```
cd server
python -m venv venv
source venv/Scripts/activate
pip install django
pip install -r requirements.txt
```

- Mac

```
cd server
python3 -m venv venv
source venv/bin/activate
pip3 install django
pip3 install -r requirements.txt
```

<br>

## 실행

### 1. 가상 환경 실행

위 초기 셋팅에서 진행했을 경우 넘어간다

- Windows

```
cd server
source venv/Scripts/activate
```

- Mac

```
cd server
source venv/bin/activate
```

### 2. 환경 변수 설정

manage.py가 있는 폴더 내에 .env 파일을 생성해 노션에 있는 환경변수 값을 넣어준다.
