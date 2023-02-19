#include<stdio.h>
#include<time.h>

#define LEN 150


int sum =10000;


void deposit(){
    int money;
    printf("enter money =  : ");
    scanf("%d",&money);
    sum += money;
    printf("succesfully deposit !!\n");
    printf("total amt after deposit : %d",sum);
    

printf("\n");

}

void withdraw(){
    int wm;
    printf("enter withdraw money : ");
    scanf("%d",&wm);
    printf("succesfully withdraw !!\n");
    sum = sum-wm;
    printf("Ammount left = %d",sum);
    printf("\n");

}


void accountd(){
printf("total balance = %d",sum);

}


int main(){
// time

   char buf[LEN];
   time_t curtime;
   struct tm *loc_time;


    int k,acn,choice,sum = 10000;
    char name[99];
    printf("enter your name = ");
    scanf("%s",name);

    printf("enter account num : ");
    scanf("%d",&acn);


printf("\n**************************************************************\n");

printf("1.DEPOSIT MONEY\n");
printf("2.WITHDRAW MONEY\n");
printf("3.ACCOUNT DETAIL\n");
printf("4.TRANSFER MONEY\n");

printf("\n**************************************************************\n");

printf("enter your choice : ");
scanf("%d",&choice);

switch(choice){
    case 1:
    deposit();
    break;

        case 2:
    withdraw();
    break;

        case 3:
    accountd();
    break;
    
    //     case 4:
    // transfer();
    

}
printf("\n**************************************************************\n");
printf("\n");
 //Getting current time of system
   curtime = time (NULL);

   // Converting current time to local time
   loc_time = localtime (&curtime);

   // Displaying date and time in standard format
   printf("%s", asctime (loc_time));

   strftime (buf, LEN, "Today is  :  %A, %b %d.\n", loc_time);
   fputs (buf, stdout);
   strftime (buf, LEN, "Time is :  %I:%M %p.\n", loc_time);
   fputs (buf, stdout);

printf("\n**************************************************************\n");

}








