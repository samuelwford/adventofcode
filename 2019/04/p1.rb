input = "234208-765869".split('-')
x = input[0].to_i
y = input[1].to_i

x # => 234208
y # => 765869

def has_doubles?(pwd)
  pwd[0] == pwd[1] or pwd[1] == pwd[2] or pwd[2] == pwd[3] or pwd[3] == pwd[4] or pwd[4] == pwd[5]
end

has_doubles?("111111") # => true
has_doubles?("223450") # => true
has_doubles?("123789") # => false

def ascending?(pwd)
  pwd[5] >= pwd[4] and pwd[4] >= pwd[3] and pwd[3] >= pwd[2] and pwd[2] >= pwd[1] and pwd[1] >= pwd[0]
end

ascending?("111111") # => true
ascending?("223450") # => false
ascending?("123789") # => true

def is_valid?(pwd)
  has_doubles?(pwd) and ascending?(pwd)
end

def is_still_valid?(pwd)
  sets = []
  sets << [pwd[0..1], pwd[2..5]]
  sets << [pwd[1..2], pwd[0] + pwd[3..5]]
  sets << [pwd[2..3], pwd[0..1] + pwd[4..5]]
  sets << [pwd[3..4], pwd[0..2] + pwd[5]]
  sets << [pwd[4..5], pwd[0..3]]
  
  valid_sets = sets.select { |p, r| p[0] == p[1] and !r.include?(p[0]) }
  
  valid_sets.length > 0
end

is_valid?("111111") # => true
is_valid?("223450") # => false
is_valid?("123789") # => false

is_still_valid?("112233") # => true
is_still_valid?("123444") # => false
is_still_valid?("111122") # => true

candidates = []
for i in x..y
  candidates << i if is_valid?(i.to_s)
end

candidates.length # => 1246

filtered_candidates = candidates.select { |c| is_still_valid?(c.to_s) }

filtered_candidates.length # => 814

puts "#{candidates.length} candidates, #{filtered_candidates.length} after second pass"
# >> 1246 candidates, 814 after second pass
