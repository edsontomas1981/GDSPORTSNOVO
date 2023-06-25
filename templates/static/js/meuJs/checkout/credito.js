const numeroCartaoInput = document.getElementById('numero-cartao');
const bandeiraDiv = document.getElementById('bandeira');

numeroCartaoInput.addEventListener('input', () => {
  const numeroCartao = numeroCartaoInput.value.trim();
  let bandeira = '';

  if (/^4[0-9]{12}(?:[0-9]{3})?$/.test(numeroCartao)) {
    bandeira = 'Visa';
  } else if (/^5[1-5][0-9]{14}$/.test(numeroCartao)) {
    bandeira = 'Mastercard';
  } else if (/^3[47][0-9]{13}$/.test(numeroCartao)) {
    bandeira = 'American Express';
  } else if (/^6(?:011|5[0-9]{2})[0-9]{12}$/.test(numeroCartao)) {
    bandeira = 'Discover';
  } else if (/^3(?:0[0-5]|[68][0-9])[0-9]{11}$/.test(numeroCartao)) {
    bandeira = 'Diners Club';
  } else if (/^(?:2131|1800|35\d{3})\d{11}$/.test(numeroCartao)) {
    bandeira = 'JCB';
  } else if (/^2(?:014|149)\d{11}$/.test(numeroCartao)) {
    bandeira = 'Elo';
  } else if (/^6(?:22(?:12[6-9]|1[3-9][0-9]|[2-8][0-9]{2}|9(?:[01][0-9]|2[0-5]))|4[4-9]\d{13}|5[0-9]\d{14}|6[0-9]\d{14}|7[0-9]\d{14}|8[0-9]\d{14})$/.test(numeroCartao)) {
    bandeira = 'Hipercard';
  } else {
    bandeira = 'Desconhecida';
  }

  bandeiraDiv.innerText = bandeira;
});


