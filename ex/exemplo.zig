
const std = @import("std");
const acessar = @import("outrafuncao.zig");



pub fn main() void {
    
const x = acessar.outro;

std.debug.print("{d}\n", .{x});

}

  


