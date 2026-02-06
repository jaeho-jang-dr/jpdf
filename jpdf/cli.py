#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""JPDF CLI"""
import sys
import argparse

from .core import __version__, JPDF


def main():
    parser = argparse.ArgumentParser(
        prog="jpdf",
        description=f"JPDF v{__version__} - PDF/이미지 → 편집 가능 PPTX 변환기",
        epilog="예시: jpdf slides.pdf -o output.pptx"
    )
    parser.add_argument("input_path", help="입력 파일 (PDF, PNG, JPG)")
    parser.add_argument("-o", "--output", help="출력 PPTX 경로")
    parser.add_argument("--api-key", help="Google Vision API 키")
    parser.add_argument("--no-inpaint", action="store_true", help="텍스트 제거 안함")
    parser.add_argument("--zoom", type=float, default=2.0, help="확대 비율 (기본: 2.0)")
    parser.add_argument("--padding", type=int, default=10, help="패딩 (기본: 10)")
    parser.add_argument("--inpaint-radius", type=int, default=7, help="Inpaint 반경 (기본: 7)")
    parser.add_argument("--font-size", type=int, help="폰트 크기 고정")
    parser.add_argument("--font-family", default='Arial', help="폰트 (기본: Arial)")
    parser.add_argument("-v", "--version", action="version", version=f"JPDF v{__version__}")

    args = parser.parse_args()

    try:
        converter = JPDF(args.api_key)
        converter.convert(
            args.input_path,
            args.output,
            inpaint=not args.no_inpaint,
            zoom=args.zoom,
            padding=args.padding,
            inpaint_radius=args.inpaint_radius,
            font_size=args.font_size,
            font_family=args.font_family
        )
    except Exception as e:
        print(f"오류: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
