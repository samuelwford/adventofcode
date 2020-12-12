#!/usr/bin/ruby -w

file = "input.txt"
input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), file), chomp: true)

d, x, y = 0, 0, 0
ds = ['east', 'south', 'west', 'north']

input.each do |i|
  puts "at (#{x}, #{y}) facing #{ds[d]}, instruction #{i}"

  c, v = i[0], i[1..].to_i
  case c
  when 'N'
    puts " - move north #{v}"
    y += v
  when 'S'
    puts " - move south #{v}"
    y -= v
  when 'E'
    puts " - move east #{v}"
    x += v
  when 'W'
    puts " - move west #{v}"
    x -= v
  when 'F'
    puts " - move forward (#{ds[d]}) #{v}"
    case d
    when 3 # N
      y += v
    when 1 # S
      y -= v
    when 0 # E
      x += v
    when 2 # W
      x -= v
    else
      puts "ERROR: unknown direction #{d}"
      break
    end
  when 'L'
    od = d
    d -= v / 90
    d += 4 if d < 0
    puts " - turn left #{v}, #{od} -> #{d}"
  when 'R'
    od = d
    d += v / 90
    d -= 4 if d > 3
    puts " - turn right #{v}, #{od} -> #{d}"
  else
    puts "ERROR: unknown instruction #{i}"
    break
  end
  puts " - now at (#{x}, #{y}) facing #{ds[d]}"
  #gets
end

puts "|#{x}| + |#{y}| = #{x.abs + y.abs}"