//明天的价格比今天高就明天卖出，明天的价格比今天低，就今天卖出，明天买进。
//https://blog.csdn.net/camellhf/article/details/52704719
//zz:每天都买入，如果涨了就卖，跌了就不卖
class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res=0;
        for(int i=0;i<prices.size()-1; i++){
            if(prices[i]<prices[i+1]){
                res+=prices[i+1]-prices[i];
            }
        }
        return res;
    }
};