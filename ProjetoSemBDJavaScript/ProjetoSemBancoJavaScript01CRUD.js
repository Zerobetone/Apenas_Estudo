const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let pessoas = [];

function addPessoa(lista_de_pessoas) {
  console.log("| CADASTRO DE NOVA PESSOA |");
  rl.question("Digite o nome da Pessoa: ", function(nome) {
    rl.question("Digite o número de telefone: ", function(telefone) {
      rl.question("Digite a idade da pessoa: ", function(idade) {
        telefone = parseInt(telefone);
        idade = parseInt(idade);

        let pessoa = { name: nome, phone: telefone, year: idade };
        lista_de_pessoas.push(pessoa);

        console.log("Pessoa adicionada com sucesso!");
        main(lista_de_pessoas);
      });
    });
  });
}

function exibirPessoas(lista_de_pessoas) {
  console.log("LISTA DE PESSOAS");

  if (lista_de_pessoas.length === 0) {
    console.log(">>> LISTA VAZIA <<<< ");
  } else {
    lista_de_pessoas.forEach((pessoa, index) => {
      console.log(`| ${index + 1}.${pessoa.name}, ${pessoa.phone}, ${pessoa.year} |`);
    });
  }
  main(lista_de_pessoas);
}

function atualizarPessoa(lista_de_pessoas) {
  exibirPessoas(lista_de_pessoas);
  rl.question("Digite o indice da pessoa que deseja atualizar: ", function(indx) {
    indx = parseInt(indx);
    if (indx >= 0 && indx < lista_de_pessoas.length) {
      rl.question("Digite o novo nome dessa pessoa: ", function(novoNome) {
        rl.question("Digite o novo numero dessa pessoa: ", function(novoTelefone) {
          rl.question("Digite a idade dessa pessoa: ", function(novaIdade) {
            lista_de_pessoas[indx].name = novoNome;
            lista_de_pessoas[indx].phone = novoTelefone;
            lista_de_pessoas[indx].year = parseInt(novaIdade);
            console.log("Dados da Pessoa atualizados!");
            main(lista_de_pessoas);
          });
        });
      });
    } else {
      console.log("Índice inválido.");
      main(lista_de_pessoas);
    }
  });
}

function deletarPessoa(lista_de_pessoas) {
  exibirPessoas(lista_de_pessoas);
  rl.question("DIGITE O INDICE DA PESSOA QUE DESEJA DELETAR: ", function(indx) {
    indx = parseInt(indx);
    if (indx >= 0 && indx < lista_de_pessoas.length) {
      lista_de_pessoas.splice(indx, 1);
      console.log(`Pessoa ${indx + 1} deletada com sucesso!`);
      main(lista_de_pessoas);
    } else {
      console.log("Índice inválido. Nenhuma pessoa deletada.");
      main(lista_de_pessoas);
    }
  });
}

function main(pessoas) {
  console.log("| Escolha uma opção |");
  console.log("| 1 - Adicionar uma Pessoa |");
  console.log("| 2 - Listar Pessoas |");
  console.log("| 3 - Atualizar uma Pessoa |");
  console.log("| 4 - Deletar uma Pessoa |");
  console.log("| 5 - Sair |");

  rl.question("Digite uma opção desejada: ", function(opcao) {
    opcao = parseInt(opcao);

    switch (opcao) {
      case 1:
        addPessoa(pessoas);
        break;

      case 2:
        exibirPessoas(pessoas);
        break;

      case 3:
        atualizarPessoa(pessoas);
        break;

      case 4:
        deletarPessoa(pessoas);
        break;

      default:
        console.log("Opção inválida!");
        rl.close();
    }
  });
}

main(pessoas);