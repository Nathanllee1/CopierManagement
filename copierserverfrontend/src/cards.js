import React from 'react';



const PrinterCard = (props) => {
  return (
    <div className='card'>
      <h5 className='card-title'>{props.location}</h5>
      <h7 className='status'>{props.status}</h7>
    </div>
  )
};



export default PrinterCard;
