#!/usr/bin/ruby -w

# input = <<-INPUT
# .#.
# ..#
# ###
# INPUT

input = <<-INPUT
.###.#.#
####.#.#
#.....#.
####....
#...##.#
########
..#####.
######.#
INPUT

grid = []
grid[0] = []
grid[0][0] = input.split("\n").map {|r| r.chars.map {|c| c == "#" ? 1 : 0}}

def cube_at(grid, x, y, z, w)
    sx, sy, sz, sw = grid[0][0][0].length, grid[0][0].length, grid[0].length, grid.length
    return 0 unless x.between?(0,sx-1) && y.between?(0,sy-1) && z.between?(0,sz-1) && w.between?(0,sw-1)
    grid[w][z][y][x]
end

def active_cubes_around(grid, x, y, z, w)
    a = []
    for dw in -1..1
        a[dw + 1] = []
        for dz in -1..1
            a[dw + 1][dz + 1] = []
            for dy in -1..1
                a[dw + 1][dz + 1][dy + 1] = []
                for dx in -1..1
                    a[dw + 1][dz + 1][dy + 1][dx + 1] = 0
                end
            end
        end
    end

    c = 0
    for dw in -1..1
        for dz in -1..1
            for dy in -1..1
                for dx in -1..1
                    cube = cube_at(grid, x+dx, y+dy, z+dz, w+dw)
                    a[dw + 1][dz + 1][dy + 1][dx + 1] = cube
                    unless dx == 0 && dy == 0 && dz == 0 && dw == 0
                        c += cube
                    end
                end
            end
        end
    end

    # pretty "around (#{x}, #{y}, #{z})", a
    c
end

def cycle(grid)
    sx, sy, sz, sw = grid[0][0][0].length + 2, grid[0][0].length + 2, grid[0].length + 2, grid.length + 2
    gen1 = []
    gen2 = []

    for w in 0..sw - 1
        gen1[w] = []
        gen2[w] = []
        for z in 0..sz - 1
            gen1[w][z] = []
            gen2[w][z] = []
            for y in 0..sy - 1
                gen1[w][z][y] = []
                gen2[w][z][y] = []
                for x in 0..sx - 1
                    gen1[w][z][y][x] = cube_at(grid, x - 1, y - 1, z - 1, w - 1)
                    gen2[w][z][y][x] = 0
                end
            end
        end
    end

    # puts ">>>> START OF CYCLE <<<<<"
    # pretty "gen 1", gen1
    # pretty "gen 2", gen2
    # gets
    
    for w in 0..sw - 1
        for z in 0..sz - 1
            for y in 0..sy - 1
                for x in 0..sx - 1
                    current = cube_at(gen1, x, y, z, w)
                    active = active_cubes_around(gen1, x, y, z, w)
                    cube = current

                    # puts "    (#{x},#{y},#{z}) = #{cube}, #{active} active neighbors"
                    if current == 1
                        unless active.between?(2,3)
                            # puts "--- deactivating"
                            cube = 0 
                        end
                    end

                    if current == 0
                        if active == 3
                            # puts "+++ activating"
                            cube = 1
                        end
                    end

                    gen2[w][z][y][x] = cube
                end
            end
        end
    end

    # puts "<<<<< END OF CYCLE >>>>"
    # pretty "gen 1", gen1
    # pretty "gen 2", gen2
    # gets

    gen2
end

def pretty(name, grid)
    times = grid.length
    planes = grid[0].length
    rows = grid[0][0].length

    puts "----------------------[ #{name} ]----------------------"
    for time in 0..times-1
        for row in 0..rows-1
            for plane in 0..planes-1
                grid[time][plane][row].each do |col|
                    print "_.#"[col+1]
                end
                print "  "
            end
            puts
        end
        puts
    end
end

def sum_of(grid)
    c = 0
    grid.each do |time|
        time.each do |plane|
            plane.each do |row|
                row.each do |col|
                    c += col
                end
            end
        end
    end
    c
end


pretty "input", grid
gets

for g in 1..6
    grid = cycle(grid)
    pretty "cycle #{g}", grid
    puts "sum #{sum_of(grid)}"
    gets
end

