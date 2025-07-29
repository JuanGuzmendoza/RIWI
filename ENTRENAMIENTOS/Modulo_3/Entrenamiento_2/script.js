document.addEventListener("DOMContentLoaded", function () {
    table_product();               // This function shows the product table when page loads
    show_unique_products();        // This function shows unique products when page loads
    show_products_by_category();   // This function shows products by category when page loads
});


let products = {
    1: { id: 1, name: "Lapto", price: 1500 },
    2: { id: 2, name: "Mause", price: 100 },
    3: { id: 3, name: "Pc", price: 500 },
}


let products_category = new Map([
    ["Electronica", "Laptop"],
    ["Accesorios", "Mouse"],
    ["Electronico", "Pc"],
]);


// This function adds new products to the table and collections
function add_product() {
    const product_name = document.getElementById("form_product_name").value;
    const product_price = parseInt(document.getElementById("form_product_price").value);
    const product_category = document.getElementById("form_product_category").value;
    const table_product = document.querySelector("#product_table tbody");

    if (!product_name || !product_price || !product_category) {
        alert("All fields are required");
        return;
    }

    const id = (Object.keys(products).length) + 1;
    products[id] = { id: id, name: product_name, price: product_price };
    products_category.set(product_category, product_name); 

    table_product.innerHTML += `
    <tr>
        <td>${id}</td>
        <td>${product_name}</td>
        <td>$${product_price}</td>
    </tr>
    `;

    //update product list and category list
    show_unique_products();       
    show_products_by_category(); 

    // Clear inputs after adding
    document.getElementById("form_product_name").value = "";
    document.getElementById("form_product_price").value = "";
    document.getElementById("form_product_category").value = "";
}


// This function shows unique product names in the main page
function show_unique_products() {
    let setProducts = new Set(Object.values(products).map(products => products.name));
    const list = document.getElementById("unique_product_list");
    list.innerHTML="";

    for (const name of setProducts) {
        const li = document.createElement("li");
        li.textContent = name;
        list.appendChild(li);
    }
}


// This function shows all products by category in the main page
function show_products_by_category() {
    const list = document.getElementById("category_product_list");
    list.innerHTML="";
    products_category.forEach((product,category)=>{
        const li = document.createElement("li");
        li.textContent = `${category} → ${product}`;
        list.appendChild(li);
    });
}


// This function shows all products in the HTML table
function table_product() {
    const tableBody = document.querySelector("#product_table tbody");
    for (let id in products) {
        const product = products[id];

        tableBody.innerHTML += `
            <tr>
                <td>${product.id}</td>
                <td>${product.name}</td>
                <td>$${product.price}</td>
            </tr>
        `;
    }
}
