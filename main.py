# Basic information about classes
class Test:
    def __init__(self, a_1: str, a_2: int, a_3: float):
        self.value_1 = a_1
        self.value_2 = a_2
        self.value_3 = a_3
        self.value_4 = 9

    def __str__(self):
        return f"Main data ==> {self.value_1} {self.value_2} {self.value_4}"


t1 = Test("This is test value_1", 4, 242.000)
print(f"Print results: {t1}")