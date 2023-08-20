
function createTask(title, description){
   const tasks_lista = []

            let task = { title:title, description:description }
            tasks_lista.push(task);

   //     main(tasks_lista);
   return tasks_lista;

     
}

module.exports=createTask;