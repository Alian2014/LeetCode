#include <stdio.h>
#include "max.h"

int main()
{
    int a;
    int b;
    scanf("%d%d",&a,&b);
    int c = Max(a,b);
    printf("Hello World\n");
    printf("%d\n",c);
    return 0;
}