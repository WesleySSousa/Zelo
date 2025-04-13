BtnChamaMenu = document.getElementById("BtnMenu");
BtnChamaMenu.addEventListener("click", function () {
  BtnChamaMenu.classList.toggle("AtivaMenu");
});

function aplicarRiscoNosMarcados() {
  const checkboxes = document.querySelectorAll('input[type="checkbox"]');
  checkboxes.forEach((checkbox) => {
    const span = checkbox.nextElementSibling;
    if (span && span.tagName === "SPAN") {
      span.style.textDecoration = checkbox.checked ? "line-through" : "none";
      span.style.color = checkbox.checked ? "gray" : "whitesmoke";
    }
  });
}


window.onload = aplicarRiscoNosMarcados;

setTimeout(function () {
  const mensagens = document.getElementById("mensagens");
  if (mensagens) {
    mensagens.style.transform = "translateY(-200px)";
  }
}, 3000);
