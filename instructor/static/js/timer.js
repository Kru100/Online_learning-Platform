function startCountdown() {
    console.log("startCountdown function called");
    var countdownTime = 5; // 5 seconds
  
    var countdownInterval = setInterval(function() {
      countdownTime--;
  
      if (countdownTime < 0) {
        clearInterval(countdownInterval);
        var messageElement = document.querySelector('.alert.alert-primary');
        if (messageElement) {
          messageElement.remove();
        }
      }
    }, 1000); // Update countdown every second
  
    return countdownInterval; // Return the interval reference
  }
  
  window.onload = function() {
    startCountdown();
  };