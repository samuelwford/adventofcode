#!/usr/bin/ruby -w

lines = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)

def calc(lhs, oper, rhs)
    oper == "*" ? lhs * rhs : lhs + rhs
end

def eval(expr)
    print expr

    accum, oper = 0, "+"
    stack = []
    while expr.length > 0
        char, expr = expr[0], expr[1..]
        case char
        when "+", "*"
            oper = char
        when "("
            stack.push [accum, oper]
            accum, oper = 0, "+"
        when ")"
            tmp = accum
            accum, oper = stack.pop
            accum = calc(accum, oper, tmp)
        when "0".."9"
            accum = calc(accum, oper, char.to_i)
        end
    end

    puts " = #{accum}"
    accum
end

eval("1 + 2 * 3 + 4 * 5 + 6")
eval("1 + (2 * 3) + (4 * (5 + 6))")
eval("2 * 3 + (4 * 5)")
eval("5 + (8 * 3 + 9 + 3 * 4 * 3)")
eval("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
eval("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")

puts lines.map {|line| eval(line)}.sum