dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + (ARGV[0] || "test2.txt")

filename # => "test2.txt"

def parse(line)
  directives = line.split(',')
  
  segments = []
  
  p1 = Point.new(0, 0)
  
  directives.each do |directive| 
    op = directive[0]
    run = directive[1..directive.length].to_i
    
    p2 = p1.copy
    
    case op
    when "R"
      p2.x += run
    when "L"
      p2.x -= run
    when "U"
      p2.y += run
    when "D"
      p2.y -= run
    end
    
    line = Line.new(p1, p2)
    segments << line
    
    p1 = p2.copy
  end
  
  segments
end

def compute_trail(set)
  set.map { |l| [l.length, l]}
end

class Point
  attr_accessor :x
  attr_accessor :y
  
  def initialize(x, y)
    @x = x
    @y = y
  end
  
  def copy
    Point.new(@x, @y)
  end
  
  def to_s
    "(#{@x},#{@y})"
  end
end

class Line
  attr_accessor :p1
  attr_accessor :p2
  
  def initialize(p1, p2)
    @p1 = p1
    @p2 = p2
  end
  
  def horizontal?
    @p1.y == @p2.y
  end
  
  def vertical?
    @p1.x == @p2.x
  end
  
  def parallel_to?(line)
    (horizontal? and line.horizontal?) or (vertical? and line.vertical?)
  end
  
  def length
    if horizontal?
      return (@p2.x - @p1.x).abs()
    else
      return (@p2.y - @p1.y).abs()
    end
  end
  
  def to_s
    "#{horizontal? ? 'H' : 'V'}#{@p1}-#{@p2}"
  end
  
  def inspect
    to_s
  end
  
  def intersects_with?(line)
    return false if parallel_to?(line) 
    
    if horizontal? 
      return (is_between?(@p1.y, line.p1.y, line.p2.y) and is_between?(line.p1.x, @p1.x, @p2.x))
    else
      return (is_between?(line.p1.y, @p1.y, @p2.y) and is_between?(@p1.x, line.p1.x, line.p2.x))
    end
  end

  def point_of_intersection_with(line)
    h, v = self, line if horizontal?
    h, v = line, self if vertical?
    
    Point.new(v.p1.x, h.p1.y)
  end
  
  def distance_from_start_to(point)
    (point.x - @p1.x).abs() + (point.y - @p1.y).abs()
  end
  
  def is_between?(a, x, y)
    a.between?([x,y].min, [x,y].max)
  end
end

lines = File.readlines(filename)

set1, set2 = parse(lines[0]), parse(lines[1])

set1 # => [H(0,0)-(8,0), V(8,0)-(8,5), H(8,5)-(3,5), V(3,5)-(3,2)]
set2 # => [V(0,0)-(0,7), H(0,7)-(6,7), V(6,7)-(6,3), H(6,3)-(2,3)]

puts "set1: " + set1.join(" ")
puts "set2: " + set2.join(" ")

length1 = 0
set1.each do |line1|
  length2 = 0
  set2.each do |line2|
    if line1.intersects_with?(line2)
      intersection = line1.point_of_intersection_with(line2)
      i2l = length2 + line2.distance_from_start_to(intersection)
      i1l = length1 + line1.distance_from_start_to(intersection)
      il = i1l + i2l
      puts "found an intersection at #{intersection} at length #{i1l} + #{i2l} = #{il}"
    end
    length2 += line2.length
  end
  length1 += line1.length
end

# >> set1: H(0,0)-(8,0) V(8,0)-(8,5) H(8,5)-(3,5) V(3,5)-(3,2)
# >> set2: V(0,0)-(0,7) H(0,7)-(6,7) V(6,7)-(6,3) H(6,3)-(2,3)
# >> found an intersection at (0,0) at length 0 + 0 = 0
# >> found an intersection at (6,5) at length 15 + 15 = 30
# >> found an intersection at (3,3) at length 20 + 20 = 40
