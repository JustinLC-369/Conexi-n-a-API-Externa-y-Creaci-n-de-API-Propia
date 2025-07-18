const API_BASE = 'http://localhost:8000';

document.addEventListener("DOMContentLoaded", () => {
    getLocalDogs();
    document.getElementById("dog-form").onsubmit = createDog;
});

function getExternalDogs() {
    fetch(`${API_BASE}/external/dogs`)
        .then(res => res.json())
        .then(urls => {
            const div = document.getElementById("external-dogs");
            div.innerHTML = "";
            urls.forEach(url => {
                const img = document.createElement("img");
                img.src = url;
                div.appendChild(img);
            });
        });
}

function getLocalDogs() {
    fetch(`${API_BASE}/dogs/`)
        .then(res => res.json())
        .then(dogs => {
            const div = document.getElementById("local-dogs");
            div.innerHTML = "";
            dogs.forEach(dog => {
                const box = document.createElement("div");
                box.innerHTML = `<h4>${dog.title}</h4><p>${dog.description}</p><img src="${dog.image_url}">`;
                div.appendChild(box);
            });
        });
}

function createDog(event) {
    event.preventDefault();
    const form = event.target;
    const data = {
        title: form.title.value,
        description: form.description.value,
        image_url: form.image_url.value
    };
    fetch(`${API_BASE}/dogs/`, {
        method: "POST",
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    })
    .then(res => res.json())
    .then(() => {
        form.reset();
        getLocalDogs();
    });
}
