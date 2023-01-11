
const addBtn = document.getElementById("add_cat")
addBtn.addEventListener('click', createFormInputs);

let numOfCats = 0;
function createFormInputs() {
   
    numOfCats++;

    // creating span for the category name
    const nameSpan = document.createElement("span");
    nameSpan.className ="category_name";
    nameSpan.id="category" + numOfCats;
    const nameLabel = document.createElement("label");
    nameLabel.setAttribute("for", "category" + numOfCats);
    //nameLabel.innerText = "Category";
    const nameInput = document.createElement("input");
    nameInput.setAttribute("type", "text");
    nameInput.name="category" + numOfCats;
    nameInput.placeholder="Category"

    nameSpan.appendChild(nameLabel);
    nameSpan.appendChild(nameInput);

    const amountSpan = document.createElement("span");
    amountSpan.className ="category_amount";
    amountSpan.id="amount" + numOfCats;
    const amountLabel = document.createElement("label");
    amountLabel.setAttribute("for", "amount" + numOfCats);
    //amountLabel.innerText = "Category";
    const amountInput = document.createElement("input");
    amountInput.setAttribute("type", "text");
    amountInput.name="amount" + numOfCats;
    amountInput.placeholder="Amount";

    amountSpan.appendChild(amountLabel);
    amountSpan.appendChild(amountInput);
    amountSpan.appendChild(document.createElement("br"));

    const refElement = document.getElementById("inputs");
    refElement.appendChild(nameSpan);
    refElement.appendChild(amountSpan);
};