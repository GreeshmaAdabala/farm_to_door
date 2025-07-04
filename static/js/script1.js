let vegetableStock = [];

function addVegetable(name, priceId, qtyId) {
    let qty = document.getElementById(qtyId).value;
    let price = document.getElementById(priceId).value;

    if (price === "" || price <= 0) {
        alert("Please enter a valid price!");
        return;
    }

    if (qty === "" || qty <= 0) {
        alert("Please enter a valid quantity!");
        return;
    }

    // Add vegetable details to vegetableStock array
    vegetableStock.push({
        name: name,
        price: price,
        quantity: qty
    });

    let availableList = document.getElementById("available-vegetables");

    let itemDiv = document.createElement("div");
    itemDiv.classList.add("available-item");

    let img = document.createElement("img");
    let images = {
        "Brinjal": "/static/images/brinjal.jpeg",
        "Cabbage": "/static/images/cabbage.jpeg",
        "Carrot": "/static/images/carrot.jpeg",
        "Cauliflower": "/static/images/cauli.jpg",
        "Cucumber": "/static/images/cucumber.jpg",
        "Tomato": "/static/images/tomato.jpeg",
        "CurryLeaves": "/static/images/curry.jpeg",
        "Drumstick": "/static/images/drumstick.jpg",
        "IvyGourd": "/static/images/ivygourd.jpeg",
        "Potato": "/static/images/potato.jpeg",
        "Ridge Gourd": "/static/images/ridgegourd.jpg",
        "Spinach": "/static/images/Spinach.jpeg"
    };

    img.src = images[name];
    img.alt = name;
    img.classList.add("veg-image");

    let text = document.createElement("p");
    text.textContent = `${name} - ₹${price}/Kg, Quantity: ${qty} Kg, Total: ₹${price * qty}`;

    itemDiv.appendChild(img);
    itemDiv.appendChild(text);
    availableList.appendChild(itemDiv);

    document.getElementById(priceId).value = "";
    document.getElementById(qtyId).value = "";
}
function saveStock() {
    fetch('/save_stock', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(vegetableStock)  // Sending the vegetableStock as JSON
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Shows "Stock saved successfully!"
    })
    .catch(error => {
        console.error('Error:', error);
    });
}



