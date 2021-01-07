class RandomizedSet {
private:
    vector<int> dataset;
public:
    /** Initialize your data structure here. */
    RandomizedSet() {
        
    }
    
    /** Inserts a value to the set. Returns true if the set did not already contain the specified element. */
    bool insert(int val) {
        if(find(dataset.begin(), dataset.end(), val) == dataset.end()){
            dataset.push_back(val);
            return true;
        }else{
            return false;
        }
    }
    
    /** Removes a value from the set. Returns true if the set contained the specified element. */
    bool remove(int val) {
        auto it = find(dataset.begin(), dataset.end(), val);
        if(it == dataset.end()){
            return false;
        }else{
            dataset.erase(it);
            return true;
        }
    }
    
    /** Get a random element from the set. */
    int getRandom() {
        auto random_num = rand()%dataset.size() + 0;
        return dataset[random_num];
    }
};

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet* obj = new RandomizedSet();
 * bool param_1 = obj->insert(val);
 * bool param_2 = obj->remove(val);
 * int param_3 = obj->getRandom();
 */