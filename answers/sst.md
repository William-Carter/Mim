<!--sst-->
### How to Install Source Speedrun Tools (SST)
1. Download the auto-update script from [here](https://dl.mikes.software/sst-updatescript.zip)
2. Unzip the folder and rename it to sst
https://media.discordapp.net/attachments/874115875685429341/1413786007005958325/extractAll.png?ex=68bd3252&is=68bbe0d2&hm=fdfca22fdcd3b86c63997b1fad4b38b9c34db9a7cf647720a2b5a336ec27a6d4&=&format=webp&quality=lossless&width=444&height=498
https://media.discordapp.net/attachments/874115875685429341/1413785647357104259/rename.png?ex=68bd31fd&is=68bbe07d&hm=61ab3407673dffe4b4f271cce069be602f58964a591d98c834e27d35331f2ea2&=&format=webp&quality=lossless&width=311&height=113
3. Move the folder next to your `portal` folder
https://media.discordapp.net/attachments/874115875685429341/1413786789319147531/sst.png?ex=68bd330d&is=68bbe18d&hm=a6a9efe5c938773624cfbe847b5f2314226be76fff7634cd97876fd3255381f3&=&format=webp&quality=lossless&width=348&height=489
4. Edit your `portal.bat` and add `call sst/update.bat` on the line before game start.
https://media.discordapp.net/attachments/874115875685429341/1413787510370340914/sstautoupdate.png?ex=68bd33b9&is=68bbe239&hm=41ec2231a34cc7ab3e2a18237232d06ae67eca60485cdac352689693f6221b3e&=&format=webp&quality=lossless&width=280&height=110
5. Open the game. In the console, run `plugin_load ../sst/sst` to load sst for the first time.
https://cdn.discordapp.com/attachments/874115875685429341/1413788309611872266/image.png?ex=68bd3477&is=68bbe2f7&hm=dd2f6ad62b847f1c7848500efa41f32834edb7c86efcb6379accf72a6d9c5418&
6. Finally, run `sst_autoload_enable` to automatically load sst in the future