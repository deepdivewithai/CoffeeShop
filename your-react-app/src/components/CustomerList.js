import React, { useEffect, useState } from 'react';

function CustomerList() {
  const [customers, setCustomers] = useState([]);

  useEffect(() => {
    const apiUrl = 'http://127.0.0.1:8000/customers/'; // Replace with the correct API endpoint

    fetch(apiUrl, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      }
    })
      .then(response => response.json())
      .then(data => {
        setCustomers(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Customer List</h1>
      <ul>
        {customers.map(customer => (
          <li key={customer.id}>
            <strong>{customer.name}</strong><br />
            Email: {customer.email}<br />
            Phone Number: {customer.phone_number}<br />
            Address: {customer.address}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default CustomerList;
