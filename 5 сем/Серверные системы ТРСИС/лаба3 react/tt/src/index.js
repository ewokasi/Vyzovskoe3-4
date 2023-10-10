import React from "react";
import * as rd from "react-dom/client";
import "./index.css"
const r = document.getElementById("root");
const root = rd.createRoot(r)

var bus = ["1", "2", "3"]
var plane = ["3", "4", "5"]
var ship = ["6", "7", "8"]
function TimeTable(){

        return ((<div id="tt_form"><header>Расписание</header>
        <button onClick={()=> root.render(ShowBus(bus, "bus")) }>bus</button>
        <button onClick={()=> root.render(ShowBus(plane, "plane")) }>plane</button>
        <button onClick={()=> root.render(ShowBus(ship, "ship")) }>ships</button>
        </div>))
}

function ShowBus(props, _class){
  
    const listItems = props.map((numbers) =>
  <li>{numbers}</li>
);
    return (<><ul id = "show">{listItems}</ul>
            <div id ="forms">
             
                    <input id = "rem" className = {_class} placeholder="input index to remove"></input>
                     <button onClick={Del}>Del</button>
            
            
                    <input id = "add" className = {_class} placeholder="input to add"></input>
                    <button onClick={Add}>Add</button>
          
            </div>
            </>)  }

   
function Del(){
    let input = document.getElementById("rem")
    let index = input.value
    switch (input.className){
        case ('bus'):
            delete bus[index]
            break
        case ('plane'):
            delete plane[index]
            break
        case ('ship'):
            delete ship[index]
            break       
    }

}


function Add(){
    let input = document.getElementById("add")
    let index = input.value
    switch (input.className){
        case ('bus'):
            bus.push(index)
            break
        case ('plane'):
            plane.push(index)
            break
        case ('ship'):
            ship.push(index)
            break       
    }
}
const tt = document.getElementById("timeTable");
const table = rd.createRoot(tt)
table.render(<TimeTable/>) 
