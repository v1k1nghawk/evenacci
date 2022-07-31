
let a =1
let b = 1
let c = 2
function fib(num) {
 for(let i = 1; i<num;i++)
 {
     c = a+b
     a = b;
     b = c;

      if((c>>1)<<1 === c)
         console.log(c)
 }
}
var number = prompt('Enter number:')
fib(number)


