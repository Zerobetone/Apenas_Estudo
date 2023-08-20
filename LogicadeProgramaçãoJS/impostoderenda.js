 
 function calculateIncomeTax(salario){
    
    if(salario<=20000){
        return "isento de imposto";
    }
    else if (salario>20000 && salario<=50000){
        return "10% de imposto, gerando um imposto de "+ (salario*0.10);
    }
    else if (salario>50000 && salario<=100000){
        return "20% de imposto, gerando um imposto de "+ (salario*0.20);
    }
        return "30% de imposto, gerando um imposto de "+ (salario*0.30);
 }

console.log(calculateIncomeTax(30000)); 