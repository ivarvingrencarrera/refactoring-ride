from abc import ABC, abstractmethod

from src.segment import Segment

class FareCalculator(ABC):
    @abstractmethod
    def calculate(self, segment: Segment) -> float:
        pass
