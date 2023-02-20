import tkinter as tk
from dataclasses import dataclass
from core.logic.ground_speed import DataInput, GroundSpeedCalculatorLogic, ExecuteCalculateGroundSpeed


@dataclass
class CalculatorUI(GroundSpeedCalculatorLogic):
    root = tk.Tk()
    root.title("Calculator")
    expression = ""
    display = tk.Entry(root, width=25, font=("Arial", 16))
    calculation = ExecuteCalculateGroundSpeed()

    def __post_init__(self):

        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        self.create_button("7", 4, 0)
        self.create_button("8", 4, 1)
        self.create_button("9", 4, 2)

        self.create_button("4", 3, 0)
        self.create_button("5", 3, 1)
        self.create_button("6", 3, 2)

        self.create_button("*", 2, 3)

        self.create_button("1", 2, 0)
        self.create_button("2", 2, 1)
        self.create_button("3", 2, 2)
        self.create_button("-", 3, 3)

        self.create_button(".", 1, 1)
        self.create_button("C", 1, 2)
        self.create_button("+", 1, 3)

        self.create_button(".", 5, 0)
        self.create_button("0", 5, 1)
        self.create_button("=", 5, 1, column_span=4)

        self.root.mainloop()

    def create_button(self, text: str, row: int, col: int, column_span=1):
        button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 16),
                           command=lambda: self.button_click(text))
        button.grid(row=row, column=col, columnspan=column_span, padx=5, pady=5)

    def button_click(self, text):
        match text:
            case "C":
                self.expression = ""
            case "=":
                try:
                    # self.expression = str(eval(self.expression))
                    self.expression = str(eval(str(self.calculation.execute())))
                except Exception as e:
                    self.expression = "Error"
                    raise e
            case _:
                self.expression += text

        self.display.delete(0, tk.END)
        self.display.insert(0, self.expression)


if __name__ == '__main__':
    CalculatorUI()
