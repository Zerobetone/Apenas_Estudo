/*function calcularValorTotal(produtos) {
  if (produtos.length > 0) {
    var total = 0; // Erro: A variável 'total' está sendo declarada com 'var' dentro do bloco if
    for (let i = 0; i < produtos.length; i++) {
      total += produtos[i].preco;
    }
    return total;
  }
}

const listaDeProdutos = [
  { nome: 'Produto A', preco: 20 },
  { nome: 'Produto B', preco: 30 },
  { nome: 'Produto C', preco: 15 }
];

const valorTotal = calcularValorTotal(listaDeProdutos);
console.log('Valor total dos produtos:', valorTotal); */

function calcularValorTotal(produtos) {
    var total = 0;
  if (produtos.length > 0) {
     // Erro: A variável 'total' está sendo declarada com 'var' dentro do bloco if
    for (let i = 0; i < produtos.length; i++) {
      total += produtos[i].preco;
    }
    return total;
  }
}

const listaDeProdutos = [
  { nome: 'Produto A', preco: 20 },
  { nome: 'Produto B', preco: 30 },
  { nome: 'Produto C', preco: 15 }
];

const valorTotal = calcularValorTotal(listaDeProdutos);
console.log('Valor total dos produtos:', valorTotal);




