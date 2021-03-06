#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

w = input[0].length - 1 # because of the new line
h = input.length

i, trees = 0, 0

while i < h
  x, y = i * 3, i
  _, x2 = x.divmod(w)
  trees += 1 if input[y][x2] == "#"
  i += 1
end

puts "trees: #{trees}"