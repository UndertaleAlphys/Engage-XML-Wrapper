# Engage-XML-Wrapper

## What do the scripts do?

They update XLSX and XML files to your ROMFS or Cobalt mod (based on _EngageXML_ and _Cobalt-Migrator_).  
If you prefer GUI-based editing, _Astra_ by thane98 is a good choice.  
[https://github.com/thane98/Astra](https://github.com/thane98/Astra)

## Configs before starting

1. _EngageXML_ and _Cobalt-Migrator_ are required.  
   [https://github.com/AraragiHoozuki/EngageXml](https://github.com/AraragiHoozuki/EngageXml)  
   [https://github.com/DivineDragonFanClub/cobalt-migrator](https://github.com/DivineDragonFanClub/cobalt-migrator)  
   Then, edit the config\general.yaml file with your text editor. You need to specify the paths of these two executable files and save it.

2. Edit _romfs_update.yaml_, where you need to specify the folder containing your XLSX/XML/bytes or other files. Note that the files should follow **the same pattern**. An example is provided below.  
   If _romfs_update.yaml_ looks like this:
   ```
   input directory path: input
   output directory path: output\WhateverMod\romfs\Data\StreamingAssets\aa\Switch
   ```
   A XLSX file with the following input path:
   ```
   input xlsx path: input\fe_assets_gamedata\whatever.xlsx
   ```
   will be updated to:
   ```
   updated bundle path: output\WhateverMod\romfs\Data\StreamingAssets\aa\Switch\whatever.xml.bundle
   ```
   When everything is set, save the file.

3. Edit _cobalt_update.yaml_. In most cases, the _romfs mod directory path_ is the place where your mod is located, and the _cobalt mod directory path_ is typically located at:
   ```
   Your emulator directory\sdcard\engage\mods
   ```

## Usage

Once everything is set, you can update your mod with a single click.

1. _multi_bundle_to_xlsx_ converts several bundle files to XLSX when you drag the files into the program.  
2. _multi_item_convert_ does something similar but deals with non-XML bundles.  
3. _update_to_romfs_ updates your edited files to ROMFS mods.  
4. _update_to_cobalt_ first performs the same action, then migrates the ROMFS mod to Cobalt.
