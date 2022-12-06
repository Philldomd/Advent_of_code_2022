# After reading up on enumeration in pyhton i found a new more clean solution

def fineTuneDataMarker(file_buffer, markerLength):
    for index, value in enumerate(file_buffer):
        if len(set(file_buffer[index-markerLength:index])) == markerLength:
            return index