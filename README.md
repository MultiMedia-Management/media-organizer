# media-organizer
The main idea of this project is to help you organize all of your medias, which means, basically, pictures and videos.

With this goal in mind, this app will scan the directories that you specify and as a result, it will create a nice and very well structured and organized set of folders that will help to move on.

This project it still under work, so, pretty soon I'll update the readme with some additional information, but let me share some points right now.

<b>

## Supported Extensions
At this moment, we are supporting a limited number of extensions, in this way, we can guarantee that the application will behave as expected. Note that these will likely be the majority of files you have. Once we cover new extensions. Please, let us share the complete list.
 - jpg
 - jpeg
 - mp4
 - mov

<br>

1. We are using a simple `JSON` file as our db at this moment, `~/.mo_hash.json`
In order to proceed, there are two approaches here that we have to keep in mind.

<br>

## First Approach
You have already something organized and you have a folder for that, for example `/home/user/my_memories`. That said, let's use the current folder as our `target-dir`
- You can set a target dir using `mo.py setup target-dir`.
- Once you have your `target-dir` set, we can move along and load our data with all the medias you have. In order to do that, you can run `mo.py db reload`

Note: If you have a huge number of medias, this can spend some time, so please, be patiente.

- Once the load is done, you would be ok to move forward. Let's say you have a folder with some pictures that you would like to add to your organized place, and let say this folder is located at `/home/user/pictures`, so you would be ok to execute `mo.py import-files source-dir /home/user/pictures`. This will allow the app to scan all the files under that structure recursively, and as consequence, this will create a folder located at `<YOU TARGER-DIR HERE>/MO_DIR` with some subdirectories, that will be similar to below.
```
/home/user/my_memories/MO_DIR/
├── 0000
│   └── 00
│       ├── PICTURE
│       └── VIDEO
├── 1999
│   ├── 05
│   │   └── PICTURE
│   └── 06
│       └── PICTURE
├── 2000
│   ├── 03
│   │   └── PICTURE
│   ├── 11
│   │   └── VIDEO
│   └── 12
│       └── VIDEO
├── 2023
│   ├── 01
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 02
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 03
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 04
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 05
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 06
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 07
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 08
│   │   ├── PICTURE
│   │   └── VIDEO
│   └── 09
│       ├── PICTURE
│       └── VIDEO
└── UNKNOWN
    ├── PICTURE
    └── VIDEO
```
Above you can notice that we have some medias from different years, also, `0000` and `UNKNOWN`. Basically, if the machine was not set properly with the date and time, or if the bateries for the old cameras was not charged, then you can see things like this. Now, about the `unknown`, this will happen with all the medias that someone send to you via `IM` or `Instant Message` in general, for example, `whatsapp`.

Keep in mind, for all the operation above, your pictures will not be deleted, and at the end of each operation that you do, a complete report will be generated in your home dir under the folder `~/mo_reports`, with the results of your actions. With that, you would be ok to move on and remove the files from the source, once now, you have a single copy on your `MO_DIR` folder, organized and happy.


<br>

## Second Approach
You have only a lot of directories with a bunch of pictures, nothing organized and you are really looking for something that will help you out. If this is the case, you can create a new empty folder that will be used as your `target-dir`, for example, `/home/user/my_memories`
- You can set a target dir using `mo.py setup target-dir`.
- Let's say you have a folder with some pictures that you would like to add to your organized place, and let say this folder is located at `/home/user/pictures`, so you would be ok to execute `mo.py import-files source-dir /home/user/pictures`. This will allow the app to scan all the files under that structure recursively, and as consequence, this will create a folder located at `<YOU TARGER-DIR HERE>/MO_DIR` with some subdirectories, that will be similar to below.
```
/home/user/my_memories/MO_DIR/
├── 0000
│   └── 00
│       ├── PICTURE
│       └── VIDEO
├── 1999
│   ├── 05
│   │   └── PICTURE
│   └── 06
│       └── PICTURE
├── 2000
│   ├── 03
│   │   └── PICTURE
│   ├── 11
│   │   └── VIDEO
│   └── 12
│       └── VIDEO
├── 2023
│   ├── 01
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 02
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 03
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 04
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 05
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 06
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 07
│   │   ├── PICTURE
│   │   └── VIDEO
│   ├── 08
│   │   ├── PICTURE
│   │   └── VIDEO
│   └── 09
│       ├── PICTURE
│       └── VIDEO
└── UNKNOWN
    ├── PICTURE
    └── VIDEO
```
Above you can notice that we have some medias from different years, also, `0000` and `UNKNOWN`. Basically, if the machine was not set properly with the date and time, or if the bateries for the old cameras was not charged, then you can see things like this. Now, about the `unknown`, this will happen with all the medias that someone send to you via `IM` or `Instant Message` in general, for example, `whatsapp`.

Keep in mind, for all the operation above, your pictures will not be deleted, and at the end of each operation that you do, a complete report will be generated in your home dir under the folder `~/mo_reports`, with the results of your actions. With that, you would be ok to move on and remove the files from the source, once now, you have a single copy on your `MO_DIR` folder, organized and happy.


In the future, I'll add a video presenting how to use it and all the features that we have.

Please, I hope you enjoy it and any feedback will be very welcome. It could be via email <waldirio@gmail.com> or via [issue](https://github.com/MultiMedia-Management/media-organizer/issues/new/choose)