file = "input.txt"
# file = "test1.txt"
# file = "test2.txt"

dir = __dir__.nil? ? "" : __dir__ + "/"
filename = dir + (ARGV[0] || file)

filename # => "input.txt"

program = File.read(filename).split(",").map{|x| x.to_i }

def execute(program, input)
  ic = 0
  acc = input
  
  while program[ic] != 99 do
    instruction = program[ic]
    
    field = "%05d" % instruction
    
    op = field[3..4]
    mode = []
    mode[0] = field[2]
    mode[1] = field[1]
    mode[2] = field[0]
    
    params = []
    desc = []
    
    case op
    when "01"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      result = params[0] + params[1]
      
      desc[0] = "value #{params[0]}" + (mode[0] == "0" ? " from %03d" % program[ic + 1] : "")
      desc[1] = "value #{params[1]}" + (mode[1] == "0" ? " from %03d" % program[ic + 2] : "")
      
      puts "%03d: %s,%d,%d,%d - add %s + %s, store %05d in %03d" % [ic, field, program[ic + 1], program[ic + 2], program[ic + 3], desc[0], desc[1], result, params[2]]
      
      program[params[2]] = result
      ic += 4
      
    when "02"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      result = params[0] * params[1]
      
      desc[0] = "value #{params[0]}" + (mode[0] == "0" ? " from %03d" % program[ic + 1] : "")
      desc[1] = "value #{params[1]}" + (mode[1] == "0" ? " from %03d" % program[ic + 2] : "")

      puts "%03d: %s,%d,%d,%d - multiply %s * %s, store %05d in %03d" % [ic, field, program[ic + 1], program[ic + 2], program[ic + 3], desc[0], desc[1], result, params[2]]
      
      program[params[2]] = result
      ic += 4
      
    when "03"
      params[0] = program[ic + 1]

      puts "%03d: %s,%d - store input %d in %03d" % [ic, field, program[ic + 1], acc, params[0]]
      
      program[params[0]] = acc
      ic += 2
      
    when "04"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      acc = params[0]

      desc[0] = "value #{params[0]}" + (mode[0] == "0" ? " from %03d" % program[ic + 1] : "")

      puts "%03d: %s,%d - output %d from %s" % [ic, field, program[ic + 1], acc, desc[0]]
      
      puts ">>>> %d <<<<" % acc 
      ic += 2
      
    when "05"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]

      desc[0] = "value #{params[0]}" + (mode[0] == "0" ? " from %03d" % program[ic + 1] : "")
      desc[1] = "value #{params[1]}" + (mode[1] == "0" ? " from %03d" % program[ic + 2] : "")

      puts "%03d: %s,%d,%d - jump if %s true to %s" % [ic, field, program[ic + 1], program[ic + 2], desc[0], desc[1]]
      
      if params[0] != 0 
        ic = params[1]
      else
        ic += 3
      end
      
    when "06"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]

      desc[0] = "value #{params[0]}" + (mode[0] == "0" ? " from %03d" % program[ic + 1] : "")
      desc[1] = "value #{params[1]}" + (mode[1] == "0" ? " from %03d" % program[ic + 2] : "")

      puts "%03d: %s,%d,%d - jump if %s false to %s" % [ic, field, program[ic + 1], program[ic + 2], desc[0], desc[1]]
      
      if params[0] == 0 
        ic = params[1]
      else
        ic += 3
      end
      
    when "07"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      result = params[0] < params[1] ? 1 : 0
      
      desc[0] = "value #{params[0]}" + (mode[0] == "0" ? " from %03d" % program[ic + 1] : "")
      desc[1] = "value #{params[1]}" + (mode[1] == "0" ? " from %03d" % program[ic + 2] : "")

      puts "%03d: %s,%d,%d,%d - store result %b of %s < %s in %03d" % [ic, field, program[ic + 1], program[ic + 2], program[ic + 3], result, desc[0], desc[1], params[2]]
      
      program[params[2]] = result
      ic += 4
      
    when "08"
      params[0] = mode[0] == "0" ? program[program[ic + 1]] : program[ic + 1]
      params[1] = mode[1] == "0" ? program[program[ic + 2]] : program[ic + 2]
      params[2] = program[ic + 3]
      result = params[0] == params[1] ? 1 : 0
      
      desc[0] = "value #{params[0]}" + (mode[0] == "0" ? " from %03d" % program[ic + 1] : "")
      desc[1] = "value #{params[1]}" + (mode[1] == "0" ? " from %03d" % program[ic + 2] : "")

      puts "%03d: %s,%d,%d,%d - store result %b of %s == %s in %03d" % [ic, field, program[ic + 1], program[ic + 2], program[ic + 3], result, desc[0], desc[1], params[2]]
      
      program[params[2]] = result
      ic += 4
      
    end  
  end
  
  acc
end

result = execute(program, 5)

puts "program output: #{result}"

result # => 9436229


# >> 000: 00003,225 - store input 5 in 225
# >> 002: 00001,225,6,6 - add value 5 from 225 + value 1100 from 006, store 01105 in 006
# >> 006: 01105,1,238 - jump if value 1 true to value 238
# >> 238: 01105,0,99999 - jump if value 0 true to value 99999
# >> 241: 01105,227,247 - jump if value 227 true to value 247
# >> 247: 01005,227,99999 - jump if value 0 from 227 true to value 99999
# >> 250: 01005,0,256 - jump if value 3 from 000 true to value 256
# >> 256: 01106,227,99999 - jump if value 227 false to value 99999
# >> 259: 01106,0,265 - jump if value 0 false to value 265
# >> 265: 01006,0,99999 - jump if value 3 from 000 false to value 99999
# >> 268: 01006,227,274 - jump if value 0 from 227 false to value 274
# >> 274: 01105,1,280 - jump if value 1 true to value 280
# >> 280: 00001,225,225,225 - add value 5 from 225 + value 5 from 225, store 00010 in 225
# >> 284: 01101,294,0,0 - add value 294 + value 0, store 00294 in 000
# >> 288: 00105,1,0 - jump if value 1 true to value 294 from 000
# >> 294: 01106,0,300 - jump if value 0 false to value 300
# >> 300: 00001,225,225,225 - add value 10 from 225 + value 10 from 225, store 00020 in 225
# >> 304: 01101,314,0,0 - add value 314 + value 0, store 00314 in 000
# >> 308: 00106,0,0 - jump if value 0 false to value 314 from 000
# >> 314: 00108,677,226,224 - store result 1 of value 677 == value 677 from 226 in 224
# >> 318: 00102,2,223,223 - multiply value 2 * value 0 from 223, store 00000 in 223
# >> 322: 01006,224,329 - jump if value 1 from 224 false to value 329
# >> 325: 01001,223,1,223 - add value 0 from 223 + value 1, store 00001 in 223
# >> 329: 01108,226,677,224 - store result 0 of value 226 == value 677 in 224
# >> 333: 01002,223,2,223 - multiply value 1 from 223 * value 2, store 00002 in 223
# >> 337: 01006,224,344 - jump if value 0 from 224 false to value 344
# >> 344: 00007,226,677,224 - store result 0 of value 677 from 226 < value 226 from 677 in 224
# >> 348: 00102,2,223,223 - multiply value 2 * value 2 from 223, store 00004 in 223
# >> 352: 01006,224,359 - jump if value 0 from 224 false to value 359
# >> 359: 01007,226,677,224 - store result 0 of value 677 from 226 < value 677 in 224
# >> 363: 01002,223,2,223 - multiply value 4 from 223 * value 2, store 00008 in 223
# >> 367: 01006,224,374 - jump if value 0 from 224 false to value 374
# >> 374: 01108,677,226,224 - store result 0 of value 677 == value 226 in 224
# >> 378: 00102,2,223,223 - multiply value 2 * value 8 from 223, store 00016 in 223
# >> 382: 01005,224,389 - jump if value 0 from 224 true to value 389
# >> 385: 01001,223,1,223 - add value 16 from 223 + value 1, store 00017 in 223
# >> 389: 00107,226,226,224 - store result 1 of value 226 < value 677 from 226 in 224
# >> 393: 00102,2,223,223 - multiply value 2 * value 17 from 223, store 00034 in 223
# >> 397: 01006,224,404 - jump if value 1 from 224 false to value 404
# >> 400: 00101,1,223,223 - add value 1 + value 34 from 223, store 00035 in 223
# >> 404: 01107,226,226,224 - store result 0 of value 226 < value 226 in 224
# >> 408: 01002,223,2,223 - multiply value 35 from 223 * value 2, store 00070 in 223
# >> 412: 01005,224,419 - jump if value 0 from 224 true to value 419
# >> 415: 01001,223,1,223 - add value 70 from 223 + value 1, store 00071 in 223
# >> 419: 01007,677,677,224 - store result 1 of value 226 from 677 < value 677 in 224
# >> 423: 00102,2,223,223 - multiply value 2 * value 71 from 223, store 00142 in 223
# >> 427: 01006,224,434 - jump if value 1 from 224 false to value 434
# >> 430: 00101,1,223,223 - add value 1 + value 142 from 223, store 00143 in 223
# >> 434: 01107,226,677,224 - store result 1 of value 226 < value 677 in 224
# >> 438: 01002,223,2,223 - multiply value 143 from 223 * value 2, store 00286 in 223
# >> 442: 01006,224,449 - jump if value 1 from 224 false to value 449
# >> 445: 00101,1,223,223 - add value 1 + value 286 from 223, store 00287 in 223
# >> 449: 00107,677,677,224 - store result 0 of value 677 < value 226 from 677 in 224
# >> 453: 00102,2,223,223 - multiply value 2 * value 287 from 223, store 00574 in 223
# >> 457: 01005,224,464 - jump if value 0 from 224 true to value 464
# >> 460: 01001,223,1,223 - add value 574 from 223 + value 1, store 00575 in 223
# >> 464: 01008,226,226,224 - store result 0 of value 677 from 226 == value 226 in 224
# >> 468: 01002,223,2,223 - multiply value 575 from 223 * value 2, store 01150 in 223
# >> 472: 01005,224,479 - jump if value 0 from 224 true to value 479
# >> 475: 00101,1,223,223 - add value 1 + value 1150 from 223, store 01151 in 223
# >> 479: 01007,226,226,224 - store result 0 of value 677 from 226 < value 226 in 224
# >> 483: 00102,2,223,223 - multiply value 2 * value 1151 from 223, store 02302 in 223
# >> 487: 01005,224,494 - jump if value 0 from 224 true to value 494
# >> 490: 01001,223,1,223 - add value 2302 from 223 + value 1, store 02303 in 223
# >> 494: 00008,677,226,224 - store result 0 of value 226 from 677 == value 677 from 226 in 224
# >> 498: 01002,223,2,223 - multiply value 2303 from 223 * value 2, store 04606 in 223
# >> 502: 01005,224,509 - jump if value 0 from 224 true to value 509
# >> 505: 01001,223,1,223 - add value 4606 from 223 + value 1, store 04607 in 223
# >> 509: 00108,677,677,224 - store result 0 of value 677 == value 226 from 677 in 224
# >> 513: 01002,223,2,223 - multiply value 4607 from 223 * value 2, store 09214 in 223
# >> 517: 01005,224,524 - jump if value 0 from 224 true to value 524
# >> 520: 01001,223,1,223 - add value 9214 from 223 + value 1, store 09215 in 223
# >> 524: 01008,677,677,224 - store result 0 of value 226 from 677 == value 677 in 224
# >> 528: 00102,2,223,223 - multiply value 2 * value 9215 from 223, store 18430 in 223
# >> 532: 01006,224,539 - jump if value 0 from 224 false to value 539
# >> 539: 00007,677,226,224 - store result 1 of value 226 from 677 < value 677 from 226 in 224
# >> 543: 01002,223,2,223 - multiply value 18430 from 223 * value 2, store 36860 in 223
# >> 547: 01005,224,554 - jump if value 1 from 224 true to value 554
# >> 554: 01108,226,226,224 - store result 1 of value 226 == value 226 in 224
# >> 558: 01002,223,2,223 - multiply value 36860 from 223 * value 2, store 73720 in 223
# >> 562: 01005,224,569 - jump if value 1 from 224 true to value 569
# >> 569: 00107,677,226,224 - store result 0 of value 677 < value 677 from 226 in 224
# >> 573: 00102,2,223,223 - multiply value 2 * value 73720 from 223, store 147440 in 223
# >> 577: 01005,224,584 - jump if value 0 from 224 true to value 584
# >> 580: 00101,1,223,223 - add value 1 + value 147440 from 223, store 147441 in 223
# >> 584: 00008,226,226,224 - store result 1 of value 677 from 226 == value 677 from 226 in 224
# >> 588: 01002,223,2,223 - multiply value 147441 from 223 * value 2, store 294882 in 223
# >> 592: 01005,224,599 - jump if value 1 from 224 true to value 599
# >> 599: 00108,226,226,224 - store result 0 of value 226 == value 677 from 226 in 224
# >> 603: 01002,223,2,223 - multiply value 294882 from 223 * value 2, store 589764 in 223
# >> 607: 01006,224,614 - jump if value 0 from 224 false to value 614
# >> 614: 00007,226,226,224 - store result 0 of value 677 from 226 < value 677 from 226 in 224
# >> 618: 00102,2,223,223 - multiply value 2 * value 589764 from 223, store 1179528 in 223
# >> 622: 01006,224,629 - jump if value 0 from 224 false to value 629
# >> 629: 01107,677,226,224 - store result 0 of value 677 < value 226 in 224
# >> 633: 00102,2,223,223 - multiply value 2 * value 1179528 from 223, store 2359056 in 223
# >> 637: 01005,224,644 - jump if value 0 from 224 true to value 644
# >> 640: 00101,1,223,223 - add value 1 + value 2359056 from 223, store 2359057 in 223
# >> 644: 00008,226,677,224 - store result 0 of value 677 from 226 == value 226 from 677 in 224
# >> 648: 00102,2,223,223 - multiply value 2 * value 2359057 from 223, store 4718114 in 223
# >> 652: 01006,224,659 - jump if value 0 from 224 false to value 659
# >> 659: 01008,226,677,224 - store result 1 of value 677 from 226 == value 677 in 224
# >> 663: 01002,223,2,223 - multiply value 4718114 from 223 * value 2, store 9436228 in 223
# >> 667: 01006,224,674 - jump if value 1 from 224 false to value 674
# >> 670: 01001,223,1,223 - add value 9436228 from 223 + value 1, store 9436229 in 223
# >> 674: 00004,223 - output 9436229 from value 9436229 from 223
# >> >>>> 9436229 <<<<
# >> program output: 9436229
