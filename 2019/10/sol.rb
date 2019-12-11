input = <<INPUT.split("\n")
#.#.###.#.#....#..##.#....
.....#..#..#..#.#..#.....#
.##.##.##.##.##..#...#...#
#.#...#.#####...###.#.#.#.
.#####.###.#.#.####.#####.
#.#.#.##.#.##...####.#.##.
##....###..#.#..#..#..###.
..##....#.#...##.#.#...###
#.....#.#######..##.##.#..
#.###.#..###.#.#..##.....#
##.#.#.##.#......#####..##
#..##.#.##..###.##.###..##
#..#.###...#.#...#..#.##.#
.#..#.#....###.#.#..##.#.#
#.##.#####..###...#.###.##
#...##..#..##.##.#.##..###
#.#.###.###.....####.##..#
######....#.##....###.#..#
..##.#.####.....###..##.#.
#..#..#...#.####..######..
#####.##...#.#....#....#.#
.#####.##.#.#####..##.#...
#..##..##.#.##.##.####..##
.##..####..#..####.#######
#.#..#.##.#.######....##..
.#.##.##.####......#.##.##
INPUT

# input = <<INPUT.split("\n")
# .#..##.###...#######
# ##.############..##.
# .#.######.########.#
# .###.#######.####.#.
# #####.##.#.##.###.##
# ..#####..#.#########
# ####################
# #.####....###.#.#.##
# ##.#################
# #####.##.###..####..
# ..######..##.#######
# ####.##.####...##..#
# .#####..#.######.###
# ##...#.##########...
# #.##########.#######
# .####.#.###.###.#.##
# ....##.##.###..#####
# .#.#.###########.###
# #.#.#.#####.####.###
# ###.##.####.##.#..##
# INPUT

h, w = input[0].length, input.count
puts "width: #{w}, height: #{h}"

Asteroid = Struct.new(:num, :x, :y, :visible, :others)
Pair = Struct.new(:a, :b, :angle, :dist, :degrees)

puts "parsing"
a = []
n = 0
for x in 0...w do
  for y in 0...h do
    if input[y][x] == "#"
      a << Asteroid.new(n, x.to_f, y.to_f, 0, [])
      n += 1
    end
  end
end

def dist(a, b)
  return Math.sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
end

def angle(a, b)
  Math.atan2(b.y - a.y, b.x - a.x)
end

def degrees(a, b)
  180 - angle(a, b) * 180.0 / Math::PI
end

puts "computing pairs"
for i in 0...a.count
  for j in 0...a.count
    if i != j
      a[i].others << Pair.new(a[i], a[j], angle(a[i], a[j]), dist(a[i], a[j]), degrees(a[i], a[j]))
    end
  end  
end

puts "counting visible pairs"
z = 0
a.each do |i|
  c = 0
  l = nil
  i.others.sort_by{|b| [b.angle, b.dist]}.each do |p|
    if p.angle != l
      c += 1
      l = p.angle
    end
    # puts "  #{p.a.num} (#{p.a.x},#{p.a.y}) <-> #{p.b.num} (#{p.b.x},#{p.b.y}) = #{p.angle}, #{p.dist} ... #{c}"
  end
  i.visible = c
  # puts "#{i.num} (#{i.x},#{i.y}) - #{i.visible}"
end

max = a.max_by{|b| b.visible}
puts "max: #{max.num} (#{max.x},#{max.y}) = #{max.visible}"

puts "part 2"

c = 0
la = nil
max.others.sort_by{|b| [b.degrees, b.dist]}.each do |b|
  if b.degrees != la
    c += 1
    puts "#{c}: #{b.b.x * 100 + b.b.y}"
    la = b.degrees
  end
  if b.b.x * 100 + b.b.y == 612.0
    puts "**************************************************"
  end
  puts "   #{b.b.x * 100 + b.b.y} - #{b.degrees} - #{b.dist}"
end