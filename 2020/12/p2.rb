#!/usr/bin/ruby -w

file = "input.txt"
input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), file), chomp: true)

x, y, wx, wy = 0, 0, 10, 1
ds = ['east', 'south', 'west', 'north']

input.each do |i|
  puts "ship at (#{x}, #{y}), waypoint at (#{wx}, #{wy}), instruction #{i}"

  c, v = i[0], i[1..].to_i
  case c
  when 'N'
    puts " - move waypoint north #{v}"
    wy += v
  when 'S'
    puts " - move waypoint south #{v}"
    wy -= v
  when 'E'
    puts " - move waypoint east #{v}"
    wx += v
  when 'W'
    puts " - move waypoint west #{v}"
    wx -= v
  when 'F'
    puts " - move ship forward #{v} * (#{wx}, #{wy})"
    x += wx * v
    y += wy * v
  when 'L'
    puts " - rotate way point counter-clockwise around ship #{v / 90} times"
    case v / 90
    when 1
      wx, wy = -wy,  wx
    when 2
      wx, wy = -wx, -wy
    when 3
      wx, wy =  wy, -wx
    else
      puts "ERROR: unknown waypoint rotation"
      break
    end
  when 'R'
    puts " - rotate way point clockwise around ship #{v / 90} times"
    case v / 90
    when 1
      wx, wy =  wy, -wx
    when 2
      wx, wy = -wx, -wy
    when 3
      wx, wy = -wy,  wx
    else
      puts "ERROR: unknown waypoint rotation"
      break
    end
  else
    puts "ERROR: unknown instruction #{i}"
    break
  end
  puts " - ship now at (#{x}, #{y}), waypoint at (#{wx}, #{wy})"
  #gets
end

puts "|#{x}| + |#{y}| = #{x.abs + y.abs}"