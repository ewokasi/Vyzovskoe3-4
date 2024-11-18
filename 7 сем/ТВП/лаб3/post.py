class PostSystem:
    def __init__(self, initial_string, productions, alphabet):
        self.string = initial_string  # Начальная строка
        self.productions = productions  # Множество продукций (правил)
        self.alphabet = alphabet  # Алфавит символов

    def apply_production(self, production):
        # Проверяем, можно ли применить правило
        lhs, rhs = production
        if lhs in self.string:
            # Применяем правило и возвращаем результат
            self.string = self.string.replace(lhs, rhs, 1)
            return True
        return False

    def run(self, output_file):
        with open(output_file, 'w', encoding='utf-8') as f:
            while True:
                f.write(f"Текущая строка: {self.string}\n")
                applied = False
                
                for production in self.productions:
                    # Пробуем применить правило
                    if self.apply_production(production):
                        f.write(f"Применено правило: {production[0]} -> {production[1]}\n")
                        applied = True
                        break
                
                # Если ни одно правило не было применено, заканчиваем
                if not applied:
                    f.write("Достигнут конец вывода\n")
                    break

def read_file(filename):
    with open(filename, 'r') as f:
        return f.read().strip()

def read_productions(filename):
    productions = []
    with open(filename, 'r') as f:
        for line in f:
            lhs, rhs = line.strip().split("->")
            productions.append((lhs.strip(), rhs.strip()))
    return productions

def main():
    # Читаем начальную строку, алфавит и правила
    initial_string = read_file('input_string.txt')
    alphabet = read_file('alphabet.txt').split()
    productions = read_productions('productions.txt')

    # Проверка символов начальной строки
    for symbol in initial_string:
        if symbol not in alphabet:
            raise Exception(f"Символ '{symbol}' не в алфавите")

    # Запуск системы Поста
    post_system = PostSystem(initial_string, productions, alphabet)
    post_system.run('output.txt')

if __name__ == "__main__":
    main()
