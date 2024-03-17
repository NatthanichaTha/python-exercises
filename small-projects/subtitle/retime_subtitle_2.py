import sys
filepath = sys.argv[1]
offset_s = sys.argv[2]

def parse_content(filepath):
    file = open(filepath, "r")
    content = file.readlines()
    parsed_content = []
    block = []
    for line in content:
        if line == "\n":
            parsed_content.append(block)
            block = []
        else:
            block.append(line.replace("\n", ""))

    return parsed_content

def time_in_sec(timestring):
    timestring = timestring.split(":")
    hour = int(timestring[0])
    minute = int(timestring[1])
    second = int(timestring[2][0:2])
    ms = int(timestring[2][3:])
    time_in_sec = hour*3600 + minute*60 + second*1 + ms/1000

    return time_in_sec

def sec_to_timestring(time_in_sec):
    hour = int(time_in_sec / 3600)
    time_in_sec = time_in_sec % 3600
    minute = int(time_in_sec / 60)
    time_in_sec = time_in_sec % 60
    second = int(time_in_sec / 1)
    time_in_sec = time_in_sec % 1
    ms = int(time_in_sec * 1000)
    new_timestring = str(hour).zfill(2) + ":" + str(minute).zfill(2) + ":" + str(second).zfill(2) + "," + str(ms).zfill(3)
    return new_timestring

def add_sec(timestring, offset_s):
    time_sec = time_in_sec(timestring)
    retimed_time_in_sec = time_sec + float(offset_s)
    retimed_timestring = sec_to_timestring(retimed_time_in_sec)
    return retimed_timestring

def retime(parsed_content, offset_s):
    retimed_content = []
    for block in parsed_content:
        new_block = block
        timestring = new_block[1].split(" --> ")
        start_timestring = add_sec(timestring[0], offset_s)
        end_timestring = add_sec(timestring[1], offset_s)
        new_block[1] = start_timestring + " --> " + end_timestring
        retimed_content.append(block)
    return retimed_content

parsed_content = parse_content(filepath)
retimed_content = retime(parsed_content, offset_s)

newfile = open(filepath.replace(".srt", ".retimed.srt"), "w")
for block in retimed_content:
    newfile.write("\n".join(block) + "\n")
    newfile.write("\n")

