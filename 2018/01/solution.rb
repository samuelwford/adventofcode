file = ARGV[0] || "input.txt"

lines = File.readlines(file).map { |x| x.to_i }
result = lines.reduce(0, :+)

puts "part one - #{result}"

frequencies = [0]
frequency = 0

lines.each do |drift|
  frequency += drift
  
end
