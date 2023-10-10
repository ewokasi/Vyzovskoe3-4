function add_row(id, name, cost){
    if (id%2==0){
        style = 'style= "background-color: white"'
    }
    else{
        style = 'style= "background-color: lightgray"'
    }
        
    return  ("<tr "+style+"><td style='text-align: center'>"+id+"</td><td style='text-align: left'>"+name+"</td><td style='text-align: right'>"+cost+"</td></tr>")
}


data = [["яблоко", "100"],
        ["груша", "300"],
        ["мандарин", "10"],
        ["тыква", "200"],
        ["апельсин", "100"],
        ["тыква", "200"],
        ["огурец", "200"],
        ["пряности", "200"],
        ["сахар", "200"],
        ["соль", "200"],
        ["кетчуп", "200"]]

for(let i = 0; i<data.length; i++){
    table = document.getElementById("table")
    table.innerHTML += add_row(i,data[i][0], data[i][1])
}