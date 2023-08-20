const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
});

let tasks = [];

//Cria uma nova task
function createTask(tasks_lista){
    console.log("|  Criar nova Task  |");
    rl.question("Digite o titulo da tarefa: ", (titulo)=>{
        rl.question("Digite a descrição da tarefa: ", (descricao)=>{
            let task = { title:titulo, description:descricao }
            tasks_lista.push(task);
        console.log("Task adicionada com sucesso!");
        main(tasks_lista);

        });
    });
}
//Lista as  tasks
function showTasks(tasks_lista){
  
    if(tasks_lista.length===0){
        console.log(">>> Lista Vazia <<<")
        main(tasks_lista);
    }
        console.log(">>> LISTA DE TASKS <<<")
        console.log("INDEX |   TITLE   |  DESCRIPTION ");
    tasks_lista.forEach((task, index) => {
        
        console.log(` ${index + 1}.${task.title}, ${task.description} `);
    });
main(tasks_lista);
};

//Atualiza as tasks
function updateTask(tasks_lista){
    console.log("| ATUALIZAR LISTA DE TASKS |");
    if(tasks_lista===0){
        console.log(">>> Lista Vazia <<<");
        main(tasks_lista);
    }
    
    console.log(">>> LISTA DE TASKS <<<")
    console.log("INDEX |   TITLE   |  DESCRIPTION ");
    tasks_lista.forEach((task, index) => {
        index = parseInt(index);
        console.log(` ${index + 1}.${task.title}, ${task.description} `);
    });
    
    
    rl.question("Qual dessas tasks deseja atulizar(digite o indice):  ",(Inputindex)=>{
        index = parseInt(Inputindex) -1 ;
        if(index<0 || index>tasks_lista.length){
        console.log("<< Digite um valor válido de indice da lista que se apresenta >>")
        main(tasks_lista);
        }
        rl.question("Digite o novo titulo para a task "+(index+1)+": ", (novoTitle)=>{
            rl.question("Digite a nova descrição para a task  "+(index+1)+": ", (novaDesc)=>{
                tasks_lista[index] = { title: novoTitle, description: novaDesc };
                console.log("Dados da task "+ (index+1) +" atualizados! ");
                main(tasks_lista);               
            });
        });

    });
};

//Excluir uma nova task
function deleteTask(tasks_lista){

    if(tasks_lista.length === 0){
        console.log(">>Lista Vazia <<");
        main(task_lista);
    }
    console.log("| EXCLUSÃO DE TASK |");
    console.log(">>> LISTA DE TASKS <<<")
    console.log("INDEX |   TITLE   |  DESCRIPTION ");
    tasks_lista.forEach((task, index) => {
        index = parseInt(index);
        console.log(` ${index + 1}.${task.title}, ${task.description} `);
    });
    
    rl.question("Qual task deseja excluir da lista (Digite o indice da task): ", (index)=>{
        if(index<=0 || index>tasks_lista.length){
            console.log("O indice que digitou não pertence a lista, digite um indice presente na lista!")
            main(tasks_lista);
        }
        
        tasks_lista.splice(index,1);
        console.log("Task "+index+" deletada com sucesso!");
        main(tasks_lista);
    });
};



function main(tasks_lista){
var opcao;        
console.log("|   Escolha uma das seguintes opções    |");
console.log("1 - Criar uma nova tarefa");
console.log("2 - Exibir lista de tarefas");
console.log("3 - Atualizar uma tarefa");
console.log("4 - Deletar uma tarefa");
console.log("5 - sair");
rl.question("Digite o valor numérico de uma das opções:  ",(opcao)=>{
opcao= parseInt(opcao);
switch(opcao){
    case 1:
        createTask(tasks_lista);
        break;
    case 2:
        showTasks(tasks_lista);
        break;
    case 3:
        updateTask(tasks_lista);
        break;
    case 4:
        deleteTask(tasks_lista);
        break;
    
    default:
        console.log("Opção inválida");
        rl.close();
}
});


};

main (tasks);

module.exports = createTask;