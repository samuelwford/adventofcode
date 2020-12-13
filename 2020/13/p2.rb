#!/usr/bin/ruby -w

# input data
schedule = "19,x,x,x,x,x,x,x,x,x,x,x,x,37,x,x,x,x,x,383,x,x,x,x,x,x,x,23,x,x,x,x,13,x,x,x,x,x,x,x,x,x,x,x,x,x,x,x,29,x,457,x,x,x,x,x,x,x,x,x,41,x,x,x,x,x,x,17"

# test data
# schedule = "7,13,x,x,59,x,31,19"

buses = schedule.split(',').map(&:to_i).each_with_index.map {|i,j| [i,j]}.reject {|i,j| i == 0}

# do it in pairs unstead of all at once

offset = 0
period = buses[0][0]
for i in (0..buses.length-1)
  bus = buses[i]
  while (offset + bus[1]) % bus[0] != 0
    offset += period
  end
  period *= bus[0]
end

puts offset