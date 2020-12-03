#!/usr/bin/ruby -w

numbers = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

i = 0
while i < numbers.length - 2
  n = numbers[i].to_i
  j = i + 1
  while j < numbers.length - 1
    m = numbers[j].to_i
    k = j + 1
    while k < numbers.length
      o = numbers[k].to_i
      if n + m + o == 2020
        puts "#{n} + #{m} + #{o}= #{n + m + o}, #{n} * #{m} * #{o}= #{n * m * o}"
      end
      k += 1
    end
    j += 1
  end
  i += 1
end