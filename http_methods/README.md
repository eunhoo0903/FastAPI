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

### 주요 HTTP 응답 코드

#### 2xx (성공)
- **200 ok**: 요청이 성공적으로 처리되었습니다.
    * 가장 일반적인 응답 코드이다.
- **201 Created**: 요청이 성공적으로 이루어져 새로운 리소스가 생성되었습니다.
    * 예를 들어, POST 요청을 통해 새로운 엔트리가 데이터베이스에 추가되었을 때 사용된다.
- **204 No Content**: 요청은 성공적이지만, 클라이언트에게 보내줄 콘텐츠는 없습니다.
    * 예를 들어, DELETE 요청이 성공적으로 처리되었을 때 사용될 수 있다.

#### 3xx (리다이렉션)
- **302 Moved Permanently**: 요청한 리소스가 영구적으로 새 위치로 이동했습니다.
    * 이 코드는 리소스의 URL이 변경되었을 때 사용된다.
- **302 Found**: 요청한 리소스가 일시적으로 다른 위치에 있습니다.
    * 리다이렉션을 위해 자주 사용된다.

#### 4xx (클라이언트 오류)
- **400 Bad Request**: 서버가 요청을 이해할 수 없습니다.
    * 잘못된 요청 구조나 파라미터 때문에 발생할 수 있다.    
- **401 Unauthorized**: 요청이 인증을 필요로 합니다.
    * 보통 로그인 하지 않은 사용자가 보호된 리소스에 접근하려 할 때 반환된다.
- **403 Forbidden**: 서버가 요청을 이해했으나, 권한이 없어 요청을 거부합니다.
- **404 Not Found**: 서버가 요청한 리소스를 찾을 수 없습니다.
    * URL 오류나 존재하지 않는 페이지에 대한 요청에서 흔히 발생한다.

#### 5xx (서버 오류)
- **500 Internal Server Error**: 서버 내부 오류로 인해 요청을 처리할 수 없습니다.
    * 가장 일반적인 서버 오류 응답이다.
- **503 Service Unavailable**: 서버가 일시적으로 요청을 처리할 수 없습니다.
    * 일반적으로 서버 과부하나 유지 관리로 인해 발생한다.