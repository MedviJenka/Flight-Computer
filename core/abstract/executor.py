from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Executor(ABC):

    @abstractmethod
    def execute(self) -> None: ...
