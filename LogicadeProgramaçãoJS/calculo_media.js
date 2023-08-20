

//Solicitação da primeira nota ao usuário
var n1 = parseFloat(prompt("Digite a primeira nota: "));

//Solicitação da segunda nota ao usuário
var n2 = parseFloat(prompt("Digite a seunda nota: "));

//Solicitação da terceira nota ao usuário
var n3 = parseFloat(prompt("Digite a terceira nota: "));

function verificaNota(nota){
    if(nota<0 || nota>10 || isNaN(nota)){
        console.log("O valor de nota deve estar entre 0 e 10 , não permitido também letras!")
        return null;
    }
    else {
    return nota;}
}

var n1validada = verificaNota(n1);
var n2validada = verificaNota(n2);
var n3validada = verificaNota(n3);

if (n1validada === null || n2validada === null || n3validada === null){
        console.log("Pelo menos uma das notas não é válida. Certifique-se de inserir valores entre 0 e 10.");
}
 else{
var media = (n1validada+n2validada+n3validada)/3;

if(media<5){
    console.log("REPROVADO");
}
else if(media>=5 && media<7){
    console.log("RECUPERAÇÃO");
}
else if(media>=7){
    console.log("APROVADO");
}

 }
