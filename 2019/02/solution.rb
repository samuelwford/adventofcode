# run for puzzle: ruby solution.rb input.txt 12 2

file = ARGV[0] || "input.txt"

input = File.read(file)
strings = input.split(",")
program = strings.map { |s| s.to_i }

if ARGV.length == 3
  program[1] = ARGV[1].to_i
  program[2] = ARGV[2].to_i
end

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

dump = program.join(", ")
puts "before: #{dump}"

execute program

dump = program.join(", ")
puts "after: #{dump}"
