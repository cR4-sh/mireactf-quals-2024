#include <stdio.h>
#include <stdlib.h>

void setup()
{
    setvbuf(stdout, (char *)NULL, _IONBF, 0); 
    setvbuf(stderr, (char *)NULL, _IONBF, 0); 
}

int main()
{
    int debug = 0;
    char name[16];

    setup();
    printf("Enter your name: ");
    gets(name);

    if (debug)
    {
        printf("Debug flag: %s\n", getenv("FLAG"));
    }
    printf("Hello, %s!", name);
}