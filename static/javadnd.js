//variable to keep track of the current dragged item and access its info
let draggedItem = null;

// funtions for the draggables ie. trans-card
function dragStart(){
    console.log('drag started');
    draggedItem = this; //set draggeditem to the item triggering drag start 
}

function dragEnd(){
    console.log('drag ended');
    draggedItem = null; // set back to null when the item is released
}
// end drggables functions

//functions for drop zones ie budget_buckets
function dragOver(e) {
    e.preventDefault();
    console.log('drag over');
}
function dragEnter() {
    console.log('drag entered');
}
function dragLeave() {
    console.log('drag left');
}
function dragDrop() {
    // here THIS is the column
    console.log('drag dropped');
    const transInfo = {
        trans_id: draggedItem.id,
        category_name: this.innerText, 
    };
    fetch('/update-trans-cat.json', {
        method: 'POST',
        body: JSON.stringify(transInfo),
        headers: {
            'Content-Type': 'application/json',
          },
    })
    .then((response) => response.json())
    .then((data) => console.log(data));
    this.append(draggedItem); //add to the budget bucket it was dropped in
    console.log(this.id);
}