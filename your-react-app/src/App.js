import React from 'react';
import ProductList from './components/ProductList';
import CustomerList from './components/CustomerList'; // Import the CustomerList component
import EmployeeList from './components/EmployeeList'; // Import the EmployeeList component

function App() {
  return (
    <div className="App">
      <ProductList />      
      <CustomerList /> {/* Render the CustomerList component */}
      <EmployeeList /> {/* Render the EmployeeList component */}
    </div>
  );
}

export default App;

