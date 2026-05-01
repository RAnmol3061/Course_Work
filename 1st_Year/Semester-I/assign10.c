#include <stdio.h>

int main(){
    int i,n,fa;
    fa = 1;

    printf("Enter the number: ");
    scanf("%d",&n);

    for (i=1; i<= n; i++){
        fa = fa*i;
    }

    printf("Factorial of %d is %d", n,fa);
    return 0;
}