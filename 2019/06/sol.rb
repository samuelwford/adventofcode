file = "input.txt"
# file = "test1.txt"
# file = "test2.txt"

dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + (ARGV[0] || file)

filename # => "test2.txt"

data = File.readlines(filename).map{|x| x.strip.split(')') }

orbits = {}
data.each do |orbit|
  b = orbits[orbit[1]] || []
  b << orbit[0]
  orbits[orbit[1]] = b
end

def count_orbits(orbits, orbit)
  t = orbit[1].count
  orbit[1].each do |b|
    o = orbits[b]
    t += count_orbits(orbits, [b, o]) unless o.nil?
  end
  t
end

l = 0
orbits.each do |k,v| 
  l += count_orbits(orbits, [k,v])
end

l # => 54

def compute_path(orbits, orbit, path)
  orbit[1].each do |b|
    path << b
    o = orbits[b]
    compute_path(orbits, [b, o], path) unless o.nil?
  end
  path
end

paths = {}
orbits.each do |k,v|
  paths[k] = compute_path(orbits, [k,v], [])
end

paths # => {"B"=>["COM"], "C"=>["B", "COM"], "D"=>["C", "B", "COM"], "E"=>["D", "C", "B", "COM"], "F"=>["E", "D", "C", "B", "COM"], "G"=>["B", "COM"], "H"=>["G", "B", "COM"], "I"=>["D", "C", "B", "COM"], "J"=>["E", "D", "C", "B", "COM"], "K"=>["J", "E", "D", "C", "B", "COM"], "L"=>["K", "J", "E", "D", "C", "B", "COM"], "YOU"=>["K", "J", "E", "D", "C", "B", "COM"], "SAN"=>["I", "D", "C", "B", "COM"]}

you = paths["YOU"]
santa = paths["SAN"]

for i in 0..you.length - 1 do
  for j in 0..santa.length - 1 do
    if you[i] == santa[j] 
      puts "i + j = #{i+j}, #{you[i]} #{santa[j]}"
    end
  end
end
