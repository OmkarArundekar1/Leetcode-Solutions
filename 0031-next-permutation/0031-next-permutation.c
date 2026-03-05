void nextPermutation(int* nums, int numsSize) {
    int p1=0,p2=0,flag=0;
    for(int i=numsSize-2;i>=0;i--){
        if(nums[i]<nums[i+1]){
            p1=i;
            flag=1;
            break;
        }
    }
    if(flag==0){
        int i=0,lp=numsSize-1;
        while(lp>i){
            int temp=nums[i];
            nums[i]=nums[lp];
            nums[lp]=temp;
            i++;lp--;
        }
        return;
    }
    int tarele=nums[p1];
    for(int i=numsSize-1;i>=0;i--){
        if(nums[i]>tarele){
            p2=i;
            break;
        }
    }

    nums[p1]=nums[p2];
    nums[p2]=tarele;

    p1+=1;
    int lastp=numsSize-1;
    while(p1<lastp){
        tarele = nums[p1];
        nums[p1]=nums[lastp];
        nums[lastp]=tarele;
        p1++;lastp--;
    }
}