file = "input.txt"
# file = "test1.txt"
# file = "test2.txt"

dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + file

filename # => "input.txt"

class Rect
  attr_accessor :x
  attr_accessor :y
  attr_accessor :w
  attr_accessor :h
  
  def initialize(x, y, w, h)
    @x, @y, @w, @h = x.to_i, y.to_i, w.to_i, h.to_i
  end
  
  def left
    @x
  end
  
  def right
    @x + @w - 1
  end
  
  def top
    @y
  end
  
  def bottom
    @y + @h - 1
  end
  
  def area
    @w * @h
  end
  
  def intersects?(rect)
    left < rect.right and right > rect.left and top < rect.bottom and bottom > rect.top
  end
  
  def intersection(rect)
    return nil unless intersects?(rect)
    
    l = [left, rect.left].max
    r = [right, rect.right].min
    t = [top, rect.top].max
    b = [bottom, rect.bottom].min
    
    w = r - l + 1
    h = b - t + 1
    
    Rect.new(l, t, w, h)
  end
  
  def inspect
    "(#{@x},#{@y})-(#{right},#{bottom})"
  end
  
  def to_s
    inspect
  end
end

class Claim
  attr_accessor :num
  attr_accessor :rect
  
  def initialize(num, rect)
    @num, @rect = num.to_i, rect
  end
  
  def self.parse(string)
    m = string.match(/#(?<num>\d+)\s+@\s+(?<x>\d+),(?<y>\d+)\:\s+(?<w>\d+)x(?<h>\d+)/)
    Claim.new(m[:num], Rect.new(m[:x], m[:y], m[:w], m[:h]))
  end
  
  def inspect
    "<##{@num}: #{@rect}>"
  end
end

claims = File.readlines(filename).map{|line| Claim.parse(line)}

# r = claims.max_by{|c| c.rect.right }.rect.right
# r # => 999
# b = claims.max_by{|c| c.rect.bottom }.rect.bottom
# b # => 998
#
# a = Array.new(1000 * 1000, 0)
# a.count # => 1000000
#
# claims.each do |c|
#   for x in c.rect.left..c.rect.right
#     for y in c.rect.top..c.rect.bottom
#       a[y * 1000 + x] += 1
#     end
#   end
# end
#
# a.select!{|x| x > 1 }
# a.count # => 118840

a = Array.new(1000 * 1000, [])
a.count # => 1000000
a[1000] # => []

claims.each do |c|
  for x in c.rect.left..c.rect.right
    for y in c.rect.top..c.rect.bottom
      i = y * 1000 + x
      a[i] << c
    end
  end
end

a.count # => 1000000
a[1000] # => 
