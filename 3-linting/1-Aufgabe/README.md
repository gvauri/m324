# Reproduziere das Beispiel aus dem Kapitel Code Analyse.

1. Wie hoch ist die Test Coverage?

2. Schreibe weitere Unit Tests, um die Test Coverage zu erhöhen.

3. Wie viele Verbesserungsvorschläge zu Bugs und Code Smell sind enthalten?

4. Korrigiere alle vorgeschlagenen Änderungen.

```docker
 docker run --rm \
    --platform linux/amd64 \
    -e SONAR_HOST_URL="http://sonarqube:9000" \
    -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=house" \
    -e SONAR_TOKEN="squ_11ba443ab51f04d27cfda8fb693bd0d25206f2fc" \
    --network sonar-net \
    -v "$(pwd)":/usr/src \
    -u $(id -u):$(id -g) \
    sonarsource/sonar-scanner-cli
```

# Ich konnte den Server starten aber der sonar scanner funktioniert nicht.


java.lang.IllegalStateException: Unable to create directory: /opt/sonar-scanner/.sonar/cache
        at org.sonarsource.scanner.downloadcache.DownloadCache.mkdirs(DownloadCache.java:141)
        at org.sonarsource.scanner.downloadcache.DownloadCache.<init>(DownloadCache.java:48)
        at org.sonarsource.scanner.downloadcache.DownloadCache.<init>(DownloadCache.java:53)
        at org.sonarsource.scanner.lib.ScannerEngineBootstrapper.bootstrap(ScannerEngineBootstrapper.java:138)
        at org.sonarsource.scanner.cli.Main.analyze(Main.java:76)
        at org.sonarsource.scanner.cli.Main.main(Main.java:64)
Caused by: java.nio.file.AccessDeniedException: /opt/sonar-scanner/.sonar/cache
        at java.base/sun.nio.fs.UnixException.translateToIOException(UnixException.java:90)
        at java.base/sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:106)
        at java.base/sun.nio.fs.UnixException.rethrowAsIOException(UnixException.java:111)
        at java.base/sun.nio.fs.UnixFileSystemProvider.createDirectory(UnixFileSystemProvider.java:397)
        at java.base/java.nio.file.Files.createDirectory(Files.java:700)
        at java.base/java.nio.file.Files.createAndCheckIsDirectory(Files.java:807)
        at java.base/java.nio.file.Files.createDirectories(Files.java:793)
        at org.sonarsource.scanner.downloadcache.DownloadCache.mkdirs(DownloadCache.java:139)
        ... 5 common frames omitted


# Ich weiss nicht wie ich den Zugriff geben kann.