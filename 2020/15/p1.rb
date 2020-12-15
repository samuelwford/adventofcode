#!/usr/bin/ruby -w


def next_in_seq(seq)
    last = seq.last
    nxt  = 0

    diff = 0
    while diff < seq.length - 1
        diff += 1
        if seq[seq.length - 1 - diff] == last
            nxt = diff
            break
        end
    end
    
    nxt
end

def play(seq, rounds)
    print "playing: #{seq.inspect} ... "
    while seq.length < rounds
        seq.append(next_in_seq(seq))
    end
    print seq.last, "  "
    seq.last
end


puts play([0,3,6], 10) == 0 ? "pass" : "fail"
puts play([0,3,6], 2020) == 436 ? "pass" : "fail"
puts play([1, 3, 2], 2020) == 1 ? "pass" : "fail"
puts play([2, 1, 3], 2020) == 10 ? "pass" : "fail"
puts play([2,3,1], 2020) == 78 ? "pass" : "fail"
puts play([3,2,1], 2020) == 438 ? "pass" : "fail"
puts play([3,1,2], 2020) == 1836 ? "pass" : "fail"

play([14,1,17,0,3,20], 2020)
puts