# web | Access Denied

## Information
 еда

## Writeup
SSTI twig in card number
Then need make shell into container, understood that we cant find flag on system => need lpe
make sudo -l and view that we can run python script as root without password. In script importing library re, which we can redact. So need place backdoor on func findall in re.py library. 

Useful link: https://www.hackingarticles.in/linux-privilege-escalation-python-library-hijacking/
## Flag
`mireactf{uuid8}`