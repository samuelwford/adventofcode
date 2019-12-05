file = "input.txt"
# file = "test1.txt"
# file = "test2.txt"

dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + (ARGV[0] || file)

filename # => "input.txt"

def letter_counts(s)
  s.each_char.group_by{ |i| i }.map{ |k,v| [k, v.count] }
end

letter_counts "abcdef" # => [["a", 1], ["b", 1], ["c", 1], ["d", 1], ["e", 1], ["f", 1]]
letter_counts "bababc" # => [["b", 3], ["a", 2], ["c", 1]]
letter_counts "aabcdd" # => [["a", 2], ["b", 1], ["c", 1], ["d", 2]]

codes = File.readlines(filename)

# part 1

counts = codes.map{ |l| letter_counts(l) }

doubles = counts.select { |code| code.select{ |pair| pair[1] == 2 }.count > 0 }.count
doubles # => 247

triples = counts.select { |code| code.select{ |pair| pair[1] == 3 }.count > 0 }.count
triples # => 29

doubles * triples # => 7163

# part 2

split_codes = codes.map { |code| code.split('') }

near_matches = []
for i in 0..(split_codes.count - 2) do
  for j in (i + 1)..(split_codes.count - 1) do
    c1, c2 = split_codes[i], split_codes[j]
    differences = c1.zip(c2).select { |p| p[0] != p[1] }
    near_matches << [c1, c2, differences.first] if differences.count == 1    
  end
end

near_matches # => [[["i", "g", "h", "f", "b", "b", "y", "i", "j", "n", "o", "u", "m", "x", "j", "l", "x", "e", "v", "a", "c", "p", "w", "q", "t", "r", "\n"], ["i", "g", "h", "f", "b", "s", "y", "i", "j", "n", "o", "u", "m", "x", "j", "l", "x", "e", "v", "a", "c", "p", "w", "q", "t", "r", "\n"], ["b", "s"]]]
near_matches.map{ |n| n[0].select{ |l| l != n[2][0] and l != "\n" } }.map{ |n| n.reduce(:+) } # => ["ighfyijnoumxjlxevacpwqtr"]
near_matches[0][0].reduce(:+) # => "ighfbbyijnoumxjlxevacpwqtr\n"

# answer is acutally: ighfbyijnoumxjlxevacpwqtr
# had to remove only the single character that matches, not all instanced of that character
