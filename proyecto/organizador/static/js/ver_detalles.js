// ver_detalles.js
function verDetalles(tareaId) {
    const detallesTarea = document.getElementById('detallesTarea');
    const detallesContenido = document.getElementById('detallesContenido');

    // Obtener los detalles de la tarea mediante una petición AJAX a tu servidor
    fetch(`/detalles_tarea/${tareaId}/`)
        .then(response => response.text())
        .then(data => {
            detallesContenido.innerHTML = data;
            detallesTarea.style.display = 'block';
        })
        .catch(error => console.error(error));
}

function ocultarDetalles() {
    const detallesTarea = document.getElementById('detallesTarea');
    detallesTarea.style.display = 'none';
}
