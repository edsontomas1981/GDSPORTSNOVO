const canvas = document.getElementById('canvas');
const ctx = canvas.getContext('2d');

// Gradiente radial para suavizar as bordas
const gradient = ctx.createLinearGradient(
canvas.width / 2,
canvas.height / 2,
0,
canvas.width / 2,
canvas.height / 2,
canvas.width / 2
);
gradient.addColorStop(0, '#001  ');

gradient.addColorStop(1, '#D10024');

// Estilizar o cartão
ctx.fillStyle = gradient;
ctx.fillRect(0, 0, canvas.width, canvas.height);

// Estilizar os elementos do cartão
ctx.fillStyle = '#fff';
ctx.font = 'bold 14px Arial';

// Número do cartão
ctx.fillText('0409 0520 6423 7016', 20, 100);

// Nome do titular
ctx.fillText('NOME DO TITULAR', 20, 140);

// Data de validade
ctx.fillText('**/****', 20, 180);

// CVC
ctx.fillText('***', 270, 180);

// CVC
ctx.fillText('VISA', 250,40);

