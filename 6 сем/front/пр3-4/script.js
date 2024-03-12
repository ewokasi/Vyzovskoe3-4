// Прототип Фигура
function Shape() {}

Shape.prototype.calculateArea = function() {
    throw new Error('Метод calculateArea должен быть переопределен в подклассе');
};

Shape.prototype.calculatePerimeter = function() {
    throw new Error('Метод calculatePerimeter должен быть переопределен в подклассе');
};

// Класс Прямоугольник
class Rectangle extends Shape {
    constructor(width, height) {
        super();
        this.width = width;
        this.height = height;
    }

    calculateArea() {
        return this.width * this.height;
    }

    calculatePerimeter() {
        return 2 * (this.width + this.height);
    }
}

// Класс Круг
class Circle extends Shape {
    constructor(radius) {
        super();
        this.radius = radius;
    }

    calculateArea() {
        return Math.PI * this.radius ** 2;
    }

    calculatePerimeter() {
        return 2 * Math.PI * this.radius;
    }
}

// Класс Студент
class Student {
    constructor(name, age, averageGrade) {
        this._name = name;
        this._age = age;
        this._averageGrade = averageGrade;
    }

    getName() {
        return this._name;
    }

    setName(name) {
        this._name = name;
    }

    getAge() {
        return this._age;
    }

    setAge(age) {
        this._age = age;
    }

    getAverageGrade() {
        return this._averageGrade;
    }

    setAverageGrade(averageGrade) {
        this._averageGrade = averageGrade;
    }
}

// Класс Калькулятор
class Calculator {
    static add(a, b) {
        return a + b;
    }

    static subtract(a, b) {
        return a - b;
    }

    static multiply(a, b) {
        return a * b;
    }

    static divide(a, b) {
        if (b === 0) {
            throw new Error('Деление на ноль невозможно');
        }
        return a / b;
    }
}
        // Создаем экземпляры классов и прототипа
    var rec_x = 5;
    var rec_y = 3;
    var rectangle = new Rectangle(rec_x, rec_y);

    var cir_rad = 4;
    var circle = new Circle(cir_rad);

    var student = new Student("Иванов", 20, 4.5);

    // Вычисляем площадь и периметр для прямоугольника
    document.getElementById("rectangleInfo").textContent = " со сторонами "+ rec_x+" на "+ rec_y;
    document.getElementById("rectangleArea").textContent = rectangle.calculateArea();
    document.getElementById("rectanglePerimeter").textContent = rectangle.calculatePerimeter();

    // Вычисляем площадь и периметр для круга
    document.getElementById("circleInfo").textContent =" с Радиусом "+ cir_rad;
    document.getElementById("circleArea").textContent = circle.calculateArea().toFixed(2);
    document.getElementById("circlePerimeter").textContent = circle.calculatePerimeter().toFixed(2);

    // Получаем информацию о студенте
    document.getElementById("studentName").textContent = student.getName();
    document.getElementById("studentAge").textContent = student.getAge();
    document.getElementById("studentAverageGrade").textContent = student.getAverageGrade();

    // Примеры математических операций
    document.getElementById("addResult").textContent = Calculator.add(5, 3);
    document.getElementById("subtractResult").textContent = Calculator.subtract(10, 7);
    document.getElementById("multiplyResult").textContent = Calculator.multiply(4, 6);
    document.getElementById("divideResult").textContent = Calculator.divide(12, 4);


