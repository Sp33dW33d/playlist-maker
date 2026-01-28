from dataclasses import dataclass
from pathlib import Path

@dataclass
class AudioFile:
    path: Path 
    original_name: str
    normalized_name: str
    duration: float

@dataclass
class Track:
    original_name: str
    normalized_name: str
    duration: float
    artist: str