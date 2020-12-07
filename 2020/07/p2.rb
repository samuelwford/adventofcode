#!/usr/bin/ruby -w

input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"))
#input = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "test.txt"))
input = input.map {|x| x.chomp.delete_suffix(".")}

def parse(line)
  container, contains = line.split(" contain ")
  container.delete_suffix!(" bags")
  bags = contains.split(", ")
  
  return { color: container, bags: [] } if contains == "no other bags"
  
  bags = bags.map {|x| x.delete_suffix("s").delete_suffix(" bag").split(" ", 2) }
  bags = bags.map {|x| { color: x[1], count: x[0].to_i } }
  
  { color: container, bags: bags }
end

def find_bags_in(bag, rules, l)
  rule = rules.select { |r| r[:color] == bag }.first
  bags = rule[:bags]
  
  return 1 if bags.length == 0
  
  count = bags.map { |b| b[:count] * find_bags_in(b[:color], rules, l + 1) }
  count.sum + 1
end

rules = input.map {|line| parse(line) }

puts find_bags_in("shiny gold", rules, 0) - 1

