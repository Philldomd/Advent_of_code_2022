def fineTuneDataMarker(file_buffer):
    start = 0
    end = 4
    while end <= len(file_buffer):
        if len(set(file_buffer[start:end])) == 4:
            return end
        else:
           start += 1 
           end += 1
         
def fineTuneDataMessage(file_buffer):
    start = 0
    end = 14
    while end <= len(file_buffer):
        if len(set(file_buffer[start:end])) == 14:
            return end
        else:
           start += 1 
           end += 1