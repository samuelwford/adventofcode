#!/usr/bin/ruby -w

input = File.read(ARGV[0] || File.join(File.dirname(__FILE__), "input.txt"), chomp: true)
rules, messages = input.split("\n\n", 2)

rules = rules.split("\n").each_with_object({}) do |rule, obj|
    id, crit = rule.split(": ")
    if crit.start_with?('"')
        obj[id] = { id: id, type: :char, crit: crit[1] }
    else
        ids = crit.split(" | ").map { |s| s.split(" ") }
        obj[id] = { id: id, type: :lookup, crit: ids}
    end
end

messages = messages.split("\n")

def rule_is_valid?(msg, i, id, rules) 
    c, r = msg[i], rules[id.to_s]
    # print "does '#{c}' (pos #{i}) match #{r}? "
    case r[:type]
    when :char
        if c == r[:crit]
            puts "PASS character #{c} matches rule #{id}, #{r[:crit]}"
            return true
        else
            puts "FAIL character #{c} DOES NOT match rule #{id}, #{r[:crit]}"
            return false
        end
    when :lookup
        # puts "..."
        return r[:crit].any? do |sub_ids| 
            puts "checking string of rules with ids: #{sub_ids.inspect}"
            sub_ids.each_with_index.all? do |sub_id, sub_i| 
                puts "checking rule #{sub_id} at index #{sub_i} (#{i} + #{sub_i} = #{i + sub_i}) ..."
                rule_is_valid?(msg, i + sub_i, sub_id, rules)
            end
        end
    end
end

def is_valid?(msg, rules)
    for i in 0..msg.length - 1
        for id in 0..rules.keys.count - 1
            unless rule_is_valid?(msg, i, id, rules)
                return false
            end
        end
    end
    return true
end

messages.each do |msg|
    valid = rule_is_valid?(msg, 0, "0", rules)
    puts "#{msg}: #{valid}"
end