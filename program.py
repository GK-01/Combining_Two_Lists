# Combining Two Lists Based on Overlap Conditions
import json

def combine_lists(list1, list2):

    def should_merge(element1, element2):
        pos1, pos2 = element1['positions'], element2['positions']
        overlap_start = max(pos1[0], pos2[0])
        overlap_end = min(pos1[1], pos2[1])
        overlap_length = max(0, overlap_end - overlap_start)
        
        if overlap_length!=0:
            length1 = pos1[1] - pos1[0]
            length2 = pos2[1] - pos2[0]
            
            if (overlap_length > length1 / 2) or (overlap_length > length2 / 2):
                return True
            return False
        return False

    combined_list = sorted(list1 + list2, key=lambda x: x['positions'][0])
    if not combined_list:
        return []
    merged_list = [combined_list[0]]
    
    for i in range(1, len(combined_list)):
        current_element = combined_list[i]
        last_merged_element = merged_list[-1]
        
        if should_merge(last_merged_element, current_element):
            last_merged_element['values'].extend(current_element['values'])
        else:
            merged_list.append(current_element)
    return merged_list

try:
    list1=input("Enter the first list in JSON format in a line: \n")
    list2=input("Enter the second list in JSON format in a line: \n")
    list1 = json.loads(list1)
    list2 = json.loads(list2)
    result = combine_lists(list1, list2)
    print("Combined List:")
    print(json.dumps(result, indent=4))
except json.JSONDecodeError:
    print("Invalid JSON input. Please ensure the input is in correct JSON format.")
except Exception as e:
    print(f"An error occurred: {e}")