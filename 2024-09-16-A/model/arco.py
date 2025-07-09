from dataclasses import dataclass
@dataclass
class Arco:
    id1: str
    id2: str
    peso :int

    def __str__(self):
        return f"{self.id1},{self.id2},{self.peso}"