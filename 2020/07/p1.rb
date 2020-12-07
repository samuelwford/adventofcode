#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
input = input.map {|x| x.delete_suffix(".\n")}

def parse(line)
  container, contains = line.split(" contain ")
  bags = contains.split(", ")
  
  container.delete_suffix!(" bags")
  bags = bags.map {|x| x.delete_suffix("s").delete_suffix(" bag").split(" ", 2) }
  bags = bags.map {|x| { color: x[1], count: x[0].to_i } }
  
  { color: container, bags: bags }
end

def find_bags_to_hold(bag, rules)
  applicable = rules.select { |rule| rule[:bags].any? { |b| b[:color] == bag } }.map { |rule| rule[:color] }
  applicable |= applicable.flat_map { |bag| find_bags_to_hold(bag, rules) }
  
  applicable
end

rules = input.map {|line| parse(line) }
bags = find_bags_to_hold("shiny gold", rules)

puts bags.sort.uniq.length

