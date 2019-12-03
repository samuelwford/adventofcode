filename = __dir__ + "/" + (ARGV[0] || "test1.txt")

puts filename

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
    if p1.x < p2.x or p1.y < p2.y
      @p1 = p1
      @p2 = p2
    else  
      @p1 = p2
      @p2 = p1
    end
  end
  
  def horizontal?
    @p1.y == @p2.y
  end
  
  def vertical?
    @p1.x == @p2.x
  end
  
  def to_s
    "#{horizontal? ? 'H' : 'V'}#{@p1}-#{@p2}"
  end
end

def sort_segments(segments)
  horizontals = segments.select { |segment| segment.horizontal? }
  verticals = segments.select { |segment| segment.vertical? }
    
  [horizontals, verticals]
end

def find_intersection(h, v)  
  result = []
  if h.p1.y.between?(v.p1.y, v.p2.y) and v.p1.x.between?(h.p1.x, h.p2.x)
    result = [v.p1.x, h.p1.y]
    p = Point.new(v.p1.x, h.p1.y)
  end
  
  result
end

def find_intersections(set1, set2)
  h1, v1 = sort_segments(set1)
  h2, v2 = sort_segments(set2)
  
  intersections = []

  h1.each do |h|
    v2.each do |v|
      i = find_intersection(h, v)
      intersections << i unless i == [] or i == [0,0]
    end
  end
  
  v1.each do |v|
    h2.each do |h|
      i = find_intersection(h, v)
      intersections << i unless i == [] or i == [0,0]
    end
  end
  
  intersections.map { |i| i[0].abs() + i[1].abs() }
end

lines = File.readlines(filename)

segments = [parse(lines[0]), parse(lines[1])]
puts segments[0].join(" ")
puts segments[1].join(" ")

# look for intersections

intersections = find_intersections(segments[0], segments[1])
puts intersections.sort.inspect