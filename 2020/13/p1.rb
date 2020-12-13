#!/usr/bin/ruby -w

# input data
mark = 1000391
schedule = "19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,383,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,457,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"

# test data
# mark = 939
# schedule = "7,13,x,x,59,x,31,19"

buses = schedule.split(',').reject {|i| i == 'x'}.map(&:to_i)
times = buses.map do |i| 
  q, m = mark.divmod(i)
  w = i - m
  [i, m, w, i * w]
end
times.sort! { |a,b| a[2] <=> b[2] }

times.each {|t| puts t.inspect}