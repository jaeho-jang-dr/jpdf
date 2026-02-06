# JPDF v1.1 - PDF/이미지 → 편집 가능 PPTX 변환기

PDF, PNG, JPG 파일을 편집 가능한 PPTX로 변환합니다.

## 기능

- **OCR**: Google Cloud Vision API로 정확한 한글/영문 텍스트 추출
- **Inpainting**: OpenCV TELEA 알고리즘으로 텍스트 영역 배경 자동 복원
- **PPTX 생성**: 깨끗한 배경 + 편집 가능한 텍스트 박스
- **웹 UI**: 드래그 앤 드롭 파일 업로드
- **다양한 포맷**: PDF, PNG, JPG 지원

## 설치

```bash
pip install -r requirements.txt
```

또는 패키지로 설치:

```bash
pip install -e .
```

## 설정

```bash
cp .env.example .env.local
# .env.local 편집하여 GOOGLE_VISION_API_KEY 입력
```

## 실행

### 웹 앱

```bash
python -m jpdf.app
# 브라우저에서 http://localhost:5000 접속
```

### CLI

```bash
# 패키지로 설치한 경우
jpdf input.pdf -o output.pptx

# 또는 모듈로 실행
python -m jpdf input.pdf -o output.pptx

# 이미지 변환
python -m jpdf image.png -o output.pptx

# 옵션
python -m jpdf input.pdf --font-family "Malgun Gothic" --font-size 20
```

### Python API

```python
from jpdf import JPDF

converter = JPDF(api_key="...")
pptx_path, page_count = converter.convert("slides.pdf")
```

## 변환 모드

| 모드 | 설명 |
|------|------|
| **수정 가능하게 만들기** | 텍스트 제거 → 배경 복원 → 편집 가능한 텍스트 박스 |
| **바로 만들기** | 원본 이미지 배경 + 텍스트 오버레이 |

## CLI 옵션

| 옵션 | 설명 | 기본값 |
|------|------|--------|
| `-o, --output` | 출력 파일 경로 | `{입력파일}_편집가능.pptx` |
| `--api-key` | Google Vision API 키 | 환경변수 |
| `--no-inpaint` | 텍스트 제거 안함 | False |
| `--font-family` | 폰트 | Arial |
| `--font-size` | 폰트 크기 고정 | 자동 |
| `--zoom` | 이미지 확대 비율 | 2.0 |

## 파일 구조

```
jpdf/
├── jpdf/                # Python 패키지
│   ├── __init__.py      # 패키지 초기화
│   ├── __main__.py      # python -m jpdf 진입점
│   ├── core.py          # JPDF 변환 엔진
│   ├── cli.py           # CLI 인터페이스
│   ├── app.py           # Flask 웹 서버
│   ├── templates/
│   │   └── index.html   # 웹 UI
│   └── static/
│       └── style.css    # 스타일
├── pyproject.toml       # 패키지 설정
├── requirements.txt
├── .env.example
└── README.md
```

## 라이선스

MIT License
