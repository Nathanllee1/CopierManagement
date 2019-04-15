import React from 'react';



const PrinterCard = (props) => {
  return (
    <div class='card'>
        <h5 class='card-title'>{props.location}</h5>
        <br>
        <h7 class='status'>{props.status}</h7>
    </div>
  )
};



export default PrinterCard;
