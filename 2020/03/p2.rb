#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

def run(dx, dy, forest)
  h, w = forest.length, forest[0].length - 1 # because of the new line
  x, y, trees = 0, 0, 0

  while y < h
    _, x2 = x.divmod(w)
    trees += 1 if forest[y][x2] == "#"
    x += dx
    y += dy
  end
  
  trees
end

a = run(1, 1, input)
b = run(3, 1, input)
c = run(5, 1, input)
d = run(7, 1, input)
e = run(1, 2, input)

puts "a: #{a}, b: #{b}, c: #{c}, d: #{d}, e: #{e}"
puts "a * b * c * d * e: #{a*b*c*d*e}"