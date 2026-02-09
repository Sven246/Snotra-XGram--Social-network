document.addEventListener("DOMContentLoaded", () => {
    const box = document.getElementById("channels");

    fetch("/api/v1/channels/list")
        .then(r => r.json())
        .then(data => {
            data.forEach(ch => {
                box.innerHTML += `
                    <div class="channel">
                        <h3>${ch.title}</h3>
                        <p>${ch.description}</p>
                        <a class="btn" href="/channels/${ch.id}">Открыть</a>
                    </div>
                `;
            });
        });
});
