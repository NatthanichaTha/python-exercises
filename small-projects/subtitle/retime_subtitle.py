import sys
filepath = sys.argv[1]
offset_s = float(sys.argv[2])
file = open(filepath, "r")
file_content = file.readlines()

def parse_srt_blocks(file_content):
    subtitle_block = []
    block = []
    for line in file_content:
        if line != "\n":
            line = line.replace("\n", "")
            block.append(line)
        else:
            subtitle_block.append(block)
            block = []
    return subtitle_block

def timestring_to_sec(timestring):
    timestring = timestring.split(":")
    hour_to_sec = int(timestring[0]) * 3600
    minute_to_sec = int(timestring[1]) * 60
    second = int(timestring[2][:2])
    ms_to_sec = int(timestring[2][3:]) / 1000
    return hour_to_sec + minute_to_sec + second + ms_to_sec

def sec_to_timestring(sec: int):
    sec_to_hour = int(sec/3600) 
    sec = sec % 3600
    sec_to_min = int(sec/60)
    sec = sec % 60
    sec_to_sec = int(sec/1)
    sec = int((sec - sec_to_sec)*1000)
    
    timestring = str(sec_to_hour).zfill(2) + ":" + str(sec_to_min).zfill(2) + ":" + str(sec_to_sec).zfill(2) + "," + str(sec)[:3].zfill(3) 
    return timestring

def add_sec(timestring, sec):
    modified_sec = timestring_to_sec(timestring) + sec
    modified_timestring = sec_to_timestring(modified_sec)
    return modified_timestring

def retime_blocks(srt_blocks, offset_s):
    retimed_blocks = []
    for block in srt_blocks:
        block_timing = block[1].split(" --> ")
        block_start_time = block_timing[0]
        block_end_time = block_timing[1]
        modified_block_start_time = add_sec(block_start_time, offset_s)
        modified_block_end_time = add_sec(block_end_time, offset_s)
        modified_block_timing = modified_block_start_time + " --> " + modified_block_end_time
        retimed_blocks.append([block[0], modified_block_timing, "\n".join(block[2:])])
    return retimed_blocks

def write_srt_block(blocks, filepath):
    newfile = open(filepath[:-4] + ".retimed.srt", "w")
    for block in blocks:
        for line in block:
            newfile.write(line+"\n")
        newfile.write("\n") 

parsed_blocks = parse_srt_blocks(file_content)
retimed_blocks = retime_blocks(parsed_blocks, offset_s)

write_srt_block(retimed_blocks, filepath)

print(timestring_to_sec("00:00:00,000"))
print(sec_to_timestring(0.0))