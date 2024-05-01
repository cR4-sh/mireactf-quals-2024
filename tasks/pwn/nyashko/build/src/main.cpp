#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char banner[] = R"(
                                                       .    
                      (.,,*,,***,**,,...,       ,,....,/    
    *,,,(.         *.,*****,,*,*..,,,*,.*.*,**,,,.,,,**     
     .,**%,,,,,*(..,.,,,,,,.,.*,,,,.,,,...,,,,,/,,.(.*/     
      ,****.**/*.,,,,,,*,,.,.,,,,,,,,,,,,.,...,,,*&   /     
      .*    .*,,,,,*,***,,,,.,,,,,/,,,,,,/,,,,,,,**%  (     
       .   (*,,,,,/,*,,**,,,/,,,,,,,,,,,**,,.,,.,.**#       
        / ./#,,*,/**,../*,*(*/,*,**((*,*/*/*(*,.,/*/%&.     
    .( *  (*,,,**#*(,.,##/*****,***//*/,*//***,.*,/#((#     
   (   ,//,(.*,/*#//.. .*(//***,(,**//(*////*/*,*.,(( .     
   /*/*  */#.*,////(.    /(,***//,##*/**.,//(/*,**(**  ,    
        //*/,,/,/*/(@@@@&#,(,*(//#./&&&&#%&,***,***,#  #    
        *(/(,,,//*%#@&@&&&. .,..,*. /,@@&&&*(*,**,(%*(*     
   .../ (,/#,,*/#/*#(#*&,*#         ,#./**.,(*//**/*/(      
    .  ,((%/,*,///**,,.##...  ..    ...*,,.###/(****%(*     
       ,/(((,#****/#.,....            ...*,.%*/*#/*,(/((    
       ,#*, .#*//**/%. .                  #/(((,/*..,/#*    
      /((*.*(./..*/*((*(               (/*#((*.//.,,,. /*   
     ///.(...,,*#.(///,..,/(&%.../@/&/(..,/#*/..,,,,,%..#.  
    / /#..,(,./../%(#//(%%. ......    #/#*((%*/ ../.,,. ((  
   /  //#       .,*.,,,,,*,          ,*,...,.%,(%. .   #/(  
   (  /##     #,.,.#...,,,/*...  .../**,,,../.*%(%,(.(#/(/  
  /  .,#((.(*****/&/*.,..,,,%,...../**,,..**.%//#***(//,*#  
  *  %*.(//,.,,****/*,*(*...,*/*///*,,,/**,..,//.,*****..( 
)";

void win()
{
    system("cat /app/flag.txt");
}

void read(char* buffer, int size)
{
    char c;
    int readen;

    while ((c = getchar()) != '\n' && c != EOF && size) 
    { 
        *(buffer++) = c;
        size--;
    }

    *buffer = 0;
}

void setup()
{
    setvbuf(stdout, (char *)NULL, _IONBF, 0); 
    setvbuf(stderr, (char *)NULL, _IONBF, 0); 
}

int main()
{
    setup();

    char password[16];
    char input[16];
    int len = 0;
    
    strcpy(password, getenv("PASSPHRASE"));

    puts(banner);
    puts("Are you a nyashko??? Lets check your nyasko passphrase!\n");
    printf("Enter your passphrase lentgh: ");
    scanf("%d", &len);

    char c;
    while ((c = getchar()) != '\n' && c != EOF) { }

    if (len > 15)
    {
        puts("Passphrase should be smaller!");
        exit(1);
    }
    
    printf("passphrase: ");
    read(input, len);

    if (strcmp(input, password))
    {
        puts("Hmmm, looks like youre not a nyashko >(>_<)<");
        exit(1);
    }

    puts("Nyaaaaa~~ Youre difinatly a nyashko!!!");
}