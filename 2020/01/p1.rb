input = ARGV[0]
numbers = File.readlines(input)

i = 0
while i < numbers.length - 1
  n = numbers[i].to_i
  j = i + 1
  while j < numbers.length
    m = numbers[j].to_i
    if n + m == 2020
      puts "#{n} + #{m} = #{n + m}, #{n} * #{m} = #{n * m}"
    end
    j += 1
  end
  i += 1
end