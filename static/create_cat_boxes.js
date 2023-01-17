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
                nameH1.className="text-center"
                nameH1.id ="category-name";
                nameH1.innerHTML = dict["category_name"];
                const catamountH1 = document.createElement("h1");
                catamountH1.className="h1 mb-0";
                catamountH1.innerText= dict["max_amount"];
            
                newDiv.appendChild(nameH1);
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