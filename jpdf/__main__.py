"""python -m jpdf 진입점"""
import sys
from .cli import main

sys.exit(main() or 0)
