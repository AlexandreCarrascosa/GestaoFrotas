document.addEventListener('DOMContentLoaded', () => {
  const formElement = document.getElementById('reservaForm');
  const toggleButton = document.getElementById('toggle-theme');

  if (formElement) {
    formElement.addEventListener('submit', async function (e) {
      e.preventDefault();
      const form = new FormData(this);
      const data = Object.fromEntries(form.entries());

      const res = await fetch('https://gestaofrotas-g05f.onrender.com/api/reserva', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data),
      });

      if (res.ok) {
        const msg = `
🛻Reserva de Veiculo 🛻

PLACA - ${data.placa}

Solicitante: ${data.solicitante}
Motorista: ${data.motorista}
Motivo: ${data.motivo}
Gestor Responsável : ${data.gestor}

Data da Retirada: ${data.data_retirada}
Hora da Retirada: ${data.hora_retirada}

Data da Devolução: ${data.data_devolucao}
Hora da Devolução: ${data.hora_devolucao}
        `;
        const whatsappUrl = `https://wa.me/?text=${encodeURIComponent(msg)}`;
        window.open(whatsappUrl, '_blank');
      } else {
        alert("Erro ao enviar reserva.");
      }
    });
  }

  if (toggleButton) {
    toggleButton.addEventListener('click', () => {
      document.body.classList.toggle('dark');
      const isDark = document.body.classList.contains('dark');
      localStorage.setItem('dark-mode', isDark);
    });

    const darkMode = localStorage.getItem('dark-mode') === 'true';
    if (darkMode) {
      document.body.classList.add('dark');
    }
  }
});
