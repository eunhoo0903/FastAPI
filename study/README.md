# FastAPI 공부하기

## 라우팅
> FastAPI에서 라우팅은 클라이언트로부터의 HTTP 요청을 적절한 함수나 메소드로 연결하는 과정을 의미한다.

### 기본 라우팅
- 기본적으로 HTTP GET 메소드를 사용한 라우팅
- 예시: 루트 URL(http://127.0.0.1:8000/)에 GET 요청시 "Hello, FastAPI" 응답 반환
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, FastAPI"}
```

### 경로 매개변수(Path Parameters)와 쿼리 매개변수(Query Parameters)
- 경로 매개변수: URL의 일부로 통합된 변수, 동적 값 처리에 사용
    * 예시: `/items/{item_id}` 에서 `{item_id}`는 경로 매개변수
    ```
    @app.get("/items/{item_id}")
    def read_item(item_id):
        return {"item_id": item_id}
    ```

- 복수의 경로 매개변수 사용
    * 예시: `/users/{user_id}/items/{item_name}` 에서 `user_id`와 `item_name`은 경로 매개변수
    ```
    @app.get("/users/{user_id}/items/{item_name}")
    def read_user_item(user_id, item_name):
        return {"user_id": user_id, "item_name": item_name}
    ```

- 쿼리 매개변수: URL의 `?` 이후에 정의되는 키-값 쌍, 필터링이나 정렬 등에 사용
    * 예시: `/items/?skip=5&limit=5` 에서 `skip`과 `limit`은 쿼리 매개변수
    ```
    @app.get("/items/")
    def read_items(skip, limit):
        return {"skip": skip, "limit": limit}
    ```

#### 테스트
```
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

## 타입 힌트
> 타입 힌트(Type Hint)는 변수나 함수의 예상되는 데이터 타입을 명시적으로 표시하는 프로그래밍 기술이다.
> FastAPI는 이를 활용하여 요청의 유효성을 검증하고, 적절한 데이터 처리를 도와준다.

### 기본 타입 힌트 사용
- 목적: 경로나 쿼리 매개변수에 타입을 지정하여 자동 검증
- 예시:
    * 경로 매개변수 예시: `@app.get("/items/{item_id}")` 에서 `item_id: int`
    * 쿼리 매개변수 예시: `@app.get("/items/")` 에서 `data: str = "funcoding"`
```
from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id,}

@app.get("/items/")
def read_items(data: str = "funcoding"):
        return {"data": data}
```
- 웹 브라우저 테스트: 
    * `http://127.0.0.1:8000/items/123` -> 출력: `{"item_id": 123}`
    * `http://127.0.0.1:8000/items/fun` -> 오류: `item_id`가 int가 아님
    * `http://127.0.0.1:8000/getdata/?data=somequery` -> 출력: `{"data": "somequery"}`
    * `http://127.0.0.1:8000/getdata/` -> 출력: `{"data": "funcoding"}`
    * `http://127.0.0.1:8000/getdata/?data=1.1` -> 출력: `{"data": "1.1"}` (문자열로 처리)

### 고급 타입 힌트 사용
- 목적: `typing` 모듈의 `List`, `Dict` 등을 사용하여 복잡한 데이터 구조 표현
- 예시: 
    * 리스트 자료형 쿼리 매개변수: `List[int] = Query([])`
    * 딕셔너리 자료형 요청 본문: `item: Dict[str, int]`
```
from fastapi import FastAPI, Query
from typing import List, Dict

app = FastAPI()

@app.get("/items/")
async def read_items(q: List[int] = Query([])):
    return {"q": q}

@app.post("/create-item/")
async def create_item(item: Dict[str, int]):
    return item
```
`Query`는 쿼리 매개변수의 기본값 설정 및 유효성 검사에 사용된다. `Query([])`는 매개변수가 필수가 아니며, 기본값으로 빈 리스트를 설정한다. List 타입 힌트는 반드시 `Query()`와 함께 사용해야 한다.

#### 웹 브라우저 및 HTTP 클라이언트 테스트
- 목적: FastAPI에서 타입 힌트를 사용하여 데이터 유효성을 검증하는 방법 시연
- 예시 및 결과:
    * **List 타입 쿼리 매개변수 테스트**
        + `curl "http://127.0.0.1:8000/items/?q=1&q=2&q=3"` 실행
        + 웹 브라우저: `"http://127.0.0.1:8000/items/?q=1&q=2&q=3"` -> 결과: `{"q": [1,2,3]}`
    * **타입 불일치 시 에러 테스트**
        + 웹 브라우저: `"http://127.0.0.1:8000/items/?q=하나&q=둘&q=셋"` -> 결과: 타입 에러(정수가 아닌 문자열 입력)
    * **HTTP POST 요청 테스트**
        + `curl -X POST "http://127.0.0.1:8000/create-item/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":1}"`
        + 결과: 서버에서 `{"name": 1}` 형태로 요청 본문 받고 반환

이러한 테스트는 FastAPI가 타입 힌트를 기반으로 유효성 검증을 어떻게 수행하는지 확인하는데 유용하다. 타입 힌트의 정확한 사용은 API의 안정성을 크게 향상시킨다.