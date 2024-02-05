function candiescheck(candies,extracandies){
    let result=[];
    let largest=Math.max(...candies);
    for(let i=0;i<candies.length;i++){
        if ((candies[i]+extracandies)>=largest) {
            result[i]=true;
        }else{
            result[i]=false;
        }
    }
    return result;
}
let can=[2,3,5,1,3];
var res=candiescheck(can,3);
console.log(res);