function myName(){
    alert("Костяков Никита Андреевич, 4134к");
}

function tip(){
    imt = parseInt( document.getElementById('imt').value);
    if (imt<18){
        alert("Недостаток веса");
    }
    else if (imt >=18 && imt< 24){
        alert("Все в норме");
    }
    else {
        alert("Избыток веса");
    }
}


function sumup(){
    num1 = parseInt( document.getElementById('1st').value);
    num2 = parseInt( document.getElementById('2nd').value);
    num3 =num1 + num2;
    alert("Сумма: " + num3 );
}

myName();