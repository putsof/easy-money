document.addEventListener("DOMContentLoaded", showCategory());
function showCategory(){
    fetch('/categories.json')
      .then((response)=> response.json())
      .then((listOfDicts) =>{
        listOfDicts.forEach(
            dict => {
                const newDiv = document.createElement("div");
                newDiv.className ="category-bucket";
                const nameH1 = document.createElement("h1");
                nameH1.id ="category-name"
                nameH1.innerHTML = dict["category_name"];
            
                newDiv.appendChild(nameH1);
                newDiv.addEventListener('dragover', dragOver);
                newDiv.addEventListener('dragenter', dragEnter);
                newDiv.addEventListener('dragleave', dragLeave);
                newDiv.addEventListener('drop', dragDrop);
                
                const refElement = document.getElementById("container");
                refElement.appendChild(newDiv);
            });
    })
}