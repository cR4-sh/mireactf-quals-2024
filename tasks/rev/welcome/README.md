# rev | welcome

## Information
    Структрура apk известна всем. Ведь так?

## Public
welcome.apk

## Writeup
The task is to analyze the structure of given `.apk` file and find 7 flag parts in code and resources of the application.

1 - **mireactf{** and **4ndr01d_1** in xml layout of MainActivity (res/layout/activity_main.xml)
2 - **n_l0v3_w1** - from application metadata tag stored in AndroidManifest.xml
3 - **7h_57r1n6_r350urc3** - from string resources (res/values/strings.xml)
4 - **5_n471v3_l1b5_u** - string in a native library `libwelcome` (actually was "6\`o5u2w4\`m2c6\`v", near it implementation of rot(-1))
5 - **nus3d_4ss3ts_h** - asset string (assets/secret_data)
6 - **4rdc0d3d_d474_4** - hardcoded "authorization token" in base64 form with swapped even and odd characters (NetworkManager)
7 - **nd_j3tp4ck_c0mp053}** - from text element in Jetpack Compose activity (ComposeActivity)

## Flag
`mireactf{4ndr01d_1n_l0v3_w17h_57r1n6_r350urc35_n471v3_l1b5_unus3d_4ss3ts_h4rdc0d3d_d474_4nd_j3tp4ck_c0mp053}`
