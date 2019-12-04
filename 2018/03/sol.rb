# file = "input.txt"
file = "test1.txt"
# file = "test2.txt"

dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + file

filename # => "test1.txt"

claims = File.readlines(filename)
claims # => ["#1 @ 1,3: 4x4\n", "#2 @ 3,1: 4x4\n", "#3 @ 5,5: 2x2"]

parsed = claims.map{|c|c.match(/#(?<num>\d+)\s+@\s+(?<x>\d+),(?<y>\d+)\:\s+(?<w>\d+)x(?<h>\d+)/)}
parsed # => [#<MatchData "#1 @ 1,3: 4x4" num:"1" x:"1" y:"3" w:"4" h:"4">, #<MatchData "#2 @ 3,1: 4x4" num:"2" x:"3" y:"1" w:"4" h:"4">, #<MatchData "#3 @ 5,5: 2x2" num:"3" x:"5" y:"5" w:"2" h:"2">]

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
  
  def intersects?(rect)
    left < rect.right and right > rect.left and top < rect.bottom and bottom > rect.top
  end
  
  def intersection(rect)
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
    @num, @rect = num, rect
  end
  
  def inspect
    "<##{@num}: #{@rect}>"
  end
end

objects = parsed.map{|m| Claim.new(m[:num], Rect.new(m[:x], m[:y], m[:w], m[:h]))}
objects # => [<#1: (1,3)-(4,6)>, <#2: (3,1)-(6,4)>, <#3: (5,5)-(6,6)>]

a, b, c = objects[0], objects[1], objects[2]

a # => <#1: (1,3)-(4,6)>
b # => <#2: (3,1)-(6,4)>
c # => <#3: (5,5)-(6,6)>

a.rect.intersects?(b.rect) # => true
b.rect.intersects?(a.rect) # => true
a.rect.intersects?(c.rect) # => false

a.rect.intersection(b.rect) # => (3,3)-(4,4)
