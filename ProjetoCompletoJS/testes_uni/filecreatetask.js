
function createTask(title, description){

            let task = { title:title, description:description }
            tasks_lista.push(task);

   //     main(tasks_lista);
   return task;

     
}

module.exports=createTask();