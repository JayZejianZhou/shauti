class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        if(intervals.size()==1) return 1;
        
        sort(intervals.begin(), intervals.end());
        int required_room = 1;
        
        vector<vector<int>> schedule;
        for(int i=0;i<intervals.size();i++){
            available_office(schedule, intervals[i]);
        }
        return schedule.size();
        
    }
    
    void available_office(vector<vector<int>>& schedule, vector<int>& time_frame){
        for(int i=0;i<schedule.size();i++){
            if(schedule[i][1] <= time_frame[0]){
                schedule[i] = time_frame;
                return;
            }
        }
        schedule.push_back(time_frame);
    }
};