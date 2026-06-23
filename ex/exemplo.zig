
const std = @import("std");
const acessar = @import("outrafuncao.zig");



pub fn main() void {
var y : u8 = 10; 
var x : u8 = 5;
y = x += 1;
std.debug.print("O valor de x é: {}\n", .{y});

}

  


