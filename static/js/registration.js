function validateForm(event) {
  

  const name = document.getElementById("name").value.trim();
  const phone = document.getElementById("phone").value.trim();
  const altPhone = document.getElementById("alt_phone").value.trim();
  const street = document.getElementById("street").value.trim();
  const city = document.getElementById("city").value.trim();
  const pincode = document.getElementById("pincode").value.trim();
  const email = document.getElementById("email").value.trim();

  // Name: min 3, max 30
  if (name.length < 3 || name.length > 30) {
    alert("Name must be between 3 and 30 characters.");
    return false;
  }

  const phoneRegex = /^[6-9]\d{9}$/;
  if (!phoneRegex.test(phone)) {
    alert("Phone number must be 10 digits and start with 6-9.");
    return false;
  }
  if (!phoneRegex.test(altPhone)) {
    alert("Alternate phone number must be 10 digits and start with 6-9.");
    return false;
  }
  if (phone === altPhone) {
  alert("Phone number and alternate phone number must be different.");
  return false;
}


  const emailRegex = /^[a-zA-Z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$/;
  if (email !== "" && !emailRegex.test(email)) {
    alert("Please enter a valid email address.");
    return false;
  }

  if (street.length < 10 || street.length > 50) {
    alert("Street address must be between 10 and 50 characters.");
    return false;
  }

  if (city.length < 3 || city.length > 20) {
    alert("City name must be between 3 and 20 characters.");
    return false;
  }

  const pinRegex = /^5\d{5}$/;
  if (!pinRegex.test(pincode)) {
    alert("Pincode must be 6 digits and start with 5.");
    return false;
  }

  // ✅ If all validations passed, redirect
  return true;  // ✅ This allows the form to submit to Flask

}
