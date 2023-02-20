from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Calculator(ABC):

    @abstractmethod
    def is_on(self) -> bool: ...

    @abstractmethod
    def is_off(self) -> bool: ...
