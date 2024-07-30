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
        + 웹 브라우저: `"http://127.0.0.1:8000/items/?q=1&q=2&q=3"` -> 결과: `{"q": [1, 2, 3]}`
    * **타입 불일치 시 에러 테스트**
        + 웹 브라우저: `"http://127.0.0.1:8000/items/?q=하나&q=둘&q=셋"` -> 결과: 타입 에러(정수가 아닌 문자열 입력)
    * **HTTP POST 요청 테스트**
        + `curl -X POST "http://127.0.0.1:8000/create-item/" -H "accept: application/json" -H "Content-Type: application/json" -d "{\"name\":1}"`
        + 결과: 서버에서 `{"name": 1}` 형태로 요청 본문 받고 반환

이러한 테스트는 FastAPI가 타입 힌트를 기반으로 유효성 검증을 어떻게 수행하는지 확인하는데 유용하다. 타입 힌트의 정확한 사용은 API의 안정성을 크게 향상시킨다.

### 타입 힌트 사용 가능한 데이터 타입
FastAPI에서 사용할 수 있는 파이썬 타입 힌트이다.

#### 기본 데이터 타입
- `int`: 정수
- `float`: 부동 소수점 수
- `str`: 문자열
- `bool`: 불리언 (True 또는 False)

#### 컬렉션 타입
- `List`: 예: `List[int]` (정수 리스트)
- `Tuple`: 예: `Tuple[str, int]` (문자열과 정수 튜플)
- `Dict`: 예: `Dict[str, float]` (문자열 키와 부동 소수점 값의 딕셔너리)
- `Set`: 예: `Set[bool]` (불리언 값의 세트)

#### 특수 타입
- `None`: 값 없음
- `Any`: 모든 타입 허용, 타입 검사 무시

#### `typing` 모듈의 고급 타입
- `Optional`: 예: `Optional[str]` (문자열 또는 None)
- `Union`: 예: `Union[int, str]` (정수 또는 문자열)

#### 예시: 복잡한 타입 힌트 조합
- `List[Dict[str, Union[int, str]]]`: 문자열 키와 정수 또는 문자열 값이 있는 딕셔너리의 리스트

FastAPI는 이러한 다양한 타입 힌트를 활용하여 요청 데이터의 형식을 검증하고, 응답 데이터를 적절한 형식으로 변환한다.
또한, 이를 통해 API 문서를 자동으로 생성할 수 있다.