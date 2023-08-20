const numbers = [11,4,5,6,23,45,22]


function findMax(arr){
    let max = arr[0];
    for(let i=1 ;i<arr.length;i++){
        if(max<arr[i]){
            max=arr[i];
        }
    }
 return max;
}

console.log("O maior valor do array é :"+findMax(numbers));