class Expression:
    __mathemetical_operations = {
        "^": lambda a, b: float(a) ** float(b),
        "*": lambda a, b: float(a) * float(b),
        "/": lambda a, b: float(a) / float(b),
        "+": lambda a, b: float(a) + float(b),
        "-": lambda a, b: float(a) - float(b)
    }

    __mathematical_operations_array = __mathemetical_operations.keys()

    def __init__(self, expression) -> None:
        if type(expression) == str:
            self.__expression = self.__create_array_from_expression(expression)
        else:
            self.__expression = expression

    def __str__(self) -> str:
        if len(self.__expression) <= 1:
            return str(self.__expression[0])
        
        return " ".join(self.__expression)
    
    def __create_array_from_expression(self, expression: str) -> list[str]:
        if len(expression) <= 1:
            return [expression]
        
        expression_array = []
        current_number = ""

        for i in range(len(expression)):
            char = expression[i]

            if char == "(":
                expression_array.append(char)
                continue

            if char not in self.__mathematical_operations_array and char != ")":
                current_number += char
                continue

            if expression[i-1] == ")":
                expression_array.append(char)
                continue

            expression_array.append(current_number)
            current_number = ""
            expression_array.append(char)
        
        if expression[-1] != ")":
            expression_array.append(current_number)

        return expression_array

    def __replace_brackets(self) -> None:
        expression_in_brackets = []
        is_in_brackets = False

        i = 0
        while i < len(self.__expression):
            current = self.__expression[i]

            if current == ")":
                if len(self.__expression) > i + 1:
                    if self.__expression[i+1] == ")":
                        expression_in_brackets.append(current)
                        self.__expression.pop(i)
                
                expression = Expression(expression_in_brackets)
                expression.calculate_expression()
                self.__expression[i] = str(expression)
                expression_in_brackets = []
                is_in_brackets = False
                i += 1
                continue

            if is_in_brackets:
                expression_in_brackets.append(current)
                self.__expression.pop(i)
                continue

            if current == "(":
                if is_in_brackets:
                    expression_in_brackets.append(current)
                
                is_in_brackets = True
                self.__expression.pop(i)
                continue

            i += 1
    
    def calculate_expression(self) -> None:
        self.__replace_brackets()

        i = 1
        while i < len(self.__expression):
            if self.__expression[i] == "^":
                self.__replace_with_result(i)
                continue

            i += 2

        i = 1
        while i < len(self.__expression):
            current = self.__expression[i]
            if current == "+" or current == "-":
                i += 2
                continue

            self.__replace_with_result(i)

        while len(self.__expression) > 1:
            self.__replace_with_result(index=1)

    def __replace_with_result(self, index: int):
        mathematical_function = self.__expression[index]
        result = self.__mathemetical_operations[mathematical_function](self.__expression[index-1], self.__expression[index+1])

        self.__expression[index] = result
        self.__expression.pop(index-1)
        self.__expression.pop(index)
