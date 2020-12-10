#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input.map! {|i| i.to_i}.sort!

test1 = [16,10,15,5,1,11,7,19,6,12,4].sort
test2 = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3].sort

def chain(input, adapters)
  $tries += 1
  
  tail = input.last
  
  candidates = adapters.select {|adapter| (adapter - tail).between?(0, 3)}
  
  if candidates.length == 0
    #puts "> #{input.inspect}"
    $chains += 1
    return
  end
  
  candidates.each do |candidate|
    new_input, new_adapters = input + [candidate], adapters - [candidate]
    chain(new_input, new_adapters)
  end
end

def analyze(input)
  $tries = 0
  $chains = 0
  $max = input.max
  puts input.inspect
  chain([input.shift], input)
  puts "tries: #{$tries}, chains: #{$chains}"
end

puts "======[ tests ]========================"
analyze([0] + test1)
analyze([0] + test2)

puts "\n\n======[ answer ]======================"
input = [0] + input
cuts = (0..input.length - 2).map {|i| [i + 1, input[i + 1] - input[i]]}.filter {|i| i[1] == 3}.map {|i| i[0]}

cuts << input.length

segments = []
last = 0
cuts.each do |cut|
  segments << input[last..cut]
  last = cut
end

total = 1
segments.each do |segment|
  analyze(segment)
  total *= $chains
end

puts "\n\ntotal: #{total}"