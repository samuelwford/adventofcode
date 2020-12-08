#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

class CPU
  attr_reader :a, :pc, :ram
  
  def load(program)
    @ram = program
    @pc = 0
    @a = 0
  end
  
  def acc(i)
    @a += i
    puts "  add #{i} to acc = #{@a}"
    @pc += 1    
  end
  
  def jmp(i)
    @pc += i
  end
  
  def nop
    @pc += 1
  end
  
  def run
    while @ram[@pc] != "stop"
      i, arg = @ram[@pc].split(" ")
      puts "#{pc}: #{i} #{arg}"
      @ram[@pc] = "stop"
      case i
      when "jmp"
        jmp(arg.to_i)
      when "acc"
        acc(arg.to_i)
      when "nop"
        nop
      else
        "ERROR #{@pc}: @{i} @{arg}"
      end
    end
  end
end

cpu = CPU.new
cpu.load(input)
cpu.run