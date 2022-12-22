
console.log("is this running")
// get all elements that we  want to implement drag and drop on
// draggable for trans card and droppable for budget bucket
const trans_card = document.querySelectorAll(".trans-card") 
const budget_bucket = document.querySelectorAll('.budget-bucket')

//variable to keep track of the current dragged item and do things to it
let draggedItem = null;

// funtions for the draggables ie. trans-card
function dragStart(){
    console.log('drag started');
    draggedItem = this; //set draggeditem to the item triggering drag start 
}

function dragEnd(){
    console.log('drag ended');
    this.className = 'trans-card'
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
    console.log('drag dropped');
    this.append(draggedItem); //add to the budget bucket it was dropped in
}
// end functions for drop zones

//add an eventlistener to each trans card
//one for the drag event start and the other for the drag end
trans_card.forEach(
    trans => {
        trans.addEventListener('dragstart', dragStart);
        trans.addEventListener('dragend', dragEnd);
    });

budget_bucket.forEach(
    bucket =>{
        bucket.addEventListener('dragover', dragOver);
        bucket.addEventListener('dragenter', dragEnter);
        bucket.addEventListener('dragleave', dragLeave);
        bucket.addEventListener('drop', dragDrop);
    });