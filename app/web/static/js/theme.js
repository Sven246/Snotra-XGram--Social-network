document.addEventListener("DOMContentLoaded", () => {
    const saved = localStorage.getItem("theme");
    if (saved === "dark") document.body.classList.add("dark");

    const btn = document.getElementById("theme-toggle");
    if (!btn) return;

    btn.addEventListener("click", () => {
        document.body.classList.toggle("dark");
        localStorage.setItem("theme",
            document.body.classList.contains("dark") ? "dark" : "light"
        );
    });
});
