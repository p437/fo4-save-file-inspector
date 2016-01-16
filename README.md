# Fallout4 save file dissector

Just download the zip and click main.py. You must have a version of python installed. 2.7 and 3k should work. If you have not yet installed python on your Microsoft Windows operating system, go there https://www.python.org/downloads/.

This programs lists the fallout 4 save files identified in the default location.

This is just a little crappy attempt to reverse-engineer the save file format, because i'm sick of writing down weapons properties to perform a manual comparison.

    C:\Users\heh\Desktop\fallout4>main.py
    ROBOCO INDUSTRIES (TM) TERMINK PROTOCOL

         Fallout4 save file inspector


    Identifying runtime :

    01 system            : Windows
    02 platform          : Windows-7-6.1.7601-SP1
    03 machine           : AMD64
    04 architecture      : ('32bit', 'WindowsPE')
    05 processor         : Intel64 Family 6 Model 30 Stepping 5, GenuineIntel
    06 python            : CPython

    Using save directory: C:\Users\heh\Documents\My Games\Fallout4\Saves
    Listing directory..
    Found 44 saves.
    Parsing..
    Sorting..
       0    Sun Dec 13 23:32:13 2015        1       PrewarVault111
       1    Mon Dec 14 22:03:38 2015        1       Vault111Cryo
       2    Mon Dec 14 22:34:51 2015        1       Commonwealth
       3    Wed Dec 16 16:05:06 2015        3       Commonwealth
       4    Wed Dec 16 18:06:03 2015        4       Commonwealth
       5    Wed Dec 16 22:46:48 2015        6       Commonwealth
       6    Wed Dec 16 23:22:58 2015        6       Commonwealth
       7    Thu Dec 17 21:48:53 2015        7       Commonwealth
       8    Fri Dec 18 23:27:39 2015        8       Commonwealth
       9    Fri Dec 18 23:35:17 2015        9       Commonwealth
      10    Sun Dec 20 21:30:08 2015        9       Commonwealth
      11    Sun Dec 20 22:06:34 2015        9       CorvegaAssemblyPlant01
      12    Sun Dec 20 22:31:40 2015        9       CorvegaAssemblyPlant01
      13    Mon Dec 21 22:15:19 2015        10      CorvegaAssemblyPlant01
      14    Mon Dec 21 22:47:39 2015        10      Commonwealth
      15    Mon Dec 21 23:35:04 2015        11      ArcjetSystems01
      16    Tue Dec 22 00:00:23 2015        11      Commonwealth
      17    Mon Dec 28 17:12:01 2015        12      WestonWaterTreatment01
      18    Mon Dec 28 17:13:17 2015        12      WestonWaterTreatment01
      19    Mon Dec 28 20:29:17 2015        12      Commonwealth
      20    Mon Dec 28 21:43:57 2015        12      Commonwealth
      21    Mon Dec 28 22:18:24 2015        12      CambridgePD01
      22    Tue Dec 29 19:20:40 2015        13      Commonwealth
      23    Wed Dec 30 14:41:51 2015        13      DmndPublick01
      24    Wed Dec 30 17:58:58 2015        13      Commonwealth
      25    Wed Dec 30 18:17:27 2015        13      Commonwealth
      26    Wed Dec 30 18:23:46 2015        14      Commonwealth
      27    Wed Dec 30 18:28:31 2015        14      Commonwealth
      28    Wed Dec 30 18:40:57 2015        14      Commonwealth
      29    Wed Dec 30 18:45:43 2015        14      Commonwealth
      30    Wed Dec 30 19:01:28 2015        14      Vault114
      31    Wed Dec 30 19:24:57 2015        14      Vault114
      32    Wed Dec 30 19:40:00 2015        15      DiamondCity
      33    Wed Dec 30 22:14:59 2015        15      DiamondCity
      34    Sun Jan  3 15:31:50 2016        15      Commonwealth
      35    Sun Jan  3 16:43:19 2016        15      FortHagen01
      36    Sun Jan  3 17:10:39 2016        16      FortHagen02
      37    Sun Jan  3 17:33:15 2016        16      DmndStandsTaphouse01
      38    Thu Jan  7 23:21:12 2016        16      DiamondCity
      39    Thu Jan  7 23:41:37 2016        16      TrinityTower01
      40    Tue Jan 12 22:05:28 2016        17      DiamondCity
      41    Tue Jan 12 22:15:03 2016        17      DmndPlayerHouse01
      42    Tue Jan 12 22:18:06 2016        17      DiamondCity
      43    Tue Jan 12 22:18:10 2016        17      DiamondCity

    Ready. Enter a save number, "q" to quit, and "a" to print all information
    > 0
    0 <class 'str'>
    File name           : Save1_C36BA0EB_526172697479_PrewarVault111_000026_20151213223213_1_2.fos
    Byte count          : 3315895
    Last access         : Sun Dec 13 23:32:13 2015
    Save type           : Save1
    ?hex id?            : C36BA0EB
    ?dec id?            : 526172697479
    Ingame location     : PrewarVault111
    Played time         : 000026
    Timestamp           : 20151213223213
    Player level        : 1
    ?const 2?           : 2
    01_magic            : 464f345f5341564547414d45         FO4_SAVEGAME
    02_magic_correct    : False
    03_header_length    : 105
    04_unknown_int_B    : 11
    05_unknown_int_C    : 1
    07_username_len     : 6
    07_username_str     : 'Rarity'
    08_unknown_int_D    : 1
    09_location_len     : 9
    09_location_str     : 'Vault 111'
    10_played_time_len  : 35
    10_played_time_str  : '0d.0h.26m.0 days.0 hours.26 minutes'
    11_race_len         : 9
    11_race_str         : 'HumanRace'
    980_full_header     : 464f345f5341564547414d4569000000 FO4_SAVEGAMEi···
                          0b000000010000000600526172697479 ··········Rarity
                          0100000009005661756c742031313123 ······Vault 111#
                          0030642e30682e32366d2e3020646179 ·0d.0h.26m.0 day
                          732e3020686f7572732e3236206d696e s.0 hours.26 min
                          75746573090048756d616e5261636501 utes··HumanRace·
                          000000000000004843               ·······HC
    981_10last          : 01000000000000004843             ········HC
    99_next_32          : d045d31cf635d1018002000080010000 ·E···5··········
                          1d4b74ff1d4b72ff1d4b74ff1d4b74ff ·Kt··Kr··Kt··Kt·
    Press enter to exit.
