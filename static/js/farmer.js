function validateLogin() {
  const name = document.getElementById("name").value.trim();
  const password = document.getElementById("password").value.trim();

  const namePattern = /^[A-Za-z\s]{3,}$/; // allow letters and spaces, min 3 chars
  const passwordPattern = /^.{8}$/; // password = exactly 8 chars

  if (!namePattern.test(name)) {
    showPopup("🧑‍🌾 Please enter a valid name (at least 3 letters).");
    return;
  }

  if (!passwordPattern.test(password)) {
    showPopup("🔒 Password must be exactly 8 characters.");
    return;
  }

  showPopup("✅ Login successful! Redirecting...");
  setTimeout(() => {
    window.location.href = "/vegetableselection";
  }, 1500);
}

function showPopup(message) {
  document.getElementById("popup-message").textContent = message;
  document.getElementById("popup").style.display = "block";
}

function closePopup() {
  document.getElementById("popup").style.display = "none";
}