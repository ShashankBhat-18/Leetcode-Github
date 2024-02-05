#include<stdio.h>
#include<stdlib.h>
int findDuplicate(int* nums, int numsSize){

    for(int i=0;i<numsSize;i++){
        int num=*(nums+i);
            for(int j=i+1;j<numsSize;j++){
                if (*(nums+j)==num){
                    printf("%d\n",num);
                    return 0;
                }
            }
        
    }
}
int main(){
    int nums[]={1,3,4,2,2};
    int numsSize=sizeof(nums)/sizeof(nums[0]);
    if (findDuplicate(nums,numsSize)!=0){
        printf("No duplicates");
    }
    return 1;
}