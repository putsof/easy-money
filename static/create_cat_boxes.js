document.addEventListener("DOMContentLoaded", showCategory());

function showCategory(){
    var isWrapperNeeded = false;

    fetch('/categories.json')
      .then((response)=> response.json())
      .then((listOfDicts) =>{
        listOfDicts.forEach(
            dict => {
                const newDiv = document.createElement("div");
                newDiv.className ="col-sm square rounded m-2 p-5 vh-25 vw-25";
                newDiv.style = "background-color: #99ddff;"
                const nameH1 = document.createElement("h1");
                nameH1.className="text-center p-2"
                nameH1.id ="category-name";
                nameH1.innerHTML = dict["category_name"];
                nameH1.style="display: inline-block";
                
                const catamountH1 = document.createElement("h1");
                catamountH1.className="h1 p-2";
                catamountH1.innerText= dict["max_amount"];
                catamountH1.style="display: inline-block";
                const cattotalH1 = document.createElement("h1")
                cattotalH1.className="h1 mb-0";
                cattotalH1.innerText= 0;
                cattotalH1.id=dict["category_name"] + "total";
                cattotalH1.style="display: inline-block";
                const divider = document.createElement("h1");
                divider.className="h1 p-2";
                divider.innerText = "/";
                divider.style="display: inline-block";

                newDiv.appendChild(nameH1);
                newDiv.appendChild(cattotalH1);
                newDiv.appendChild(divider);
                newDiv.appendChild(catamountH1);


                newDiv.addEventListener('dragover', dragOver);
                newDiv.addEventListener('dragenter', dragEnter);
                newDiv.addEventListener('dragleave', dragLeave);
                newDiv.addEventListener('drop', dragDrop);
                
                const refElement = document.getElementById("all-categories");
                refElement.appendChild(newDiv);

                if (isWrapperNeeded == true){
                    const wrapperDiv = document.createElement("div");
                    wrapperDiv.className = "w-100 d-none d-md-block";
                    refElement.appendChild(wrapperDiv);
                    isWrapperNeeded = false;
                } else {
                    isWrapperNeeded = true;
                }
            });
    })
}