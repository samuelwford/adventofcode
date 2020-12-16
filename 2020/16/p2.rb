#!/usr/bin/ruby -w

lines = File.readlines(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)

rules = {}
ticket = []
nearby = []

mode = "rules"
lines.each do |line|
    next if line == ""
    
    if line == "your ticket:"
        mode = "ticket"
        next
    end

    if line == "nearby tickets:"
        mode = "nearby"
        next
    end

    case mode
    when "rules"
        field, rule = line.split(": ")
        ranges = rule.split(" or ")
        ranges.map! do |r|
            n = r.split('-').map(&:to_i)
            (n[0]..n[1])
        end
        rules[field] = ranges

    when "ticket"
        ticket = line.split(',').map(&:to_i)

    when "nearby"
        nearby << line.split(',').map(&:to_i)

    end
end

def is_valid?(rules, ticket)
    ticket.all? {|f| rules.each_value.any? {|r| r[0] === f || r[1] === f}}
end

valid = nearby.select {|t| is_valid?(rules, t)}

def find_field(rule, nearby, ticket)
    for i in 0..ticket.length - 1
        fields = nearby.map {|t| t[i]}.reject {|f| rule[0] === f || rule[1] === f}
        puts "##{i} passes" if fields.length == 0
    end
end

def find(rule, nearby, ticket)
    passing = []
    for i in 0..ticket.length - 1
        fields = nearby.map {|t| t[i]}.reject {|f| rule[0] === f || rule[1] === f}
        passing << i if fields.length == 0
    end
    passing
end

possible = rules.map { |n, r| [n, find(r, valid, ticket)] }
         .sort_by { |n, p| p.count }
         
result = {}
possible.each do |name, positions|
    num = positions.first
    result[name] = num
    possible.each {|_n, p| p.delete(num)}
end

puts result.select {|field, position| field.start_with?("departure")}
           .map { |field, position| ticket[position] }
           .reduce(1) { |product, num| product * num }

# possible = rules.each.
#     map { |name, rule| [name, find(rule, valid, ticket)] }.
#     sort do |name, positions|
#         puts "- #{name}: #{positions.inspect}"
#         positions.count
#     end

# puts possible.inspect