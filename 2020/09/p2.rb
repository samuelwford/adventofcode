#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input.map! {|i| i.to_i}

code = 133015568

stride = 2
found = false
while !found && stride < input.length
  i = 0
  while i < input.length - stride
    chunk = input[i, stride]
    if chunk.sum == code
      found = true
      puts "found: #{chunk}"
      puts "min = #{chunk.min}, max = #{chunk.max}, min + max = #{chunk.min + chunk.max}"
      break
    end
    i += 1
  end
  stride += 1
end