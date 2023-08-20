

const produtos = [];


//CREATE

function criaProduto(lista_de_produtos){
nome = prompt("Digite o nome do produto: ");
valor = prompt("Digite o valor do produto: ");
código = prompt("Digite o código: ");

let produto = {}


}

//READ
function listaProduto(lista_de_produtos){

}

//UPDATE
function atualizaProduto(lista_de_produtos){

}

//DELETE
function deletaPessoa(lista_de_produtos){

}


function main(produtos){
 opcao = prompt("Digite uma opção: ");
 parseInt(opcao);
    switch(opcao){
        case 1:
            criaProduto(produtos);
            break;
        case 2:
            listaProduto(produtos);
            break;
        case 3:
            atualizaProduto(produtos);
            break;
        case 4:
            deletaPessoa(produtos);
            break;
        default:
            console.log("Opção inválida!");
    }
    
}

