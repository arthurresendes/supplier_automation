document.getElementById('requestForm').addEventListener('submit', function (e) {
    e.preventDefault();

    // Validação básica
    const nomeAdmin = document.getElementById('nomeAdmin').value;
    const nomeCol = document.getElementById('nomeCol').value;
    const ma = document.getElementById('ma').value;
    const val = document.getElementById('val').value;
    const msg = document.getElementById('msg').value;

    const notification = document.getElementById('notification');
    const ritmIdElement = document.getElementById('ritmId');

    if (!nomeAdmin || !nomeCol || !ma || !val || !msg) {
        notification.textContent = 'Por favor, preencha todos os campos.';
        notification.className = 'notification error';
        notification.style.display = 'block';
        ritmIdElement.style.display = 'none';
        return;
    }

    // Gerar ID RITM aleatório
    const randomNumbers = Math.floor(1000 + Math.random() * 9000);
    const ritmId = `RITM${randomNumbers}`;

    // Exibir notificação e ID gerado
    notification.textContent = 'Solicitação enviada com sucesso!';
    notification.className = 'notification success';
    notification.style.display = 'block';

    ritmIdElement.textContent = `${ritmId}`;
    ritmIdElement.style.display = 'block';

});