
function fib(num) {
    let a = 1
    let b = 1
    let c = 2
    let counter = 0

    while(counter < num) {
        c = a + b
        a = b;
        b = c;
        //if((c>>1)<<1 === c)
        if(!(c%2))
        {
            console.log(c)
            counter++
        }
    }
}
function enter_number() {
    let num = prompt('Введите положительное целое число:')

    while ((Number.parseInt(num).toString() !== num) || (num <= 0))
    {
       num = prompt('Введите положительное целое число:')
    }
    fib(num)
}
enter_number()


