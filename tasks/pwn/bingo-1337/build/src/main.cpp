#include <stdio.h>
#include <stdlib.h>
#include <ctime>

#define NUMS_COUNT  16

char banner[] = R"(
   ____               _   _     ____    U  ___ u 
U | __")u    ___     | \ |"| U /"___|u   \/"_ \/ 
 \|  _ \/   |_"_|   <|  \| |>\| |  _ /   | | | | 
  | |_) |    | |    U| |\  |u | |_| |.-,_| |_| | 
  |____/   U/| |\u   |_| \_|   \____| \_)-\___/  
 _|| \\_.-,_|___|_,-.||   \\,-._)(|_       \\    
(__) (__)\_)-' '-(_/ (_")  (_/(__)__)     (__)   
    _   _____  _____   _____                     
   /"| |___"/u|___"/u |___ "|                    
 u | |uU_|_ \/U_|_ \/    / /                     
  \| |/ ___) | ___) | u// /\                     
   |_| |____/ |____/   /_/ U                     
 _//<,-,_// \\ _// \\ <<>>_                      
(__)(_/(__)(__|__)(__|__)__)                     
)";

void setup()
{
    setvbuf(stdout, (char *)NULL, _IONBF, 0); 
    setvbuf(stderr, (char *)NULL, _IONBF, 0); 
}

int main()
{
    setup();
    srand(time(0));
    puts(banner);

    u_int8_t input[NUMS_COUNT];

    printf("It's time to check your luck!\nEnter %d numbers: ", NUMS_COUNT);

    for (int i = 0; i < NUMS_COUNT; i++)
        scanf("%hhu", &input[i]);

    for (int i = 0; i < NUMS_COUNT; i++)
    {   
        if (input[i] != rand() % 256)
        {
            puts("not lucky...");
            exit(1);
        }
    }

    printf("BINGOO!!! I think you spent all of your luck...%s\n", getenv("FLAG"));
}