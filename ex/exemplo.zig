pub fn main() void {
    var a: i32 = 10;
    const b: i32 = 20;
    const c = 30;

    a = b;
    a += c;
    a +%= b;
    a +% c;
    a +| b;

    a +|= c;
    a -= b;
    a -% c;
    a -%= b;
    a -| c;
    a -|= b;



     var x: i32 = 0;
    const limite: i32 = 10;

    while (x < limite) {
        x += 1;

        if (x == limite) {
            break;
        }
    }

    return x;

    
}