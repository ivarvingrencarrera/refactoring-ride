from abc import ABC, abstractmethod

from src.segment import Segment


class FareCalculatorHandler(ABC):
    @abstractmethod
    def calculate(self, segment: Segment) -> float:
        pass
