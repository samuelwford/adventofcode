#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || "input.txt")

good = 0
total = 0

input.each do |line|
  m = line.match(/(?<min>\d{1,2})-(?<max>\d{1,2})\s(?<char>.)\:\s(?<pwd>.*)/)

  pwd = m[:pwd]
  char = m[:char]
  min = m[:min].to_i
  max = m[:max].to_i

  count = pwd.scan(char).length

  total += 1
  good += 1 if count >= min && count <= max
end

puts "total: #{total}, good: #{good}"
