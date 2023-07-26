from dataclasses import dataclass

@dataclass
class CFToken:
    type: str
    value: str
    line: int
    column: int
