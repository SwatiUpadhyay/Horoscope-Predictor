document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("horoscope-form");
    const resultDiv = document.getElementById("prediction-result");
    const resultText = document.getElementById("result-text");
  
    // Typewriter function with golden glowing cursor
    function typeWriter(text, element, speed = 40) {
      element.textContent = '';
      element.classList.add("typing"); // show blinking cursor
      let i = 0;
  
      function type() {
        if (i < text.length) {
          element.textContent += text.charAt(i);
          i++;
          setTimeout(type, speed);
        } else {
          element.classList.remove("typing"); // hide cursor when done
        }
      }
  
      type();
    }
  
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
  
      const sign = document.getElementById("sign").value;
  
      try {
        const response = await fetch("/predict", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ sign }),
        });
  
        const data = await response.json();
        const horoscope = data.horoscope || "✨ No stars aligned today.";
  
        resultDiv.classList.remove("hidden");
        typeWriter(horoscope, resultText);
  
      } catch (error) {
        console.error("Error:", error);
        resultDiv.classList.remove("hidden");
        typeWriter("🌑 Oops, something went wrong!", resultText);
      }
    });
  });
  