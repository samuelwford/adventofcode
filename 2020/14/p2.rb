#!/usr/bin/ruby -w

lines = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)

mem = {}
bitmask = 0
bitmap = 0
bits = []
mask = "0" * 35

lines.each do |line|
    # puts line
    parts = line.split(" = ")
    if parts[0] == "mask"
        mask = parts[1]
        bitmask = mask.gsub(/[10]/, '1').gsub(/X/, '0').to_i(2)
        bitmap = mask.gsub(/X/, '0').to_i(2)
        bits = mask.chars.each_index.select {|i| mask[i] == 'X'}.map {|i| 35 - i}.reverse
        gets
    else
        base, val = parts[0][4..-2].to_i, parts[1].to_i
        # puts "==================="
        # puts line
        # puts ""

        for i in 0..(2**bits.length - 1)
            # puts "computing bit #{i} ..."
            offset = 0
            for b in 0..bits.length - 1
                offset += 2**bits[b] if i & 2**b > 0
            end
            
            # bar = "-" * 36

            # bitmask_bin = '%036b' % bitmask
            # base_bin   = '%036b' % base

            masked_base = base & bitmask
            # masked_base_bin = '%036b' % masked_base

            mapped_base = masked_base | bitmap
            # mapped_base_bin = '%036b' % mapped_base

            # bitmap_bin = '%036b' % bitmap

            with_offset = mapped_base | offset
            with_offset_bin = '%036b' % with_offset

            # i_bin      = "%0#{bits.length}b" % i
            # offset_bin = '%036b' % offset

            # puts "mask:   #{mask}"
            # puts ""
            # puts "base:   #{base_bin} (#{base})"
            # puts "mask:   #{bitmask_bin}"
            # puts "        #{bar}"
            # puts "        #{masked_base_bin}"
            # puts ""
            # puts "        #{masked_base_bin}"
            # puts "bitmap: #{bitmap_bin}"
            # puts "        #{bar}"
            # puts "        #{mapped_base_bin}"
            # puts ""
            # puts "        #{mapped_base_bin}"
            # puts "offset: #{offset_bin} (#{i_bin})"
            # puts "        #{bar}"
            # puts "final:  #{with_offset_bin} (#{with_offset})"
            # puts ""
            # gets

            mem[with_offset_bin] = val
        end
    end
end

puts mem.values.sum