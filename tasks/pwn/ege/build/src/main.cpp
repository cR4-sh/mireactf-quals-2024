#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctime>

char banner[] = R"(
 ░▒▓██████▓▒░░▒▓████████▓▒░░▒▓████████▓▒░      ░▒▓████████▓▒░░▒▓██████▓▒░ ░▒▓████████▓▒░ 
░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░        
░▒▓█▓▒░         ░▒▓█▓▒░    ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░       ░▒▓█▓▒░        
░▒▓█▓▒░         ░▒▓█▓▒░    ░▒▓██████▓▒░        ░▒▓██████▓▒░ ░▒▓█▓▒▒▓███▓▒░░▒▓██████▓▒░   
░▒▓█▓▒░         ░▒▓█▓▒░    ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░        
░▒▓█▓▒░░▒▓█▓▒░  ░▒▓█▓▒░    ░▒▓█▓▒░             ░▒▓█▓▒░      ░▒▓█▓▒░░▒▓█▓▒░░▒▓█▓▒░        
 ░▒▓██████▓▒░   ░▒▓█▓▒░    ░▒▓█▓▒░             ░▒▓████████▓▒░░▒▓██████▓▒░ ░▒▓████████▓▒░                                                                                  
)";

char q1[] = R"(
1. Chto takoi ' or 1=1 --?
    1) idk man
    2) hmmmm... True?
    3) xor
    4) SQL Injection
)";

char q2[] = R"(
2. 1337 ^ 1337?
    1) 1337
    2) 0
    3) 7331
    4) 4342016897902897469403500760137597113653058229257224877226895823934931297349533928046501081099375077846021150809999456076255649899730959626201628661911635912097527563037559743102976878282131159171883056747396185822522966975108770297633407533288917996059356995808793672364850599452893873882234257588004348835555320495962971086870743496098967258919368639026811047589523889847842147880527762175968413860197731095288288390505166113847397307582934287774592155118056098770149996962559074131028298496129357925145205127546082212331941902122428849500258434092708097249750680371331273515723450469689630449392883552481591913920320640883588535179756510562591971860862264587897388894288629861134905777764058270000120090857076565884613454059385449304728858504538737326708704939508936232223539426005074284017890341411807929424812662643900874361280108730708015441088659718173055353020620203738681447845524609331298549626783310205380011829069276378767127553949908099673318960320865978190199649708528245466080579805639994525731824141995708331789014430908762107159816651969615716107365382585448360999385361032650126048907608479722632303332136397023483012143433014218714165155831700241464436382798315396944106897623012315242985035883381251061806321499981546281460330062876407080008566857771099186633695319398163529859647799852174671159790011625012959394992354050874800111465340357899231286003273719732580359377226569083437292616547352376444142700505187057826211895236662492275315305893994048719018899705585406636767202498872039834491536723257223646898000002797180044420921275525190156342515606114181061921864082613774086107824895079102245278599453237521583111647543587269415849231526394028800685695576421657428628546129507565447045946759034199537258248379568787990976678363797463720637672877342644437074649213165884808817657448972625015529769746912803848358747736123488757859456906419395011341270398586970310567105134547036336437182994572199773930531061371685578366688950077416083572783665778489248047106726922158465552895660557572383092712114568036270153728082997849505730296582953085027076375665022231307491861675325068048725037897397076738043116080294379574978282412364671368483774040833041830906799091523640107492467926776792107742490159611338477077023269875818769980349176319224999900305800712055945594080586151727743038849226025019543984003981235046396248461911796867343216665078802625272965992954991837295590728891304963524194749511605642180493628761069964292328551477009962313701896936989971764566572480982467464992791413927881693871956442227759588028368476324948285963162765587617922689517684368655487810949624958258381233878891648568361528942894471298840724621604604320521770260254359481455227150537712227342504764201009410210276281743972980259803482405535767480899757434940757902530530638796550634533573981496600491506683391936477105764012651450601256186101744164459762169401260404105129776743574177481873714796521037082885774682580213334405638996066724932708635361217587722509735052015107859126853612929436828235094219408816592956399893891366360062625868416066447747070232044680908655205238368097146580966861378383261936792268398291726613580783048815619322575265702821631577382746205198149544083977501538462186342872606539445063144785820965767094754924645997029253932101602590893463698245006165260239653863772275832045632389141729258971856248637295922027633043486557351952426192455031242560542366185969923039898542150092757978759647054130032388376165298665531817632047708627109250491653534295810730401020537593872537738501847847405725935942569946361583654711140480032492653644598576721905015645310593760036414246678082089295117567654071597823390940280430163021871086321652770177998615418478961669738197949011030062327721060337212526579469920432638157127422885146333042943961848001207038256763573985139345986911724137849671546144641634173515802220322700878375946519338749555087345729595272853314491711099390747716711091609239270963025549643149510487265577764947458468145914919629873095064915030602528258356355978194006047555596151225080630390272172792649050151832380363773151884092957101505736619951526406337588521903972167644666185251508075469127771210269096160109529020549687098341738617
)";

char q3[] = R"(
3. rev or web?
    1) rev
    2) rev
    3) rev
    4) rev
)";

char q4[] = R"(
4. Chto znachit CVE?
    1) Circus Versus Eggs 
    2) Common Vulnerabilities and Exposures
    3) Common Vanuchiy Exam (EGE)
    4) eto znachit uyazvimost
)";

char q5[] = R"(
5. sha256 ot 'ABOBA'?
    1) 98d44e13f455d916674d38424d39e1cb01b2a9132aacbb7b97a6f8bb7feb2544
    2) d89345478b298b5b713d678f90f6915b4c8a92eff45233a54e9fe0b47d1ee700
    3) Yes, please!
    4) ca49b7391d44b3e270c99a363825e5264fdfe0d8934c024d4491423b34095c10
)";

char q6[] = R"(
6. zip?
    1) PK
    2) MZ
    3) NO
    4) YES
)";

char q7[] = "\n7. Kakoi flag?\n\n>> ";

char* questions[] = {
    q1, q2, q3, q4, q5, q6, q7
};

int answers[] = {
    4, 2, 5, 2, 4, 1
};

void setup()
{
    setvbuf(stdout, (char *)NULL, _IONBF, 0); 
    setvbuf(stderr, (char *)NULL, _IONBF, 0); 
}

int main()
{   
    int ans;
    char buffer[48];
    volatile char flag[48];

    srand(time(0));
    setup();

    strcpy((char*)flag, getenv("FLAG"));

    puts(banner);

    for (int i = 0; i < 6; i++)
    {
        puts(questions[i]);
        printf(">> ");
        scanf("%d", &ans);

        if (ans != answers[i])
        {
            puts("Sorre, you didn't pass Ediniy Goverment Examen po CTF! Zdem tibya cherez god ;)");
            exit(1);
        }
    }

    printf(questions[6]);

    char c;
    while ((c = getchar()) != '\n' && c != EOF) { }

    fgets(buffer, sizeof(buffer), stdin);
    int len = strlen(buffer);
    if (len > 1)
        buffer[len-1] = 0;

    printf("\nNashi experti proveryaut vash razvernutiy otvet");

    for (int i = 0; i < 2 + rand() % 10; i++)
    {
        putc('.', stdout);
        sleep(1);
    }
    
    puts("\nVash otvet:");
    printf(buffer);

    sleep(3);

    if (strcmp(buffer, (char*)flag))
    {   
        puts("Sorre, you didn't pass Ediniy Goverment Examen po CTF! Zdem tibya cherez god ;)");
        exit(1);
    }
    
    puts("Your score: 100/100");
}