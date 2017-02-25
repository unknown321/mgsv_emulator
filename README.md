# mgsv_emulator
mgsv client/server emulator

Types of encryption implemented: COMMON, COMPOUND.

# Encryption details
Every message between server and client is encrypted using blowfish algorythm.
Unfortunately it slightly differs from realisation provided here (https://www.schneier.com/academic/blowfish/download.html), so I had to rewrite it from scratch.

Decryption process:

*decode base64-encoded message into bytestream
*decode bytestream using static blowfish key (hardcoded into exe) into json message
*if 'session_crypto' is true, then contents of message['data'] are encrypted with session cryptokey provided by server during auth phase
*if 'compress' is true, then decoded message['data'] is also compressed using zlib

Encryption process is the same, but backwards.

# How to use
Provide your credentials in settings.py (steamid and magic_hash parsed from previously captured session). Steam_ticket is not required.
Dump static_key from exe (or ask me very nicely).

Client:
    from emulator import Client
    c = Client()
    c.login()

login() will automatically parse requests and save session cryptokey (so you won't have to manually use it every time).
Afterwards, feel free to call any command available, see https://github.com/unknown321/mgsv_nuke_watcher as an example.

Server part is not implemented yet.
