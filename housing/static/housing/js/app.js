// Keep JS minimal: no errors if elements don't exist
document.addEventListener("DOMContentLoaded", () => {
  // Auto-hide Django messages after 4 seconds (if you use them)
  const alerts = document.querySelectorAll(".alert");
  if (alerts.length) {
    setTimeout(() => alerts.forEach(a => a.remove()), 4000);
  }
});
