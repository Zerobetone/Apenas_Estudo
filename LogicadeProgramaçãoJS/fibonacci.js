function fibonacci(number){
    if(number==1){
        return 1;
    }
    else if(number==0){
        return 0;
    }
    return (fibonacci(number-1)+fibonacci(number-2));

}

console.log(fibonacci(8));