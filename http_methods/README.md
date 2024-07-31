## HTTP 메소드
> HTTP 메소드는 클라이언트가 서버에 특정 동작을 요청하는 방법을 정의한다. FastAPI에서는 이를 통해 요청의 의도를 명확히 하고 적절한 엔드포인트로 라우팅한다.

### HTTP 메소드 상세 설명
- **GET**
    * **사용처**: 서버로부터 정보를 요청
    * **특징**: 데이터 읽기 전용, 서버 상태 변경 없음
    * **예시**: 사용자 프로필, 게시글 목록 조회

- **POST**
    * **사용처**: 서버에 데이터 전송, 새 리소스 생성
    * **특징**: 데이터 서버에 제출, 주로 요청 본문에 데이터 포함
    * **예시**: 새 사용자 등록, 게시글 작성

- **PUT**
    * **사용처**: 지정된 리소스의 전체 업데이트
    * **특징**: 기존 리소스의 완전한 교체
    * **예시**: 사용자 프로필 전체 업데이트

- **DELETE**
    * **사용처**: 지정된 리소스 삭제
    * **특징**: 리소스 제거 지시, 성공시 접근 불가
    * **예시**: 계정 삭제, 게시글 제거

FastAPI는 다양한 HTTP 요청 처리를 위해 메소드별 라우팅 데코레이터(`@app.get()`, `@app.post()`, `@app.put()`, `@app.delete()` 등)를 제공한다.

### FastAPI 코드 예시
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
def read_items(skip: int = 0, limit: int = 10):
    return {"skip": skip, "limit": limit}

@app.post("/items/")
def create_item(item: dict):
    return {"item": item}

@app.put("/items/{item_id}")
def update_item(item_id: int, item: dict):
    return {"item_id": item_id, "update_item": item}

@app.delete("/items/{item_id}")
def delete_item(item_id: int):
    return {"message": f"Item {item_id} has been deleted"}
```
이 코드는 FastAPI로 간단한 CRUD(Create, Read, Update, Delete) 작업을 수행하는 예시이다.
