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

def check_ticket(rules, ticket)
    # puts "scanning ticket: #{ticket.inspect}"
    # ticket.each do |field|
    #     puts " - testing field #{field}"
    #     rules.each do |rule, ranges| 
    #         valid = ranges[0] === field || ranges[1] === field
    #         puts "   - FAIL rule #{rule}, #{ranges}" unless valid
    #     end    
    # end
    ticket.reject {|f| rules.each_value.any? {|r| r[0] === f || r[1] === f}}
end

puts nearby.flat_map {|t| check_ticket(rules, t)}.sum