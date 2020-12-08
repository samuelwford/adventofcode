#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

class CPU
  attr_reader :a, :pc, :ram, :infinite_loop_detected
  
  def load(program)
    @ram = program
    @pc = 0
    @a = 0
    @infinite_loop_detected = false
  end
  
  def acc(i)
    @a += i
    @pc += 1    
  end
  
  def jmp(i)
    @pc += i
  end
  
  def nop
    @pc += 1
  end
  
  def run
    while @pc < @ram.length
      i, arg = @ram[@pc].split(" ")
      @ram[@pc] = "stop"
      case i
      when "jmp"
        jmp(arg.to_i)
      when "acc"
        acc(arg.to_i)
      when "nop"
        nop
      when "stop"
        @infinite_loop_detected = true
        break
      else
        puts "ERROR #{@pc}: @{i} @{arg}"
        break
      end
    end
  end
end

cpu = CPU.new
i = 0

while
  program = input[0..-1]
  
  x, y = program[i].split(" ")
  case x
  when "nop"
    program[i] = "jmp #{y}"
  when "jmp"
    program[i] = "nop #{y}"
  end
  
  cpu.load(program)
  cpu.run
  
  puts "iteration #{i} - acc = #{cpu.a}"  
  i += 1
  
  break unless cpu.infinite_loop_detected
end