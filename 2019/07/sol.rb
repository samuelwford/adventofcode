def execute(program, input)
  ic = 0
  acc = nil
  
  while program[ic] != 99 do
    instruction = program[ic]
    
    field = "%05d" % instruction
    
    op = field[3..4]
    mode = []
    mode[0] = field[2]
    mode[1] = field[1]
    mode[2] = field[0]
    
    params = []
    desc = []
    
    case op
    when "01"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      program[params[2]] = params[0] + params[1]
      ic += 4
      
    when "02"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      program[params[2]] = params[0] * params[1]
      ic += 4
      
    when "03"
      params[0] = program[ic + 1]
      program[params[0]] = input.shift
      ic += 2
      
    when "04"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      acc = params[0]
      ic += 2
      
    when "05"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      if params[0] != 0 
        ic = params[1]
      else
        ic += 3
      end
      
    when "06"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      if params[0] == 0 
        ic = params[1]
      else
        ic += 3
      end
      
    when "07"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      program[params[2]] = params[0] < params[1] ? 1 : 0
      ic += 4
      
    when "08"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      program[params[2]] = params[0] == params[1] ? 1 : 0
      ic += 4
      
    end  
  end
  
  acc
end

def run_series(program, settings)
  i = 0
  settings.each do |s|
    p = Array.new(program)
    i = execute(p, [s, i])
  end
  i
end

puts ">>> phase one"

p1 = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
s1 = [4,3,2,1,0]
o = run_series(p1, s1)
puts "test 1 output #{o}"

p2 = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
s2 = [0,1,2,3,4]
o = run_series(p2, s2)
puts "test 2 output #{o}"

p3 = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
s3 = [1,0,4,3,2]
o = run_series(p3, s3)
puts "test 3 output #{o}"

p = [3,8,1001,8,10,8,105,1,0,0,21,46,55,76,89,106,187,268,349,430,99999,3,9,101,4,9,9,1002,9,2,9,101,5,9,9,1002,9,2,9,101,2,9,9,4,9,99,3,9,1002,9,5,9,4,9,99,3,9,1001,9,2,9,1002,9,4,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,1001,9,3,9,1002,9,2,9,4,9,99,3,9,1002,9,4,9,1001,9,4,9,102,5,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]

puts [*0..4].permutation(5).map{ |s| run_series(p,s) }.max

puts ">>> phase two"

p1 = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
s1 = [9,8,7,6,5]

o = s1.permutation(5).map{ |s| run_series p1, s }
puts o.inspect