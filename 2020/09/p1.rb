#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input.map! {|i| i.to_i}

i = 25
while i < input.length
  unless input[i - 25, 25].combination(2).map {|b| b[0] + b[1]}.include?(input[i])
    puts "found #{input[i]}"
    break
  end
  i += 1
end

# without a 'while'
puts (0..input.length - 26)
         .map { |i| [input[i + 25], input[i, 25].combination(2).map {|m,n| m+n}] }
         .reject { |i,j| j.include? i }
         .map { |i,j| i }

# woah
puts input[(0..input.length - 26).find { |i| !input[i, 25].combination(2).map {|m,n| m+n}.include?(input[i + 25]) } + 25]
