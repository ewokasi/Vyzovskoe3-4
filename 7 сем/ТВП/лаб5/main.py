class State:
    def __init__(self, is_accept=False):
        self.transitions = {}
        self.is_accept = is_accept

    def add_transition(self, symbol, state):
        if symbol not in self.transitions:
            self.transitions[symbol] = []
        self.transitions[symbol].append(state)


class NFA:
    def __init__(self):
        self.start_state = None
        self.accept_state = None

    @staticmethod
    def create_automaton_from_regex(regex):
        stack = []  # Стек для хранения промежуточных автоматов
        i = 0

        while i < len(regex):
            char = regex[i]

            if char == '|':
                # Если встретили оператор '|', извлекаем два автомата из стека
                if len(stack) < 2:
                    raise ValueError(f"Недостаточно элементов в стеке для обработки '|'. Стек: {stack}")

                right = stack.pop()  # Автомат для правой части
                left = stack.pop()   # Автомат для левой части

                # Новый старт и финальные состояния
                start = State()
                accept = State(is_accept=True)

                # Подключаем альтернативы
                start.add_transition("", left.start_state)
                start.add_transition("", right.start_state)
                left.accept_state.add_transition("", accept)
                right.accept_state.add_transition("", accept)

                # Создаем новый автомат и помещаем его в стек
                nfa = NFA()
                nfa.start_state = start
                nfa.accept_state = accept
                stack.append(nfa)

            elif char == '(':
                # Начало подвыражения в скобках
                stack.append('(')

            elif char == ')':
                # Завершение подвыражения, извлекаем автомат
                if len(stack) < 2 or stack[-2] != '(':
                    raise ValueError(f"Ошибка: Не закрыты скобки в регулярном выражении. Стек: {stack}")
                # Убираем '('
                stack.pop()  # Убираем открывающую скобку
                nfa = stack.pop()  # Извлекаем автомат, который строится внутри скобок
                stack.append(nfa)  # Возвращаем подавтомат обратно в стек

            else:
                # Простой символ: создаем автомат для этого символа
                start = State()
                accept = State(is_accept=True)
                start.add_transition(char, accept)

                nfa = NFA()
                nfa.start_state = start
                nfa.accept_state = accept
                stack.append(nfa)

            i += 1

        # После того как обработали все символы, в стеке остался один автомат
        if len(stack) != 1:
            raise ValueError(f"Некорректное регулярное выражение. Стек: {stack}")
        return stack[-1]

    def to_transition_matrix(self):
        state_list = []
        state_map = {}

        def add_state(state):
            if state not in state_map:
                state_id = len(state_map)
                state_map[state] = state_id
                state_list.append(state)
            return state_map[state]

        add_state(self.start_state)
        matrix = {}
        for state in state_list:
            state_id = add_state(state)
            matrix[state_id] = {}
            for symbol, transitions in state.transitions.items():
                matrix[state_id][symbol] = [add_state(t) for t in transitions]
        return matrix


# Чтение регулярного выражения из файла
with open("input.txt", "r") as f:
    regex = f.read().strip()

# Построение КНА из регулярного выражения
try:
    nfa = NFA.create_automaton_from_regex(regex)

    # Получение автоматной матрицы
    transition_matrix = nfa.to_transition_matrix()

    # Получаем уникальные символы, которые встречаются в переходах
    symbols = sorted(set(sym for trans in transition_matrix.values() for sym in trans))

    # Запись автоматной матрицы в файл
    with open("output.txt", "w", encoding="utf-8") as f:
        # Заголовок таблицы
        f.write("State" + "| ".join(symbols) + "\n")
        f.write("------" + "----" * len(symbols) + "\n")
        
        # Запись переходов для каждого состояния
        for state, transitions in transition_matrix.items():
            f.write(f"{state} | ")
            for symbol in symbols:
                # Для каждого символа выводим переходы
                if symbol in transitions:
                    f.write(",".join(map(str, transitions[symbol])) + "| ")
                else:
                    f.write(" | ")  # Если переходов нет для этого символа
            f.write("\n")
except ValueError as e:
    print(f"Ошибка: {e}")
