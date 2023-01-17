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
                cardDiv.className ="card-body";
                const flexDiv = document.createElement("div");
                flexDiv.className ="d-flex justify-content-between p-md-1";
                const flexRow = document.createElement("div");
                flexRow.className="d-flex flex-row";
                const alignDiv = document.createElement("div");
                alignDiv.className="align-self-center";
                const fasDiv = document.createElement("i");
                fasDiv.className="fas fa-pencil-alt text-info fa-3x me-4";

                newDiv.appendChild(cardDiv);
                cardDiv.appendChild(flexDiv);
                flexDiv.appendChild(flexRow);
                flexRow.appendChild(alignDiv);
                alignDiv.appendChild(fasDiv);

                const merchDiv = document.createElement("div");
                const nameH4 = document.createElement("h4");
                nameH4.innerHTML = dict["merchant_name"];
                const dateDiv = document.createElement("p");
                dateDiv.className="mb-0"
                dateDiv.innerText=dict["date"].slice(0,16);
                merchDiv.appendChild(nameH4);
                merchDiv.appendChild(dateDiv);
                
                flexRow.appendChild(merchDiv)

            

                const moneyDiv = document.createElement("div");
                moneyDiv.className="align-self-center"
                const moneyH2 = document.createElement("h2");
                moneyH2.className="h1 mb-0";
                moneyH2.innerText='$' + dict["amount"];
                moneyDiv.appendChild(moneyH2);

                flexRow.appendChild(moneyDiv);
                // not displayed
                const transidH5 = document.createElement("h5");
                newDiv.id=dict["trans_id"]
                transidH5.innerHTML = dict["trans_id"];
                // end not displayed
        
          

                newDiv.addEventListener('dragstart', dragStart);
                newDiv.addEventListener('dragend', dragEnd);

                const refElement = document.getElementById("all-transactions");
                refElement.appendChild(newDiv)
            });
    })
}