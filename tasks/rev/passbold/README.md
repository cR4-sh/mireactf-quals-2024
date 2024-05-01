# rev | passbold

## Information
    Каждый уважающий себя хакер должен использовать парольный менеджер собственной разработки.
    Но все когда-то хранили пароли в `.txt`...
## Public
MyPasswords.txt
passbold.zip

## Writeup
Given .NET Core 6 Windows Forms password manager application binary and a account entry leak. The goal is to get other passwords from manager's storage file.
Application uses .net apphost destribution scheme and ReadyToRun configuration, therefore some of RE tools may not be able to open file correctly. ILSpy and dotPeek works perfect. The other way is to extract .NET assemblies by hand and reverse it in dnSpy, etc.

For master password recovery script look into `writeup/solution.py`

## Flags
Password Manager master password: `!t's_5uP3r_53cR3t#`

Flag: `mireactf{n3t_c0r3_l34kz_r3v34l_s3cr3ts}`

