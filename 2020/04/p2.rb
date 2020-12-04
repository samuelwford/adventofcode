#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))

def is_valid?(passport)
  
  # byr (Birth Year) - four digits; at least 1920 and at most 2002.
  # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
  # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
  # hgt (Height) - a number followed by either cm or in:
  # If cm, the number must be at least 150 and at most 193.
  # If in, the number must be at least 59 and at most 76.
  # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
  # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
  # pid (Passport ID) - a nine-digit number, including leading zeroes.
  
  byr_is_valid = false
  iyr_is_valid = false
  eyr_is_valid = false
  hgt_is_valid = false
  hcl_is_valid = false
  ecl_is_valid = false
  pid_is_valid = false
  
  has_required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"].all?{|f| passport.has_key?(f)}  
  
  return false unless has_required_fields
  
  byr_is_valid = passport["byr"].to_i.between?(1920, 2002)
  iyr_is_valid = passport["iyr"].to_i.between?(2010, 2020)
  eyr_is_valid = passport["eyr"].to_i.between?(2020, 2030)
  
  hgt = passport["hgt"]
  hgt_is_valid = hgt.to_i.between?(150, 193) if hgt.end_with?("cm")
  hgt_is_valid = hgt.to_i.between?(59, 76) if hgt.end_with?("in")
  
  hcl_is_valid = passport["hcl"].match?(/^\#(\d|[a-f]){6}$/)
  
  ecl_is_valid = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"].include?(passport["ecl"])
  
  pid_is_valid = passport["pid"].match?(/^\d{9}$/)
  
  byr_is_valid && iyr_is_valid && eyr_is_valid && hgt_is_valid && hcl_is_valid && ecl_is_valid && pid_is_valid
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