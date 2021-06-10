//那么对于该部分指令的要求是，机器人回到了原点或者不再原点且不面向北
//https://blog.csdn.net/fuxuemingzhu/article/details/92128721
class Solution {
public:
    bool isRobotBounded(string instructions) {
        char cur_facing='f'; // f:front, b:back, l:left, r:right
        pair<int,int> cur_pos={0,0}; //(x,y)
        for(int i=0;i<instructions.size();i++){
            if(instructions[i] == 'G') move(cur_pos, cur_facing);
            else turn(cur_facing, instructions[i]);
        }
        if(cur_pos==make_pair(0,0)) return true;
        if(cur_facing != 'f') return true;
        return false;
    }
    
    void move(pair<int,int>& cur_pos, char cur_facing){
        if(cur_facing == 'f'){
            cur_pos.second++;
        }else if(cur_facing == 'l') {
            cur_pos.first--;
        }else if(cur_facing == 'r') {
            cur_pos.first++;
        }else if(cur_facing == 'b') {
            cur_pos.second--;
        }
    }
    
    void turn(char& cur_facing, char tur){
        if(cur_facing == 'f'){
            if(tur=='L') cur_facing = 'l';
            if(tur=='R') cur_facing = 'r';
        }else if(cur_facing == 'l') {
            if(tur=='L') cur_facing = 'b';
            if(tur=='R') cur_facing = 'f';
        }else if(cur_facing == 'r') {
            if(tur=='L') cur_facing = 'f';
            if(tur=='R') cur_facing = 'b';
        }else if(cur_facing == 'b') {
            if(tur=='L') cur_facing = 'r';
            if(tur=='R') cur_facing = 'l';
        }
    }
};