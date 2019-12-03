input_args = ARGV
file_arg = input_args[0]

def compute_fuel_module_of_mass(mass)
  mass / 3 - 2
end

def compute_fuel_for_fuel_of_mass(mass)
  total_fuel = 0
  while mass > 5
    fuel = mass / 3 - 2
    total_fuel += fuel
    mass = fuel
  end
  total_fuel
end

sum = 0
File.readlines(file_arg).each do |line|
  mass = line.to_i
  fuel = compute_fuel_module_of_mass(mass)
  fuel_for_fuel = compute_fuel_for_fuel_of_mass(fuel)
  sum += (fuel + fuel_for_fuel)
  puts "elf mass #{mass}; fuel #{fuel}, fuel for fuel #{fuel_for_fuel} (total fuel so far: #{sum})"
end

puts "total fuel needed for elves: #{sum}"

