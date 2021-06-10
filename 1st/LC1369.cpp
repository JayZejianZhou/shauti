class UndergroundSystem {
private:
    unordered_map<string, unordered_map<string, vector<float>>> duration;
    unordered_map<int, pair<string, int>> database;
    unordered_map<string, unordered_map<string, vector<int>>> times;
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        database[id].first = stationName;
        database[id].second = t;
    }
    
    void checkOut(int id, string stationName, int t) {
        double temp_duration = t-database[id].second;    
        duration[database[id].first][stationName].push_back(temp_duration);       
        times[database[id].first][stationName].push_back(1);  
    }
    
    double getAverageTime(string startStation, string endStation) {
        double sum=0;
        for(auto itc:duration[startStation][endStation]) sum+=itc;
        return sum/times[startStation][endStation].size();
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */