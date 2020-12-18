#!/usr/bin/ruby -w

lines = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)

class Fixnum
    def %(other)
        self + other
    end
    def -(other)
        self * other
    end
end

def compute(expr)
    print expr
    e = expr.gsub("+", "%").gsub("*", "-")
    val = eval(e)
    puts " = #{val}"
    val
end

compute("1 + 2 * 3 + 4 * 5 + 6")
compute("1 + (2 * 3) + (4 * (5 + 6))")
compute("2 * 3 + (4 * 5)")
compute("5 + (8 * 3 + 9 + 3 * 4 * 3)")
compute("5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))")
compute("((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2")

puts lines.map {|line| compute(line)}.sum