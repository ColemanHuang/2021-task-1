#include <stdio.h>
int main(){
    int i=1;
    double j=0;
    long f;
    switch(i){ // if
        case 0:
            break;/* if else
             if else
             */
        case 1:
            break;
        case 2:
            break;
        default:
            break;
    }
    switch(i){
        case 0:
            break;
        case 1:
            break;
        default:
            break;
    }
    if(i<0){
        if(i<-1){}
        else{}
    }
    else if(i>0){
        if (i>2){}
        else if (i==2) {}
        else if (i>1) {}
        else {}
    }
    else{
        if(j!=0){}
        else{}
    }
    printf(" int double else ");
    return 0;
}
