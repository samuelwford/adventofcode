#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input.map! {|i| i.to_i}

i = 25
while i < input.length
  unless input[i - 25, 25].combination(2).map {|b| b[0] + b[1]}.include?(input[i])
    puts input[i]
    break
  end
  i += 1
end