dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + (ARGV[0] || "test1.txt")

filename # => "test1.txt"

lines = File.readlines(filename)
lines # => ["a\n", "b\n", "c\n"]
