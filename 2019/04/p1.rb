input = "234208-765869" # !> assigned but unused variable - input

def is_valid?(pwd)
  ascending = true
  has_doubles = false

  last_digit = ""
  pwd.each_char do |digit|
    ascending = false if digit.to_i < last_digit.to_i
    has_doubles = true if digit == last_digit
    last_digit = digit
  end
  
  ascending and has_doubles
end

def is_still_valid?(pwd)
  sets = []
  sets << [pwd[0..1], pwd[2..5]]
  sets << [pwd[1..2], pwd[0] + pwd[3..5]]
  sets << [pwd[2..3], pwd[0..1] + pwd[4..5]]
  sets << [pwd[3..4], pwd[0..2] + pwd[5]]
  sets << [pwd[4..5], pwd[0..3]]
  
  valid = false
  sets.each do |set|
    pair = set[0]
    remainder = set[1]
    if pair[0] == pair[1] and !remainder.include?(pair[0])
      valid = true
    end
  end
  
  valid
end

is_valid?("111111") # => true
is_valid?("223450") # => false
is_valid?("123789") # => false

is_still_valid?("112233") # => true
is_still_valid?("123444") # => false
is_still_valid?("111122") # => true

candidates = []
for i in 234208..768869
  candidates << i if is_valid?(i.to_s)
end

candidates.length # => 1246

filtered_candidates = candidates.select { |c| is_still_valid?(c.to_s) }

filtered_candidates.length # => 814
