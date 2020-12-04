#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

def is_valid?(passport)
  # puts passport
  ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].all?{|f| passport.has_key?(f)}
end


passport = {}
valid = 0
total = 0

input.each do |line|
  if line == "\n"
    valid += 1 if is_valid?(passport)
    total += 1
    passport = {}
  else 
    line.split(" ").each do |field|
      k, v = field.split(":")
      passport[k] = v
    end
  end
end

if passport.keys.length > 0 
  valid += 1 if is_valid?(passport)
  total += 1  
end

puts "total: #{total}, valid: #{valid}"