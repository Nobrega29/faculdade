let n1 = parseFloat(prompt('Informe o primeiro número: '))
let n2 = parseFloat(prompt('Informe o segundo número: '))
let opcoes = prompt('Escolha a operação q deseja: 1 = adição; 2 = subtração; 3 = multiplicação; 4 = divisão ');
let resultado 

if (opcoes == 1){
    resultado = n1 + n2;
    alert(resultado);
}
else if (opcoes == 2){
    resultado = n1 - n2;
    alert(resultado)
}
else if (opcoes == 3){
    resultado = n1 * n2;
    alert(resultado)
}
else if (opcoes == 4) {
    if (n2 == 0) {
        alert('Erro: Não é possível dividir por zero.');
    } else {
        resultado = n1 / n2;
        alert('Resultado: ' + resultado);
    }
} else {
    alert('Operação inválida');
}
