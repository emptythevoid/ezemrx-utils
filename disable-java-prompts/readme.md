These two files will remove annoying Java promtps when interacting with jnlp files. This will *disable* certificate revocation checks and will explicitely trust the sectigo cert (at least at the time of this upload). Tested on 8u192 and 8u471

Usage:

These files have to be deployed per-user in the following paths:

C:\users\<user>\AppData\LocalLow\Sun\Java\Deployment\deployment.properties

C:\users\<user>\AppData\LocalLow\Sun\Java\Deploment\security\trusted.certs
