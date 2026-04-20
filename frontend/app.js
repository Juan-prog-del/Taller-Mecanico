const API = "http://127.0.0.1:8000/clientes";

function crearCliente() {
    const nombre = document.getElementById("nombre").value;
    const telefono = document.getElementById("telefono").value;

    fetch(API + "/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            nombre: nombre,
            cedula: "0000000000",
            telefono: telefono,
            direccion: "N/A"
        })
    })
    .then(res => res.json())
    .then(() => cargarClientes());
}

function cargarClientes() {
    fetch(API + "/")
    .then(res => res.json())
    .then(data => {
        const lista = document.getElementById("lista");
        lista.innerHTML = "";

        data.forEach(c => {
            const li = document.createElement("li");
            li.textContent = c.nombre + " - " + c.telefono;
            lista.appendChild(li);
        });
    });
}

cargarClientes();