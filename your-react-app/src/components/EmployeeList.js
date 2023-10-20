import React, { useEffect, useState } from 'react';

function EmployeeList() {
  const [employees, setEmployees] = useState([]);

  useEffect(() => {
    const apiUrl = 'http://127.0.0.1:8000/employees/'; // Replace with the correct API endpoint

    fetch(apiUrl, {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
      }
    })
      .then(response => response.json())
      .then(data => {
        setEmployees(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div>
      <h1>Employee List</h1>
      <ul>
        {employees.map(employee => (
          <li key={employee.id}>
            <strong>{employee.name}</strong><br />
            Role: {employee.role}<br />
            Contact Information: {employee.contact_information}<br />
            Hire Date: {employee.hire_date}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default EmployeeList;
