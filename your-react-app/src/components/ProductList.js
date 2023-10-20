import React, { useEffect, useState } from 'react';

function ProductList() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Define the API endpoint URL
    const apiUrl = 'http://127.0.0.1:8000/product/';

    // Make the GET request using fetch
    fetch(apiUrl)
      .then(response => response.json())
      .then(data => {
        setProducts(data);
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []); // The empty dependency array means this effect runs once after the component mounts

  return (
    <div>
      <h1>Product List</h1>
      <ul>
        {products.map(product => (
          <li key={product.id}>
            <strong>{product.name}</strong><br />
            Description: {product.description}<br />
            Price: ${product.price}<br />
            Category: {product.category}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductList;
