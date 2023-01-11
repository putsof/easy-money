document.addEventListener("DOMContentLoaded", showTransaction());
function showTransaction(){
    fetch('/transaction.json')
      .then((response)=> response.json())
      .then((listOfDicts) =>{
        listOfDicts.forEach(
            dict => {
                // create trans-card
                const newDiv = document.createElement("div");
                newDiv.className ="card mt-3";
                newDiv.draggable ="true";
                const cardDiv = document.createElement("div");
                cardDiv.className ="card-body"

                const nameH4 = document.createElement("h4");
                nameH4.className ="card-title";
                nameH4.innerHTML = dict["merchant_name"];
                const amountH4 = document.createElement("h4");
                amountH4.innerHTML = dict["amount"];
                const dateH4 = document.createElement("h4");
                dateH4.innerHTML = dict["date"];
                const transidH5 = document.createElement("h5");
                newDiv.id=dict["trans_id"]
                transidH5.innerHTML = dict["trans_id"];

                newDiv.appendChild(cardDiv);
                newDiv.appendChild(nameH4);
                newDiv.appendChild(amountH4);
                newDiv.appendChild(dateH4);
                newDiv.appendChild(transidH5);

                newDiv.addEventListener('dragstart', dragStart);
                newDiv.addEventListener('dragend', dragEnd);

                const refElement = document.getElementById("all-transactions");
                refElement.appendChild(newDiv)
            });
    })
}