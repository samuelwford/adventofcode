#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)
#input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "test.txt"), chomp: true)

grid = input #.map {|r| r.chars.map {|c| c == ""}}

def seat_value(x, y, grid)
  v = 0
  if y.between?(0, grid.length - 1) && x.between?(0, grid[y].length - 1)
    v = 1 if grid[y][x] == '#'
  #   puts "(#{x}, #{y}) = #{grid[y][x]} (#{v})"
  # else
  #   puts "(#{x}, #{y}) = OOB (#{v})"
  end
  v
end

def occupied_seats_around(x, y, grid)
  c = 0
  c += seat_value(x - 1, y - 1, grid)
  c += seat_value(x    , y - 1, grid)
  c += seat_value(x + 1, y - 1, grid)
  c += seat_value(x - 1, y    , grid)
  c += seat_value(x + 1, y    , grid)
  c += seat_value(x - 1, y + 1, grid)
  c += seat_value(x    , y + 1, grid)
  c += seat_value(x + 1, y + 1, grid)
  c
end

def apply(x, y, grid, output)
  case grid[y][x]
  when '.'
    # skip
  when 'L'
    output[y][x] = '#' if occupied_seats_around(x, y, grid) == 0
  when '#'
    output[y][x] = 'L' if occupied_seats_around(x, y, grid) > 3
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
  #puts "\n---[ gen #{g} ]---"
  #puts grid

  next_gen = cycle(grid)
  if next_gen == grid
    c = occupied_count(next_gen)
    puts "stable at gen #{g} with #{c} seats occupied"
    break
  end

  grid = next_gen
  g += 1
end
