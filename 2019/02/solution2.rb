# run for puzzle: ruby solution2.rb input.txt

file = ARGV[0] || "input.txt"

input = File.read(file)
strings = input.split(",")
program = strings.map { |s| s.to_i }

def execute(program)
  pc = 0
  while program[pc] != 99
    op = program[pc]
  
    address1 = program[pc + 1]
    address2 = program[pc + 2]
    address3 = program[pc + 3]
  
    value1 = program[address1]
    value2 = program[address2]

    result = op == 1 ? value1 + value2 : value1 * value2
  
    program[address3] = result
  
    pc += 4
  end
end

x = 0
y = 0
found = false

until found
  y += 1
  if y == 100
    x += 1
    y = 0
  end
  
  copy = program[0..-1]
  copy[1] = x
  copy[2] = y
  execute copy
  
  if copy[0] == 19690720
    puts "run with #{x}, #{y} = #{copy[0]}"
    found = true
  end
end