
document.getElementById('saveBtn').addEventListener('click', function() {
    var name = document.getElementById('nameInput').value;
    document.cookie = "username=" + name;
    document.getElementById('username').textContent = name;
});

// Проверяем, есть ли сохраненное имя пользователя в cookies
var username = getCookie("username");
if (username) {
    document.getElementById('username').textContent = username;
}

// Подсчитываем и отображаем количество посещений
var visitCount = localStorage.getItem('visitCount');
visitCount = visitCount ? parseInt(visitCount) + 1 : 1;
localStorage.setItem('visitCount', visitCount);
document.getElementById('visitCount').textContent = visitCount;

// Функция для получения значения cookie по имени
function getCookie(name) {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
        var cookie = cookies[i].trim();
        if (cookie.indexOf(name + "=") === 0) {
            return cookie.substring(name.length + 1, cookie.length);
        }
    }
    return "";
}

// Генерируем случайное число от 1 до 100
var secretNumber = Math.floor(Math.random() * 100) + 1;

// Обработчик для кнопки "Угадать"
document.getElementById('guessBtn').addEventListener('click', function() {
    var guess = parseInt(document.getElementById('guessInput').value);
    var message = document.getElementById('message');
    
    if (guess === secretNumber) {
        message.textContent = "Поздравляем! Вы угадали число!";
        sessionStorage.removeItem('secretNumber'); // Очищаем sessionStorage
        secretNumber = Math.floor(Math.random() * 100) + 1; // Генерируем новое число
    } else if (guess < secretNumber) {
        message.textContent = "Загаданное число больше, чем ваше предположение.";
    } else {
        message.textContent = "Загаданное число меньше, чем ваше предположение.";
    }
});

