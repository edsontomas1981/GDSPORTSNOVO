function gerarQRCode(text) {
    var qrcode = new QRCode(document.getElementById("qrcodeContainer"), {
      width: 250,
      height: 250,
    });
    qrcode.makeCode(text);
  }

  // Evento de submit do formulário
  document.getElementById("btnPix").addEventListener("click", (e)=> {
    e.preventDefault();
    var chavePix = document.getElementById("chavePix").value;
    var valor = document.getElementById("valor").value;
    var descricao = document.getElementById("descricao").value;
    var textoCobranca = "PIX\n" +
      "Version: 01\n" +
      "Chave: " + chavePix + "\n" +
      "Valor: " + valor + "\n" +
      "Descricao: " + descricao;

    gerarQRCode(textoCobranca);
  });