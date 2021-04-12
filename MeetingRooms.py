'''
Given an array of meeting start and end times, determine if any meetings overlap
input: [[0,30], [5, 10], [15, 20]] 
ouput: False
'''
# 1). Sort by start of each meeting
# 2). compare each meeting start time with previous meeting end time to check for overlap
#    (startTime >= endTime = no overlap)
# 3). Stop at end of array

if not intervals or len(intervals) <= 1:  # edge case where there are no meetings or onely one meeting
  return True                             # return true as its impossible for overlap. you need at least 2 meetings for overlap. 

intervals.sort(key = lambda x: x[0])  # sort by the start (x[0]) of each meeting

for i in range(1,len(intervals)): # iterate from 1 as we dont want to compare start of first meeting
  if intervals[i][0] <= intervals[i-1][1]:  # if the start of this meeting is less then or equal to end of previous meeting
    return True                             # then there was no overlap between the meetings
  else:
    return False
  
# This solution has a run time of sort() multiplied by the length of mettings:
# run time = sort * length og meetings
# run time = O(logn) * O(n)
# run time = O(nlogn)

# This solution has a space complexity of o(1) as it has no storing of values
