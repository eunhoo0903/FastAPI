## 라우팅
> FastAPI에서 라우팅은 클라이언트로부터의 HTTP 요청을 적절한 함수나 메소드로 연결하는 과정을 의미한다.

### 기본 라우팅
- 기본적으로 HTTP GET 메소드를 사용한 라우팅
- 예시: 루트 URL(http://127.0.0.1:8000/)에 GET 요청시 "Hello, FastAPI" 응답 반환
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
```

### 경로 매개변수(Path Parameters)와 쿼리 매개변수(Query Parameters)
- 경로 매개변수: URL의 일부로 통합된 변수, 동적 값 처리에 사용
    * 예시: `/items/{item_id}` 에서 `{item_id}`는 경로 매개변수
    ```python
    @app.get("/items/{item_id}")
    def read_item(item_id):
        return {"item_id": item_id}
    ```

- 복수의 경로 매개변수 사용
    * 예시: `/users/{user_id}/items/{item_name}` 에서 `user_id`와 `item_name`은 경로 매개변수
    ```python
    @app.get("/users/{user_id}/items/{item_name}")
    def read_user_item(user_id, item_name):
        return {"user_id": user_id, "item_name": item_name}
    ```

- 쿼리 매개변수: URL의 `?` 이후에 정의되는 키-값 쌍, 필터링이나 정렬 등에 사용
    * 예시: `/items/?skip=5&limit=5` 에서 `skip`과 `limit`은 쿼리 매개변수
    ```python
    @app.get("/items/")
    def read_items(skip, limit):
        return {"skip": skip, "limit": limit}
    ```

### 테스트
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}

@app.get("/items/{item_id}")
def read_item(item_id):
    return {"item_id": item_id}

@app.get("/items/")
def read_items(skip=0, limit=10):
    return {"skip": skip, "limit": limit}
```