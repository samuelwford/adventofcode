#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input.map! {|i| i.to_i}.sort!

test1 = [16,10,15,5,1,11,7,19,6,12,4].sort
test2 = [28,33,18,42,31,14,46,20,48,47,24,23,49,45,19,38,39,11,1,32,25,35,8,17,7,9,4,2,34,10,3].sort

$answer = []
$try = 0

def chain(input, adapters)
  $try += 1
  
  if adapters.length == 0
    $answer = input
    return
  end
  
  tail = input.last || 0
  candidates = adapters.select {|adapter| (adapter - tail).between?(0, 3)}
  
  candidates.each do |candidate|
    new_input, new_adapters = input + [candidate], adapters - [candidate]
    chain(new_input, new_adapters)
    
    break if $answer.length > 0
  end
end

def summarize(chain)
  pairs = (0..chain.length - 2).map {|i| [chain[i], chain[i + 1]]}
  diffs = pairs.map {|i,j| j - i}
  ones = diffs.select {|i| i == 1}.count
  threes = diffs.select {|i| i == 3}.count + 1
  puts "#{ones} * #{threes} = #{ones * threes}"
end

chain([0], test1)
summarize($answer)

chain([0], test2)
summarize($answer)

chain([0], input)
summarize($answer)

