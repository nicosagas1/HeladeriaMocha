document.addEventListener('DOMContentLoaded', function () {
  const heladosRadio = document.getElementById('check-helados');
  const palitosRadio = document.getElementById('check-palitos');
  const heladosSizes = document.getElementById('helados-sizes');
  const sizeButtons = document.querySelectorAll('.size-button');
  const neighborhoodSelect = document.getElementById('neighborhood');

  // Mostrar tamaños solo si se selecciona "Helados"
  function toggleSizeOptions() {
    if (heladosRadio.checked) {
      heladosSizes.style.display = 'block';
    } else {
      heladosSizes.style.display = 'none';
      sizeButtons.forEach(btn => btn.classList.remove('active'));
    }
  }

  heladosRadio.addEventListener('change', toggleSizeOptions);
  palitosRadio.addEventListener('change', toggleSizeOptions);

  // Seleccionar tamaño
  sizeButtons.forEach(button => {
    button.addEventListener('click', function () {
      sizeButtons.forEach(btn => btn.classList.remove('active'));
      this.classList.add('active');
    });
  });

  // Cargar barrios desde el archivo JSON
  fetch("/static/public/barrios.json")
    .then(res => {
      if (!res.ok) throw new Error("Archivo no encontrado");
      return res.json();
    })
    .then(data => {
      console.log(data)
      if (data && data.barrios) {
        data.barrios.forEach(barrio => {
          const option = document.createElement("option");
          option.value = barrio;
          option.textContent = barrio;
          neighborhoodSelect.appendChild(option);
        });
      }
    })
    .catch(err => {
      console.error("Error cargando barrios:", err);
      const option = document.createElement("option");
      option.textContent = "Error al cargar barrios";
      option.disabled = true;
      neighborhoodSelect.appendChild(option);
    });
});
