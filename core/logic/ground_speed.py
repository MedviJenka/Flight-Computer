from dataclasses import dataclass
from typing import Optional
from core.abstract.executor import Executor
from core.modules.modules import read_json, log


@dataclass
class DataInput:

    distance: Optional[float or int]
    time: Optional[float or int]
    GS: Optional[float]


class GroundSpeedCalculatorLogic:

    @staticmethod
    def get_ground_speed(distance: float, time: int) -> float:
        ground_speed = distance / time * 60
        log(text=f'ground speed is {ground_speed}')
        return ground_speed


@dataclass
class ExecuteCalculateGroundSpeed(Executor, GroundSpeedCalculatorLogic):

    def execute(self) -> None:
        data = DataInput(**read_json('data', 'GS'))
        self.get_ground_speed(distance=data.distance,
                              time=data.time)


def app() -> None:
    calc = GroundSpeedCalculatorLogic()
    print(calc.get_ground_speed(90, 60))


if __name__ == '__main__':
    app()
