from dataclasses import dataclass, field
@dataclass
class Punteggio:
    driverId: int
    position: int
    circuitId: int
    def __hash__(self):
        return hash((self.driverId, self.position))

    def __eq__(self, other):
        return (self.driverId == other.driverId
                and self.position == other.position
                and self.circuitId == other.circuitId)