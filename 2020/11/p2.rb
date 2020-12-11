#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)
#input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "test.txt"), chomp: true)

grid = input #.map {|r| r.chars.map {|c| c == ""}}

def seat_value(x, y, dx, dy, grid)
  i, v, x1, y1, h, w = 1, 0, x, y, grid.length, grid[0].length
  size = [w, h].max

  # move in dx,dy direction until a seat is seen or we fall off the edge
  while i < size
    x1, y1 = x + dx * i, y + dy * i
    break unless x1.between?(0, w-1) && y1.between?(0, h-1)
    case grid[y1][x1]
    when 'L'
      break
    when '#'
      v = 1
      break
    else
      i += 1
    end
  end
  v
end

def occupied_seats_around(x, y, grid)
  c = 0
  c += seat_value(x, y, -1, -1, grid)
  c += seat_value(x, y,  0, -1, grid)
  c += seat_value(x, y,  1, -1, grid)
  c += seat_value(x, y, -1,  0, grid)
  c += seat_value(x, y,  1,  0, grid)
  c += seat_value(x, y, -1,  1, grid)
  c += seat_value(x, y,  0,  1, grid)
  c += seat_value(x, y,  1,  1, grid)
  c
end

def apply(x, y, grid, output)
  case grid[y][x]
  when '.'
    # skip
  when 'L'
    output[y][x] = '#' if occupied_seats_around(x, y, grid) == 0
  when '#'
    output[y][x] = 'L' if occupied_seats_around(x, y, grid) > 4
  end
end

def cycle(grid)
  h, w = grid.length, grid[0].length
  output = grid.clone.map(&:clone)
  for y in 0..h - 1
    for x in 0..w - 1
      apply(x, y, grid, output)
    end
  end
  output
end

def occupied_count(grid)
  c, h, w = 0, grid.length, grid[0].length
  for y in 0..h-1
    for x in 0..w-1
      c += 1 if grid[y][x] == '#'
    end
  end
  c
end

g = 0
while true
  # puts "\n---[ gen #{g} ]---"
  # puts grid

  next_gen = cycle(grid)
  if next_gen == grid
    c = occupied_count(next_gen)
    puts "stable at gen #{g} with #{c} seats occupied"
    break
  end

  grid = next_gen
  g += 1
end
