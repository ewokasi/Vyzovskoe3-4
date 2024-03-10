
function call_confirm(){

    confirm("Костяков Никита Андреевич 4134к")

}
function addrow(){
    let table = document.getElementById("table")
    var row = table.insertRow(5);
    var cell1 = row.insertCell(0);
    var cell2 = row.insertCell(1);
    var cell3 = row.insertCell(2);
    var cell4 = row.insertCell(3);
    var cell5 = row.insertCell(4);
    var cell6 = row.insertCell(5);
}

function changecolor(){
    if( document.getElementById("header").style.backgroundColor!="green"){
        document.getElementById("header").style.backgroundColor="green";
    }
    else{
        document.getElementById("header").style.backgroundColor= "#333";
    }
}

eventTarget.addEventListener("keydown", (event) => {
    if (event.isComposing || event.keyCode === 37) {//left arrow
        call_confirm();
    }
    if (event.isComposing || event.keyCode === 38) {//arrow up
        addrow();
    }if (event.isComposing || event.keyCode === 39) { //arrow right
        changecolor();
    }
});