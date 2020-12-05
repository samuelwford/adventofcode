#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

def find_seat(code)
  v, h = code[0..6], code[7..]
  
  r, c = 0, 0
  
  l, u = 0, 127
  v.split("").each do |y|
    m = (u - l).div(2)
    l, u = l, u - m - 1 if y == "F"
    l, u = l + m + 1, u if y == "B"
    # puts "#{y} -> #{l}..#{u}"
    r = l
  end
  
  l, u = 0, 7
  h.split("").each do |x|
    m = (u - l).div(2)
    l, u = l, u - m - 1 if x == "L"
    l, u = l + m + 1, u if x == "R"
    # puts "#{x} -> #{l}..#{u}"
    c = l
  end
  
  # puts "#{code}: (#{r}, #{c}) = #{r * 8 + c}"
  
  r * 8 + c
end

# puts "pass" if find_seat("FBFBBFFRLR") == 357
# puts "pass" if find_seat("BFFFBBFRRR") == 567
# puts "pass" if find_seat("FFFBBBFRRR") == 119
# puts "pass" if find_seat("BBFFBBFRLL") == 820

seats = input.map { |code| find_seat(code) }.sort()

c = seats.first
seats.each do |seat|
  if c!= seat 
    puts "my seat: #{c}"
    c = seat
  end
  c += 1
end