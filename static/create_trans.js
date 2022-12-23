document.addEventListener("DOMContentLoaded", showTransaction());
function showTransaction(){
    fetch('/transaction.json')
      .then((response)=> response.json())
      .then((listOfDicts) =>{
        listOfDicts.forEach(
            dict => {
                // create trans-card
                const newDiv = document.createElement("div");
                newDiv.className ="trans-card";
                newDiv.draggable ="true";
                const nameH4 = document.createElement("h4");
                nameH4.innerHTML = dict["merchant_name"];
                const amountH4 = document.createElement("h4");
                amountH4.innerHTML = dict["amount"];
                const dateH4 =document.createElement("h4");
                dateH4.innerHTML = dict["date"];

                newDiv.appendChild(nameH4);
                newDiv.appendChild(amountH4);
                newDiv.appendChild(dateH4);

                newDiv.addEventListener('dragstart', dragStart);
                newDiv.addEventListener('dragend', dragEnd);

                const refElement = document.getElementById("all-transactions");
                refElement.appendChild(newDiv)
            });
    })
}