#!/usr/bin/ruby -w

input = [14,1,17,0,3,20]

n = {}
input[0..-2].each_with_index {|v,i| n[v] = i}

i, l = input.length, input.last
while i < 30000000
    p = n.has_key?(l) ? (i - 1) - n[l] : 0
    n[l] = i - 1
    l, i = p, i + 1
    # puts "#{i}: #{l}"
end

puts l