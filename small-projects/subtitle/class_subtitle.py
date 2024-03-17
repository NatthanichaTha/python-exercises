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

class SubtitleBlock:
    def __init__(self, block_info: list[str]):
        self.id = int(block_info[0].replace("\n", ""))
        self.text = "".join(block_info[2:])
        block_time_info = block_info[1].replace("\n", "").split(" --> ")
        self.start_time = block_time_info[0]
        self.end_time = block_time_info[1]
    
    def __repr__(self):
        return str(self.id) + "\n" + self.start_time + " --> " + self.end_time + "\n" + self.text
    
    def retime(self, offset_s):
        self.start_time = sec_to_timestring(time_in_sec(self.start_time) + offset_s)
        self.end_time = sec_to_timestring(time_in_sec(self.end_time) + offset_s)

class Subtitle:
    def __init__(self, path: str):
        self.path = path
        self.file = open(path, "r")
        self.blocks = self.parse_blocks()
    
    def __repr__(self):
        content = ""
        for block in self.blocks:
            content += str(block) + "\n"

        return content
    
    def parse_blocks(self):
        file_content = self.file.readlines()
        all_blocks = []
        block_info = []
        for line in file_content:
            if line != "\n":
                block_info.append(line)
            else:
                all_blocks.append(SubtitleBlock(block_info))
                block_info = []
        
        return all_blocks
    
    def retime_all(self, offset_s):
        for block in self.blocks:
            block.retime(offset_s)
    
    def to_file(self, path):
        newfile = open(path, "w")
        newfile.write(self.__repr__())

    def delete_block(self, id):
        for i, block in enumerate(self.blocks):
            if block.id == id:
                self.blocks.pop(i)

subtitle = Subtitle("../../Downloads/sub.srt")
subtitle.retime_all(3)
#subtitle.to_file("../../Downloads/sub.pipo.srt")
subtitle.delete_block(2)
subtitle.add_block("00:00:00,000", "00:00:01,000", "hello", 10)
