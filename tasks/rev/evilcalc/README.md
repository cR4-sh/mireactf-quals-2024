# rev | evilcalc

## Information
    Удобный калькулятор, жаль триалка короткая.

## Public
evilcalc.apk

## Writeup
Task shows how obfuscated jetpack-compose Android application can look like.
The goal is to determine "activation" code for this calculator through reverse engineering `.apk` using JADX or similar tool. :)

The entrypoint could be found in AndroidManifest file in activity declaration.
We're interested in activity having intent-filter of category `android.intent.category.LAUNCHER` and action `android.intent.action.MAIN`.
```
<activity
    android:name="ctf.task.evilcalc.Evil"
    android:exported="true"
    ...
```

In the obfescated code of `onCreate` method might be found a call to viewmodel object setup methods.
Immediately pops up a call to decryption method with `data` and `key` (thanks Kotlin for revealing variable names).
As `data` paramter passed a hardcoded base64-string `Sn18dXMhCrmaseKT3Ub2sU9FY32HEsTwvFZPeZ9XsSY3a3/Nk3FHHFlHVzRcUV7n+iBnuqZkVCYNvbof1zDyeg==`.
The second parameter is the key. Following function calls we can understand that key is entered value to the calculator input field.
Before the call of decryption function we can notice constraints applied to the code. Following up function calls determine the key: `ᛗᛟᚾᛊᛏᛖᚱ ᛁᚾ ᚨ ᛊᚺᛖᛚᛚ`.
Open application, enter code and flag is yours.

## Flag
`mireactf{why_n0t_ju5t_cl34r_st0r4g3_3v3ry_t1me?}`
