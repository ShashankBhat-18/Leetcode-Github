function gcd(str1,str2){
    if(str1.length==0 || str2.length==0){
        return "";
    }
    else if (str2.length==str2.length) {
        return str1===str2?str1:"";
    }
    const shorter=str1.length<str2.length?str1:str2;
    const longer=str1.length>str2.length?str1:str2;
    while(longer.startsWith(shorter)){
        longer=longer.substring(shorter.length);
    }
    return longer.length===0?shorter:"";
}