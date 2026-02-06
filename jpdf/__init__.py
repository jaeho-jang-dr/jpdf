"""
JPDF - PDF/이미지 → 편집 가능 PPTX 변환기

Google Cloud Vision OCR + OpenCV Inpainting을 사용하여
PDF/이미지에서 텍스트를 추출하고, 배경을 복원한 후
편집 가능한 텍스트 박스로 PPTX를 생성합니다.

Usage:
    from jpdf import JPDF
    converter = JPDF(api_key="...")
    pptx_path, page_count = converter.convert("slides.pdf")
"""
from pathlib import Path

# .env.local 로드
try:
    from dotenv import load_dotenv
    for env_path in [
        Path.cwd() / '.env.local',
        Path.cwd() / '.env',
        Path(__file__).parent.parent / '.env.local',
        Path(__file__).parent.parent / '.env',
    ]:
        if env_path.exists():
            load_dotenv(env_path)
            break
    else:
        load_dotenv()
except ImportError:
    pass

__version__ = "1.1.0"


def __getattr__(name):
    """Lazy import — core 모듈은 실제 사용 시에만 로드"""
    from . import core
    return getattr(core, name)


__all__ = [
    '__version__',
    'JPDF',
    'TextBlock',
    'PageData',
    'SUPPORTED_FONTS',
    'convert_images_to_pptx',
]
