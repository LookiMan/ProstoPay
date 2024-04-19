# ProstoPay

## Configuration:

**Create virtual environment**

`python -m venv "env"`

<hr>

**Activate virtual environment**

Linux: `source ./env/bin/activate`

Windows: `./env/Scripts/Activate.ps1`

<hr>

**Upgrade pip**

`python -m pip install --upgrade pip`

<hr>

**Install requirements:**

`python -m pip install -r requirements.txt`

<hr>

## Checks:

**Run static type checker:**

`pyright --project pyrightconfig.json`

**Run .flake8:**

`flake8`

## Tasks 1:

```
Implement own hashmap class (put, get methods are required).
write tests for this class.
add notes with argumentation for choosen implementation.
```

**Run main script:**

`python ./task_1/main.py`

**Run tests:**

`python -m unittest ./task_1/tests/test_hash_map.py`

## Task 2:

```
Write small service class with methods

get(user_id) → UserDTO
add(user: UserDTO)

signatures can be changed if you think it's needed for better implementation

UserDTO - pydantic model
users are stored in db.
assume you have method get_async_session, which returns AsyncSession sqlalchemy object to interact with db

write tests for that class

add notes with argumentation for choosen implementation
```

**Run tests:**

`python -m unittest ./task_2/tests/test_user_service.py`
