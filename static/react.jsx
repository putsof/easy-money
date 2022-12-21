// Show a transaction
function TransactionCard(props){
  return (
      <div className="trans_card">
          <h2>Amount: {props.amount}</h2>
          <h2>MerchantName: {props.merchant_name}</h2>
          <h2>Date: {props.date}</h2>
      </div>
  );
}

  function TransactionsCardContainer(props) {
    const transCards = [];
  
    for (const currentCard of props.transactionCardData) {
      transCards.push(
        <TransactionCard
          amount={currentCard.amount}
          merchant_name={currentCard.merchant_name}
          date={currentCard.date}
          key={currentCard.trans_id}
        />,
      );
    }
    return <React.Fragment>{transCards}</React.Fragment>;
  }


function showTransaction(){
    fetch('/transaction.json')
      .then((response)=> response.json())
      .then((listOfDicts) =>{
        console.log((listOfDicts))
        ReactDOM.render(<TransactionsCardContainer transactionCardData={listOfDicts}/>, document.querySelector('#all-trans'));
    })
}

showTransaction();

  

  
