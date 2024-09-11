## Java Web Start hangs, preventing scanning
kill_javaws.bat


## Notes
Java: Newer versions of Java do not support the jnlp web start process, which will likely break document scanning and signature capture.  Further, scanning requires sk.gnome.twain.twainmanagement which does not seem to be supported after Java 8u192 anyway.  Even if you use openwebstart to resume web start capability, it will fail due to this class either being unsupported, or not licensed for newer Java versions. This appears to be a part of the Moreno library, so I'm not certain why it fails on newer Java runtimes.

OpenJDK: OpenJDK never supported web start, so this is not a useful solution to launching jnlp files
