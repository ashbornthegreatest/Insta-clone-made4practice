console.log("Script loaded 🔥");

const loginBtn = document.getElementById("loginBtn");
const userInput = document.getElementById("user");
const passInput = document.getElementById("pass");

loginBtn.addEventListener("click", async (e) => {
  e.preventDefault();

  const email = userInput.value;
  const password = passInput.value;

  try {
    const res = await fetch("http://localhost:5000/login", {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({ email, password })
    });

    const data = await res.json();

    // 🔥 ALWAYS redirect based on backend
    window.location.href = data.redirect;

  } catch (err) {
    console.error(err);
    alert("Server error bro 💀");
  }
});

const buttons = document.querySelectorAll("button");

buttons.forEach(btn => {
  btn.addEventListener("click", () => {
    console.log(btn.innerText + " clicked!");
  });
});