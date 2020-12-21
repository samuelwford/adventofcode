#!/usr/bin/ruby -w
require "set"

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)

all_words = Set.new
foods = []

ndx = input.each_with_object({}) do |line, map|
    a, b = line.split(" (contains ")
    words, allergens = a.split(" "), b.split(" ").map {|w| w[0..-2]}
    allergens.each do |allergen|
        if map.has_key?(allergen)
            map[allergen] = map[allergen].intersection(words)
        else
            map[allergen] = words.to_set
        end
    end
    all_words.merge words
    foods << words
end

ans = {}
ndx.sort_by {|k,v| v.length}.each do |k,v|
    w = ndx[k].to_a[0]
    ans[k] = w
    all_words.delete w
    ndx.each do |k1,v2|
        v2.delete w
    end
end

puts all_words.map {|w| foods.map {|f| f.count(w)}.sum }.sum

puts ans.sort_by {|k,v| k}.map {|k,v| v}.join(",")