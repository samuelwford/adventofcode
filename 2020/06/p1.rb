#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input = input.map {|x| x.chomp}
input = input.chunk_while {|x| x.length > 0}.to_a
input = input.map {|x| x.join("").split("").uniq.count}

puts input.sum()
