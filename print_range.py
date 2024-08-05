# print_increamental_range prints the given inputs as it is,
# except for increamental ranges, which are printed as start-end
def print_increamental_range(input_val):
    if not input_val:
        return ""
    
    start, end = input_val[0], input_val[0]
    output = []
    
    for i in range(1, len(input_val)):
        # Check if the next number is consecutive incremental
        if input_val[i] == end + 1:
            end = input_val[i]
        else:
            # if the start value is same as end, no range
            if start == end:
                output.append(f"{start}")
            # if there is only single consecutive increament, no range
            elif end == start + 1:
                output.append(f"{start}")
                output.append(f"{end}")
            else:
                output.append(f"{start}-{end}")
            start = input_val[i]
            end = input_val[i]
    
    # Add the last range into the output
    if start == end:
        output.append(f"{start}")
    elif end == start + 1:
        output.append(f"{start}")
        output.append(f"{end}")
    else:
        output.append(f"{start}-{end}")
    
    return ",".join(output)

# input data
input_val = [1,2,5,6,7,10,11,15,16,17,18,20]
result = print_increamental_range(input_val)
print(result)


