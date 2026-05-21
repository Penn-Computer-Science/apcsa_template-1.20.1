# APCSA Fabric Modding Template

## Setup
I've simplified the process and all you need to do is run the `SETUP.py` file!

Simply just run it, answer the questions it asks, and your project should be good!

*If you opened this in IntelliJ IDEA first, stop the build and then run the `SETUP.py` file*

For this to build, you NEED at least Java 21 (I go with Java 25)

I typically go with `JetBrains Runtime (JCEF) 25.0.3`, as that allows you to "hotload" some changes without restarting the client

To do this, do this:
1. File > Project Settings
2. SDK > Download JDK...
3. Select your Java Version (21+)
4. Select Java Vendor (None of the ones in `Other Versions`)
5. Click Download, then Done
6. Wait for it to download
7. Once done, File > Settings
8. Build, Execution, Deployment > Build Tools
9. Gradle > Gradle JVM
10. Set it to `PROJECT JVM` or your downloaded Java Version
11. You're done! Click the `Sync` button under `Build`

Once it's done syncing, if there are no configurations, restart IntelliJ

If it asks you to download a `Minecraft Development` plugin, install it and restart IntelliJ

### Happy Modding!

## Useful Links
[Fabric Getting Started Guide](https://docs.fabricmc.net/1.20.4/develop/getting-started/project-structure) - `1.20.4` is the closest to our version


[Fabric Maven API](https://maven.fabricmc.net/docs/yarn-1.20.1+build.1/index.html) - This is the closest thing I could find to the `1.20.1` docs (it's scary)

## License
This template is available under the CC0 license. Feel free to learn from it and incorporate it in your own projects.
