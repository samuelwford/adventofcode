#!/usr/bin/ruby -w

lines = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)

mem = []
bitmask = 0
bitmap = 0

lines.each do |line|
    parts = line.split(" = ")
    if parts[0] == "mask"
        bitmask = parts[1].gsub(/[10]/, '0').gsub(/X/, '1').to_i(2)
        bitmap = parts[1].gsub(/X/, '0').to_i(2)
    else
        addr, val = parts[0][4..-2].to_i, parts[1].to_i
        mem[addr] = (val & bitmask) | bitmap
    end
end

puts mem.compact.sum