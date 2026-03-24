pairs:list[list[int,int]]=[[4],[1,3],[4,2],[3,1],[2,4]]

length=pairs.pop(0)[0]
# print
print(length)
# print(len(pairs))
result=[]
for i in range(4):
    for j in range(4):
      if(pairs[i][0]==pairs[j][1] and len(result)<length):
         result.append(pairs[i])
         result.append(pairs[j])
print(result)
# /////////////////////////////////////////////////////////////////////////////////////////////////////

pairs = [[4], [1, 3], [4, 2], [3, 1], [2, 4]]

# Extract length target
target_length = pairs.pop(0)[0]

# 1. Pre-process: Group pairs by their 2nd element for fast lookup
# We want to find a partner B where B[1] == A[0]
candidates_by_second = {}
for p in pairs:
    sec_val = p[1]
    if sec_val not in candidates_by_second:
        candidates_by_second[sec_val] = []
    candidates_by_second[sec_val].append(p)
print(candidates_by_second)
result = []

# 2. Iterate through pairs (acting as the "1st pair")
for first_pair in pairs:
    # Stop if we reached the target length
    if len(result) >= target_length:
        break
    
    match_val = first_pair[0] # This must match the 2nd element of the other pair
    
    # Check if we have any candidates with this 2nd element
    if match_val in candidates_by_second:
        for second_pair in candidates_by_second[match_val]:
            # Optional: Ensure we don't match a pair with itself if [1,1] existed
            if first_pair is not second_pair: 
                result.append(first_pair)
                result.append(second_pair)
                
                # Check length constraint inside the inner loop too
                if len(result) >= target_length:
                    break
        
print(result)
#////////////////////////////////////////////////////////////////////////////////////////////////


# target_lenght=pairs.pop(0)[0]

# candidated_by_second={}

# for p in pairs:
#     secound_element=p[1]
#     if secound_element not in candidated_by_second:
#         candidated_by_second[secound_element]=[]
#     candidated_by_second[secound_element].append(p)
# print(candidated_by_second)
# print(candidated_by_second[4][0])

# result=[]

# for p in pairs:
#     length=len(result)
#     first_element=p[0]

#     if length==target_lenght:
#          break
#     if first_element in candidated_by_second:
#         for second_pair in candidated_by_second[first_element]:
#             if p is not second_pair:
                        
#                 result.append(p)
#                 result.append(second_pair)

# print(result)