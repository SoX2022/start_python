class Calc:
    persent_queue = list()
    math_queue = list()
    formula = list()

    def __init__(self, user_input = ['1', '+', '1']):
        self.reset()
        self.formula = user_input
        self.float_elements()
        self.calculation_queue()
        self.int_result()


    def simple_math(self, a, operator, b):
        match operator:
            case '+':
                return a + b
            case '-':
                return a - b
            case '*':
                return a * b
            case '/':
                return a / b


    def percentage_transformation(self, index):
        self.formula[index - 1] /=  100

        if self.formula[index-2] in ('+', '-'):
            self.formula[index - 1] = self.simple_math(1, self.formula[index-2], self.formula[index-1])
            self.formula[index - 2] = '*'

        self.formula.pop(index)


    def float_elements(self):
        for i, element in enumerate(self.formula):
            try:
                if float(element):
                    self.formula[i] = float(element)
            except:
                pass


    def int_result(self):
        if self.formula[0] % 1 == 0:
            self.formula[0] = int(self.formula[0])
        else:
            print('не удалось преобразовать в int')


    def calculation_queue(self):
        for i, element in enumerate(self.formula):
            if element == '%':
                self.persent_queue.append(i)

        for i, element in enumerate(self.formula):
            if element in ('*', '/'):
                self.math_queue.append(i)

        for i, element in enumerate(self.formula):
            if element in ('+', '-'):
                self.math_queue.append(i)

        self.calculation()


    def queue_to_calculate(self, queue, shift):
        for element in queue:
            if shift == 1:
                self.percentage_transformation(element)
            else:
                self.formula[element - 1] = self.simple_math(self.formula[element - 1], self.formula[element], self.formula[element + 1])
                self.formula.pop(element)
                self.formula.pop(element)
            
            for i, number in enumerate(self.math_queue):
                if number > element:
                   self.math_queue[i] -= shift
            
            for i, number in enumerate(self.math_queue):
                if number > element:
                    self.math_queue[i] -= shift


    def calculation(self):
        self.queue_to_calculate(self.persent_queue, 1)
        self.queue_to_calculate(self.math_queue, 2)


    def reset(self):
        self.persent_queue.clear()
        self.math_queue.clear()
        self.formula.clear()