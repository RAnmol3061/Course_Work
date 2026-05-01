#include <stdio.h>

void main() {
    int a,b,add,sub,mul,res,ch;
    float div;

    printf("Enter two numbers: ");
    scanf("%d %d", &a,&b);
    
    printf("\n 1)Addition \n 2)Subtraction \n 3)Multiplication \n 4)Division \n \n ");
    scanf("%d",&ch);

    if (ch == 1){
        add = a + b;
        printf("\n Addition = %d", add);
    } 

    if (ch == 2){
        sub = a - b;
        printf("\n Subtraction = %d", sub);
    }

    if (ch == 3){
        mul = a * b;
        printf("\n Multiplication = %d", mul);
    }

    if (ch == 4){
        div = a / b;
        printf("\n Division = %f", div);
    }
}