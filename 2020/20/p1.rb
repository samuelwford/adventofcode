#!/usr/bin/ruby -w

input = File.read(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)

tiles = input.split("\n\n").each_with_object({}) do |tile, o|
    lines = tile.split("\n").map(&:chomp)
    id, bitmap = lines[0][5..8], lines[1..]
    o[id] = bitmap
end

edges = {}
t = {}

def rotate(sides)
    [sides[3], sides[0].reverse, sides[1], sides[2].reverse]
end

tiles.each do |id, bitmap|
    east = bitmap.map {|r| r[-1]}.join
    west = bitmap.map {|r| r[0]}.join
    north = bitmap[0]
    south = bitmap[-1]

    identity   = [east, south, west, north]
    rotate_90  = rotate identity
    rotate_180 = rotate rotate_90
    rotate_270 = rotate rotate_180

    flip_h     = [west, south.reverse, east, north.reverse]
    flip_h_90  = rotate flip_h
    flip_h_180 = rotate flip_h_90
    flip_h_270 = rotate flip_h_180

    flip_v     = [east.reverse, north, west.reverse, south]
    flip_v_90  = rotate flip_v
    flip_v_180 = rotate flip_v_90
    flip_v_270 = rotate flip_v_180

    t[id] = { id: id, bitmap: bitmap, orientations: [
        identity, rotate_90, rotate_180, rotate_270, flip_h, flip_h_90, flip_h_180, flip_h_270, flip_v, flip_v_90, flip_v_180, flip_v_270
    ]}

    [east, west, north, south, east.reverse, west.reverse, north.reverse, south.reverse].each do |edge|
        if edges.has_key?(edge)
            edges[edge] << id unless edges[edge].include? id
        else
            edges[edge] = [id]
        end
    end
end

edges.each do |k,v|
    puts v.inspect if v.count == 1
end

t.each do |tile|
    id, orientations = tile[:id], tile[:orientations]
    orientations.map {|e| e[0]}.each do |east|
        # edges[east].each do |id|
        #     unless id == t[:id]
        #        t. 
        #     end
        # end
        puts "Tile #{id} East Edge #{east} Matches: #{edges[id].inspect}"
    end
end
