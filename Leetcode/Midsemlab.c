#include<stdio.h>
#include<stdlib.h>
#include<string.h>

int n;
typedef struct phoneContact{
    long phonenum;
    char str[20];

}pc;
 
void Create(pc *s){
    for(int i=0;i<n;i++){
        printf("Enter name: ");
        scanf("%s",(s+i)->str);
        printf("Enter ph no: ");
        scanf("%ld",&(s+i)->phonenum);
    }
}
long Findcontact(char *names,pc *ptr){
    for(int i=0;i<n;i++){
        if(strcmp((ptr+i)->str,names)==0){
            
            printf("Ph no: %ld\n",(ptr+i)->phonenum);
            return 1;
        }
    }
    return 0;
}
int main(){
    char strng[20];
    printf("Enter the number of people: ");
    scanf("%d",&n);
    pc *structure=(pc *)malloc(n*sizeof(pc));
    Create(structure);
    
    printf("Contact details:\n");
    for(int i=0;i<n;i++){
        printf("Name: %s\n",(structure+i)->str);
        printf("Ph no: %ld\n",(structure+i)->phonenum);
    }
    printf("Enter name to search: ");
    scanf("%s",strng);
    if (Findcontact(strng,structure)==0){
        printf("Not found\n Enter Ph no: ");
        scanf("%ld",&(structure+n)->phonenum);
        strcpy((structure+n)->str,strng);
        n++;
    }
    printf("Contact details:\n");
    for(int i=0;i<n;i++){
        printf("Name: %s\n",(structure+i)->str);
        printf("Ph no: %ld\n",(structure+i)->phonenum);
    }
  
    free(structure);
    return 0;
}