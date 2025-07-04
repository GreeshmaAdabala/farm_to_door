function sendOTP() {
    const username = document.getElementById("username").value.trim();
    const phone = document.getElementById("phone").value.trim();
    const phonePattern = /^[6-9]\d{9}$/;

    if (username.length < 3 || username.length > 30) 
        {
        alert("Please enter a valid username");
        return;
      }
  
    if (!phonePattern.test(phone)) {
      alert("Please enter a valid 10-digit phone number starting with 6-9.");
      return;
    }
  
    const otp = Math.floor(100000 + Math.random() * 900000);
    sessionStorage.setItem("sentOTP", otp);
    alert("OTP sent to your number: " + otp);
  
    document.getElementById("otp-section").style.display = "block";
  }
  
  function validateOTP(event) {
  const enteredOTP = document.querySelector('input[name="otp"]').value.trim();
  const sentOTP = sessionStorage.getItem("sentOTP");

  if (enteredOTP === sentOTP) {
    alert("OTP verified! Redirecting...");
    window.location.href = "/registration";  // ✅ Correct route
  } else {
    alert("Invalid OTP. Please try again.");
    event.preventDefault();
  }
}
