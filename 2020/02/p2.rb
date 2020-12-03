#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

good = 0
total = 0

input.each do |line|
  m = line.match(/(?<p1>\d{1,2})-(?<p2>\d{1,2})\s(?<char>.)\:\s(?<pwd>.*)/)
  
  pwd = m[:pwd]
  char = m[:char]
  p1 = m[:p1].to_i - 1
  p2 = m[:p2].to_i - 1
  
  total += 1
  
  anb = pwd[p1] == char && pwd[p2] != char
  bna = pwd[p1] != char && pwd[p2] == char

  good += 1 if anb || bna
end

puts "total: #{total}, good: #{good}"
