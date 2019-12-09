file = "input.txt"
# file = "test1.txt"
# file = "test2.txt"

dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + file

filename # => "input.txt"

log = File.readlines(filename)

guards = {}

g = ""
log.each do |l|
  day = l[1..10]
  time = l[12..16]
  msg = l[19..log.length]
  
  case msg[0]
  when "G"
    g = msg.match(/\d+/).to_s
  when "f"
    a = guards[g] || {}
    b = a[day] || []
    
    b << "#{time} S"
    
    a[day] = b
    guards[g] = a
  when "w"
    a = guards[g] || {}
    b = a[day] || []
    
    b << "#{time} W"
    
    a[day] = b
    guards[g] = a
  end    
end

names = guards.keys.sort

names.each do |name|
  puts "guard #{name} -"
  
  logs = guards[name]
  days = logs.keys.sort
  
  days.each do |day|
    times = logs[day]
    puts "  #{day}: " + times.sort.join(", ")
  end
end
