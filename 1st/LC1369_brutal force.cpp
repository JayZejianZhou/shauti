class UndergroundSystem {
private:
    //database, station id--station(intime),station(outtime), 用vector和pair而不用map是因为我需要记录时间顺序,先进来的是入栈，后进来的时间是出站
    unordered_map<int, vector<pair<string, int>>> database;
public:
    UndergroundSystem() {
        
    }
    
    void checkIn(int id, string stationName, int t) {
        database[id].push_back({stationName+"in", t});
    }
    
    void checkOut(int id, string stationName, int t) {
        database[id].push_back({stationName+"out", t});
    }
    
    double getAverageTime(string startStation, string endStation) {
        double sum_time=0; double sum_num=0;
        for(auto itc:database){
            for(int i=0;i<itc.second.size()-1;i++){
                if((itc.second)[i].first==(startStation+"in") && (itc.second)[i+1].first==(endStation+"out")){
                    sum_time += (itc.second)[i+1].second - (itc.second)[i].second;
                    sum_num ++;
                }
            }
        }
        if(sum_num==0) return 0;
        return sum_time/sum_num;
    }
};

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem* obj = new UndergroundSystem();
 * obj->checkIn(id,stationName,t);
 * obj->checkOut(id,stationName,t);
 * double param_3 = obj->getAverageTime(startStation,endStation);
 */