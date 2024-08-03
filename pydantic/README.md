## Pydantic 모델
> FastAPI에서 Pydantic 모델은 데이터 유효성 검사, 직렬화, 역직렬화를 위해 사용되는 클래스이다.

### Pydantic 특징
- Pydantic 라이브러리를 활용해 정의되며, FastAPI의 경로 작업 함수에서 요청 및 응답 데이터의 타입을 명시하는데 주로 사용
- 이 모델들은 타입 힌트를 기반으로 하여 데이터 형태와 유효성을 선언적으로 정의할 수 있게 해주며, 자동 문서 생성, 요청 검증, 응답 모델링에 활용
- Pydantic 모델을 사용함으로써 개발자는 데이터에 대한 추가적인 검증 로직을 적게 작성하면서도, 강력한 타입 안전성과 함께 더 깔끔하고 유지보수가 용이한 코드를 구성

### 데이터 검증 (Data Validation)
- **정의**: 사용자나 시스템이 보내는 데이터의 형식과 값을 확인하는 과정
- **예시**: 금액 입력 시 문자열 대신 숫자 사용
- **목적**: 잘못된 데이터 처리 방지, 버그 및 문제 예방

### 데이터 직렬화 (Data Serialization)
- **정의**: 복잡한 데이터 구조를 바이트나 문자열로 변환하는 과정
- **역직렬화**: 문자열/바이트를 원래 데이터 구조로 변환
- **목적**: 서로 다른 시스템 간의 데이터 교환 용이성 제공

### Pydantic 모델의 중요성
- FastAPI에서는 Pydantic 모델 사용을 권장
- **이유**:
    * 데이터 검증과 직렬화를 통해 API 정확성 및 안전성 향상
    * HTTP POST 메소드 같은 데이터 요청에 효과적

### Pydantic 모델과 FastAPI 코드 예제
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel): # Pydantic 모델 정의
    name: str
    price: float
    is_offer: bool = None

@app.post("/items/")
def create_item(item: Item):
    return {"item": item.dict()} # Pydantic 모델을 API에 사용
```