document.addEventListener("DOMContentLoaded", () => {
  const messages = document.querySelector(".messages");
  if (messages) {
    setTimeout(() => messages.remove(), 3000);
  }
});
