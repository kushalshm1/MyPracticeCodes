#include<stdio.h>
#include<conio.h>
#include<math.h>
int main()
{ 
    int a,b,c,d,e;
    clrscr();
    printf("type the value of A,B,C of Quardatic Equation AX^2+BX+C\n");
    printf("A=");
    scanf("%d",&a);
    printf("B=");
    scanf("%d",&b);
    printf("C=");
    scanf("%d",&c);
    d=(b*b)-(4*a*c));
    // if(d<0){
    //     d = (-1)*d
    // }
    // else{
    //     d = d
    // }
    d=sqrt(`d);
    if(d<0)
    {
        printf("Roots are Imagenary");
    }
    if(d==0)
    {
        e=-b/(2*a);
        printf("%d is the Root of equation");
    }
    if(d>0)
    {
        e=(-b+d)/(2*a);
        printf("%d,",e);
        e=(-b-d)/(2*a);
        printf("%d,",e);
}
getch();
return 0;
}
