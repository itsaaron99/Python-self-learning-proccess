"""
Data model of Application
A standard contract between scipts and controller
"""

from dataclasses import dataclass

@dataclass
class AppConfig:
    package_name: str