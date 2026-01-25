document.addEventListener("DOMContentLoaded", () => {
  const alerts = document.querySelectorAll(".alert");
  if (alerts.length) {
    setTimeout(() => alerts.forEach(a => a.remove()), 4000);
  }
});
