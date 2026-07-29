
pub fn main() void {
    var soma: i32 = 10 + 5;
    var subtracao: i32 = 20 - 8;
    var multiplicacao: i32 = 6 * 7;

    if (soma > 10) {
        soma = soma + 1;
    }

    var i: i32 = 0;

    while (i < 5) {
        i = i + 1;
    }

    for (1..10) |j| {
        j = j + 1;
    }
}