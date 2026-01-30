def buildArray(target, n):
    result = []
    current_target_index = 0  # Points to the number in 'target' we are looking for
    
    # Loop through the stream numbers starting from 1
    for stream_num in range(1, n + 1):
        
        # 1. We ALWAYS pick up the number coming from the stream
        result.append("Push")
        
        # 2. Check if this is the number we want
        if stream_num == target[current_target_index]:
            # It IS the number we want! 
            # Move to the next number in our target list
            current_target_index += 1
        else:
            # It is NOT the number we want.
            # We just picked it up ("Push"), so we must immediately throw it away ("Pop")
            result.append("Pop")
            
        # STOP CONDITION: If we have found all numbers in target, stop immediately.
        if current_target_index == len(target):
            break
            
    return result
