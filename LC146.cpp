//o(1) 复杂度，需要用map来登记key和vector的关系
class LRUCache {
private:
    vector<pair<int, int>> data;
    int capacity;
    unordered_map<int, vector<pair<int, int>>::iterator> m;
public:
    LRUCache(int capacity) {
        this->capacity = capacity;
    }
    
    int get(int key) {
        bool flag_found = false;
        int res;
        
        auto it=m.find(key);
        if(it==m.end()) return -1;

        res = (*it).second->second;
        auto temp_val = (*it).second->second;
        this->data.erase(it->second); //deque
        // this->data.push_back(temp_val); //inque
        
        return res;
                
    }
    
    void put(int key, int value) {
        auto it=m.find(key);
        if(it==m.end()){
            this->data.push_back({key,value}); //inque
            // m[key] = data.rbegin();
        }else{
            // this->data.erase(it);
            this->data.push_back({key,value}); //inque
            // this->m[key]=this->data.rbegin();
        }    
        if(this->data.size()>=this->capacity){
          this->data.erase(data.begin());  
        } 
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */