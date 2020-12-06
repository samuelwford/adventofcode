#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input = input.map {|x| x.chomp} # remove newlines
input = input.chunk_while {|x| x.length > 0}.to_a # split into groups

input = input.map do |g|
  g.delete("")
  ys = g.first.split("").sort
  g.each do |h|
    ys.select! {|i| h.include?(i)}
    #puts "- #{h}, #{ys.join("")}"
  end
  #puts "g: #{g.join(",")} = #{ys.count}"
  ys.count
end

puts input.sum()
