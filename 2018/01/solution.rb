file = "input.txt"
# file = "test1.txt"
# file = "test2.txt"

dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + (ARGV[0] || file)

dir # => ""
filename # => "input.txt"

lines = File.readlines(filename).map { |x| x.to_i }
result = lines.reduce(0, :+)

result # => 587

puts "part one - #{result}"

frequencies = [0]
duplicates = []
frequency = 0

while duplicates.length == 0 do
  lines.each do |drift|
    frequency += drift

    if frequencies.include?(frequency)
      puts "seen #{frequency} before"
      duplicates << frequency
      break
    end
  
    frequencies << frequency
  end
end

duplicates # => [83130]

# >> part one - 587
# >> seen 83130 before
