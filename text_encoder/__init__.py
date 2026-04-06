"""
text-encoder - Encode text to base64, hex, and other formats

Part of Viprasol Utilities: https://viprasol.com
"""

__version__ = "0.1.0"
__author__ = "Viprasol"
__email__ = "hello@viprasol.com"

from .core import TextEncoder, encode, process, main

__all__ = ["TextEncoder", "encode", "process", "main"]
