#include <stdio.h>

int main(){
    float a,b;
    char c;

    printf("\n 1) Addition - a \n 2)Subtraction - s \n 3)Multiplication - m \n 4)Division - d \n");
    printf("\n Enter your choice: ");
    scanf("%c",&c);

    printf("\n Enter two numbers a and b: ");
    scanf("%f %f",&a,&b);

    switch (c)
    {
    case 'a':{
        printf("Addition = %f", a+b);
        break;}
    case 's':{
        printf("Subtraction = %f", a-b);
        break;}
    case 'm':{
        printf("Multiplication = %f", a*b);
        break;}
    case 'd':{
        printf("Division = %f", a/b);
        break;}
    default:{
        printf("Enter a valid choice");
        break;}
    }
}