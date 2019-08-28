OpenCL Platform #1: NVIDIA Corporation
======================================
* Device #1: Tesla V100-SXM2-16GB, 4032/16130 MB allocatable, 80MCU

Benchmark relevant options:
===========================
* --benchmark-all
* --optimized-kernel-enable

Hashmode: 0 - MD5

Speed.#1.........: 55020.6 MH/s (48.28ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 10 - md5($pass.$salt)

Speed.#1.........: 55216.9 MH/s (48.21ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 11 - Joomla < 2.5.18

Speed.#1.........: 55277.3 MH/s (48.15ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 12 - PostgreSQL

Speed.#1.........: 55351.7 MH/s (48.09ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 20 - md5($salt.$pass)

Speed.#1.........: 29920.2 MH/s (88.81ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 21 - osCommerce, xt:Commerce

Speed.#1.........: 29926.9 MH/s (88.81ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 22 - Juniper NetScreen/SSG (ScreenOS)

Speed.#1.........: 29659.2 MH/s (89.63ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 23 - Skype

Speed.#1.........: 29886.8 MH/s (88.95ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 30 - md5(utf16le($pass).$salt)

Speed.#1.........: 53921.2 MH/s (48.54ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 40 - md5($salt.utf16le($pass))

Speed.#1.........: 29924.3 MH/s (88.98ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 50 - HMAC-MD5 (key = $pass)

Speed.#1.........:  8692.8 MH/s (76.41ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 60 - HMAC-MD5 (key = $salt)

Speed.#1.........: 18237.6 MH/s (72.87ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 100 - SHA1

Speed.#1.........: 17054.2 MH/s (77.93ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 101 - nsldap, SHA-1(Base64), Netscape LDAP SHA

Speed.#1.........: 17048.2 MH/s (77.95ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 110 - sha1($pass.$salt)

Speed.#1.........: 17082.1 MH/s (77.95ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 111 - nsldaps, SSHA-1(Base64), Netscape LDAP SSHA

Speed.#1.........: 17087.1 MH/s (77.95ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 112 - Oracle S: Type (Oracle 11+)

Speed.#1.........: 17090.1 MH/s (77.93ms) @ Accel:128 Loops:512 Thr:256 Vec:2

Hashmode: 120 - sha1($salt.$pass)

Speed.#1.........: 12385.7 MH/s (53.62ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 121 - SMF (Simple Machines Forum) > v1.1

Speed.#1.........: 12381.2 MH/s (53.64ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 122 - macOS v10.4, macOS v10.5, MacOS v10.6

Speed.#1.........: 12381.3 MH/s (53.65ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 124 - Django (SHA-1)

Speed.#1.........: 12379.9 MH/s (53.64ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 125 - ArubaOS

Speed.#1.........: 12380.9 MH/s (53.64ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 130 - sha1(utf16le($pass).$salt)

Speed.#1.........: 17403.9 MH/s (76.14ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 131 - MSSQL (2000)

Speed.#1.........: 17399.6 MH/s (76.15ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 132 - MSSQL (2005)

Speed.#1.........: 17396.2 MH/s (76.16ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 133 - PeopleSoft

Speed.#1.........: 17398.5 MH/s (76.16ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 140 - sha1($salt.utf16le($pass))

Speed.#1.........: 12405.6 MH/s (53.63ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 141 - Episerver 6.x < .NET 4

Speed.#1.........: 12406.6 MH/s (53.63ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 150 - HMAC-SHA1 (key = $pass)

Speed.#1.........:  3564.1 MH/s (93.24ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 160 - HMAC-SHA1 (key = $salt)

Speed.#1.........:  6585.6 MH/s (50.42ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 200 - MySQL323

Speed.#1.........:   172.9 GH/s (15.27ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 300 - MySQL4.1/MySQL5

Speed.#1.........:  7463.3 MH/s (89.06ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 400 - phpass, WordPress (MD5), phpBB3 (MD5), Joomla (MD5) (Iterations: 2048)

Speed.#1.........: 12873.0 kH/s (84.25ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 500 - md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5) (Iterations: 1000)

Speed.#1.........: 19408.0 kH/s (50.76ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 501 - Juniper IVE (Iterations: 1000)

Speed.#1.........: 19195.9 kH/s (50.88ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 600 - BLAKE2b

Speed.#1.........:  4025.3 MH/s (82.50ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 900 - MD4

Speed.#1.........: 81452.3 MH/s (32.58ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 1000 - NTLM

Speed.#1.........: 77706.4 MH/s (33.97ms) @ Accel:128 Loops:1024 Thr:256 Vec:2

Hashmode: 1100 - Domain Cached Credentials (DCC), MS Cache

Speed.#1.........: 22257.4 MH/s (59.80ms) @ Accel:128 Loops:512 Thr:256 Vec:4

Hashmode: 1300 - SHA2-224

Speed.#1.........:  7411.5 MH/s (89.70ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1400 - SHA2-256

Speed.#1.........:  7612.5 MH/s (87.31ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1410 - sha256($pass.$salt)

Speed.#1.........:  7632.1 MH/s (87.29ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1411 - SSHA-256(Base64), LDAP {SSHA256}

Speed.#1.........:  7632.7 MH/s (87.28ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1420 - sha256($salt.$pass)

Speed.#1.........:  6691.0 MH/s (49.62ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1421 - hMailServer

Speed.#1.........:  6691.3 MH/s (49.62ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1430 - sha256(utf16le($pass).$salt)

Speed.#1.........:  7523.0 MH/s (88.08ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 1440 - sha256($salt.utf16le($pass))

Speed.#1.........:  6702.0 MH/s (49.61ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1441 - Episerver 6.x >= .NET 4

Speed.#1.........:  6703.4 MH/s (49.62ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 1450 - HMAC-SHA256 (key = $pass)

Speed.#1.........:  1206.9 MH/s (68.84ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 1460 - HMAC-SHA256 (key = $salt)

Speed.#1.........:  2737.5 MH/s (60.68ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1500 - descrypt, DES (Unix), Traditional DES

Speed.#1.........:  1810.5 MH/s (92.46ms) @ Accel:8 Loops:1024 Thr:256 Vec:1

Hashmode: 1600 - Apache $apr1$ MD5, md5apr1, MD5 (APR) (Iterations: 1000)

Speed.#1.........: 19189.0 kH/s (50.82ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 1700 - SHA2-512

Speed.#1.........:  2337.8 MH/s (71.05ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1710 - sha512($pass.$salt)

Speed.#1.........:  2342.3 MH/s (71.09ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1711 - SSHA-512(Base64), LDAP {SSHA512}

Speed.#1.........:  2342.5 MH/s (71.08ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1720 - sha512($salt.$pass)

Speed.#1.........:  2185.8 MH/s (76.02ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1722 - macOS v10.7

Speed.#1.........:  2185.9 MH/s (76.01ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1730 - sha512(utf16le($pass).$salt)

Speed.#1.........:  2335.1 MH/s (70.93ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1731 - MSSQL (2012, 2014)

Speed.#1.........:  2338.3 MH/s (70.93ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1740 - sha512($salt.utf16le($pass))

Speed.#1.........:  2225.2 MH/s (74.79ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 1750 - HMAC-SHA512 (key = $pass)

Speed.#1.........:   441.6 MH/s (94.47ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 1760 - HMAC-SHA512 (key = $salt)

Speed.#1.........:   917.2 MH/s (90.60ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 1800 - sha512crypt $6$, SHA512 (Unix) (Iterations: 5000)

Speed.#1.........:   378.7 kH/s (85.21ms) @ Accel:512 Loops:128 Thr:32 Vec:1

Hashmode: 2100 - Domain Cached Credentials 2 (DCC2), MS Cache 2 (Iterations: 10240)

Speed.#1.........:   656.8 kH/s (49.42ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 2400 - Cisco-PIX MD5

Speed.#1.........: 39536.9 MH/s (67.22ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 2410 - Cisco-ASA MD5

Speed.#1.........: 41189.4 MH/s (64.52ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 2500 - WPA-EAPOL-PBKDF2 (Iterations: 4096)

Speed.#1.........:   807.5 kH/s (50.02ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 2501 - WPA-EAPOL-PMK (Iterations: 1)

Speed.#1.........: 54439.8 kH/s (0.02ms) @ Accel:128 Loops:1 Thr:256 Vec:1

Hashmode: 2600 - md5(md5($pass))

Speed.#1.........: 15677.4 MH/s (84.79ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 2611 - vBulletin < v3.8.5

Speed.#1.........: 15667.9 MH/s (84.83ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 2612 - PHPS

Speed.#1.........: 15668.3 MH/s (84.83ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 2711 - vBulletin >= v3.8.5

Speed.#1.........: 11108.7 MH/s (59.80ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 2811 - IPB2+ (Invision Power Board), MyBB 1.2+

Speed.#1.........: 11656.3 MH/s (56.98ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 3000 - LM

Speed.#1.........: 45331.7 MH/s (58.56ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 3100 - Oracle H: Type (Oracle 7+)

Speed.#1.........:  2417.9 MH/s (68.70ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 3200 - bcrypt $2*$, Blowfish (Unix) (Iterations: 32)

Speed.#1.........:    54245 H/s (46.05ms) @ Accel:16 Loops:8 Thr:8 Vec:1

Hashmode: 3710 - md5($salt.md5($pass))

Speed.#1.........: 14896.7 MH/s (44.58ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 3711 - MediaWiki B type

Speed.#1.........: 14930.3 MH/s (89.02ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 3800 - md5($salt.$pass.$salt)

Speed.#1.........: 29996.4 MH/s (88.62ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 3910 - md5(md5($pass).md5($salt))

Speed.#1.........: 11122.7 MH/s (59.73ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 4010 - md5($salt.md5($salt.$pass))

Speed.#1.........: 11922.9 MH/s (55.70ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 4110 - md5($salt.md5($pass.$salt))

Speed.#1.........: 12613.3 MH/s (52.66ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 4300 - md5(strtoupper(md5($pass)))

Speed.#1.........: 15665.5 MH/s (84.85ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 4400 - md5(sha1($pass))

Speed.#1.........:  9381.2 MH/s (70.81ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 4500 - sha1(sha1($pass))

Speed.#1.........:  6618.9 MH/s (50.17ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 4520 - sha1($salt.sha1($pass))

Speed.#1.........:  5690.0 MH/s (58.36ms) @ Accel:128 Loops:128 Thr:256 Vec:2

Hashmode: 4521 - Redmine

Speed.#1.........:  5689.9 MH/s (58.37ms) @ Accel:128 Loops:128 Thr:256 Vec:2

Hashmode: 4522 - PunBB

Speed.#1.........:  5690.5 MH/s (58.37ms) @ Accel:128 Loops:128 Thr:256 Vec:2

Hashmode: 4700 - sha1(md5($pass))

Speed.#1.........:  9645.7 MH/s (68.88ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 4800 - iSCSI CHAP authentication, MD5(CHAP)

Speed.#1.........: 32608.9 MH/s (81.51ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 4900 - sha1($salt.$pass.$salt)

Speed.#1.........: 12039.2 MH/s (55.17ms) @ Accel:128 Loops:256 Thr:256 Vec:4

Hashmode: 5100 - Half MD5

Speed.#1.........: 34489.5 MH/s (77.08ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 5200 - Password Safe v3 (Iterations: 2048)

Speed.#1.........:  2903.5 kH/s (54.21ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 5300 - IKE-PSK MD5

Speed.#1.........:  4242.8 MH/s (78.30ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 5400 - IKE-PSK SHA1

Speed.#1.........:  1475.8 MH/s (56.27ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 5500 - NetNTLMv1 / NetNTLMv1+ESS

Speed.#1.........: 44172.1 MH/s (59.82ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 5600 - NetNTLMv2

Speed.#1.........:  3809.1 MH/s (87.39ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 5700 - Cisco-IOS type 4 (SHA256)

Speed.#1.........:  7614.0 MH/s (87.29ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 5800 - Samsung Android Password/PIN (Iterations: 1023)

Speed.#1.........: 10509.7 kH/s (43.11ms) @ Accel:128 Loops:255 Thr:256 Vec:1

Hashmode: 6000 - RIPEMD-160

Speed.#1.........:  9922.7 MH/s (66.96ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 6100 - Whirlpool

Speed.#1.........:   780.2 MH/s (53.43ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 6211 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit (Iterations: 2000)

Speed.#1.........:   620.0 kH/s (66.33ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 6212 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit (Iterations: 2000)

Speed.#1.........:   212.5 kH/s (59.12ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 6213 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit (Iterations: 2000)

Speed.#1.........:   240.7 kH/s (84.50ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 6221 - TrueCrypt PBKDF2-HMAC-SHA512 + XTS 512 bit (Iterations: 1000)

Speed.#1.........:   754.4 kH/s (81.21ms) @ Accel:64 Loops:62 Thr:256 Vec:1

Hashmode: 6222 - TrueCrypt PBKDF2-HMAC-SHA512 + XTS 1024 bit (Iterations: 1000)

Speed.#1.........:   269.3 kH/s (75.03ms) @ Accel:64 Loops:31 Thr:256 Vec:1

Hashmode: 6223 - TrueCrypt PBKDF2-HMAC-SHA512 + XTS 1536 bit (Iterations: 1000)

Speed.#1.........:   191.6 kH/s (56.68ms) @ Accel:32 Loops:31 Thr:256 Vec:1

Hashmode: 6231 - TrueCrypt PBKDF2-HMAC-Whirlpool + XTS 512 bit (Iterations: 1000)

Speed.#1.........:   119.2 kH/s (169.65ms) @ Accel:32 Loops:31 Thr:256 Vec:1

Hashmode: 6232 - TrueCrypt PBKDF2-HMAC-Whirlpool + XTS 1024 bit (Iterations: 1000)

Speed.#1.........:    58938 H/s (165.86ms) @ Accel:32 Loops:15 Thr:256 Vec:1

Hashmode: 6233 - TrueCrypt PBKDF2-HMAC-Whirlpool + XTS 1536 bit (Iterations: 1000)

Speed.#1.........:    39173 H/s (125.02ms) @ Accel:16 Loops:15 Thr:256 Vec:1

Hashmode: 6241 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit + boot-mode (Iterations: 1000)

Speed.#1.........:   937.3 kH/s (60.53ms) @ Accel:64 Loops:62 Thr:256 Vec:1

Hashmode: 6242 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit + boot-mode (Iterations: 1000)

Speed.#1.........:   304.0 kH/s (56.44ms) @ Accel:64 Loops:31 Thr:256 Vec:1

Hashmode: 6243 - TrueCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit + boot-mode (Iterations: 1000)

Speed.#1.........:   223.4 kH/s (80.65ms) @ Accel:64 Loops:31 Thr:256 Vec:1

Hashmode: 6300 - AIX {smd5} (Iterations: 1000)

Speed.#1.........: 19336.5 kH/s (50.69ms) @ Accel:1024 Loops:500 Thr:32 Vec:1

Hashmode: 6400 - AIX {ssha256} (Iterations: 64)

Speed.#1.........: 27698.5 kH/s (57.45ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 6500 - AIX {ssha512} (Iterations: 64)

Speed.#1.........: 11762.0 kH/s (88.12ms) @ Accel:64 Loops:64 Thr:256 Vec:1

Hashmode: 6600 - 1Password, agilekeychain (Iterations: 1000)

Speed.#1.........:  6048.7 kH/s (49.18ms) @ Accel:128 Loops:125 Thr:256 Vec:1

Hashmode: 6700 - AIX {ssha1} (Iterations: 64)

Speed.#1.........: 43323.8 kH/s (25.21ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 6800 - LastPass + LastPass sniffed (Iterations: 500)

Speed.#1.........:  5281.1 kH/s (49.98ms) @ Accel:128 Loops:62 Thr:256 Vec:1

Hashmode: 6900 - GOST R 34.11-94

Speed.#1.........:   734.4 MH/s (56.77ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 7000 - FortiGate (FortiOS)

Speed.#1.........: 13739.5 MH/s (96.74ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 7100 - macOS v10.8+ (PBKDF2-SHA512) (Iterations: 35000)

Speed.#1.........:    26838 H/s (88.24ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 7200 - GRUB 2 (Iterations: 10000)

Speed.#1.........:    93948 H/s (88.24ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 7300 - IPMI2 RAKP HMAC-SHA1

Speed.#1.........:  3077.9 MH/s (53.95ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 7400 - sha256crypt $5$, SHA256 (Unix) (Iterations: 5000)

Speed.#1.........:  1036.0 kH/s (61.79ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7500 - Kerberos 5 AS-REQ Pre-Auth etype 23

Speed.#1.........:   996.7 MH/s (83.70ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 7700 - SAP CODVN B (BCODE)

Speed.#1.........:  4231.8 MH/s (78.51ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7701 - SAP CODVN B (BCODE) mangled from RFC_READ_TABLE

Speed.#1.........:  4490.6 MH/s (73.98ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7800 - SAP CODVN F/G (PASSCODE)

Speed.#1.........:  2434.1 MH/s (68.25ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 7801 - SAP CODVN F/G (PASSCODE) mangled from RFC_READ_TABLE

Speed.#1.........:  3713.4 MH/s (89.50ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 7900 - Drupal7 (Iterations: 16384)

Speed.#1.........:   128.2 kH/s (79.09ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 8000 - Sybase ASE

Speed.#1.........:   912.8 MH/s (91.18ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 8100 - Citrix NetScaler

Speed.#1.........: 14426.8 MH/s (92.13ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 8200 - 1Password, cloudkeychain (Iterations: 40000)

Speed.#1.........:    25474 H/s (80.92ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 8300 - DNSSEC (NSEC3)

Speed.#1.........:  6364.4 MH/s (52.17ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 8400 - WBB3 (Woltlab Burning Board)

Speed.#1.........:  2426.7 MH/s (68.45ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 8500 - RACF

Speed.#1.........:  6203.7 MH/s (53.53ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 8600 - Lotus Notes/Domino 5

Speed.#1.........:   705.9 MH/s (59.06ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 8700 - Lotus Notes/Domino 6

Speed.#1.........:   229.3 MH/s (90.96ms) @ Accel:64 Loops:16 Thr:256 Vec:1

Hashmode: 8800 - Android FDE <= 4.3 (Iterations: 2000)

Speed.#1.........:  1626.5 kH/s (48.84ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 8900 - scrypt (Iterations: 1)

Speed.#1.........:  1124.3 kH/s (14.34ms) @ Accel:16 Loops:1 Thr:16 Vec:1

Hashmode: 9000 - Password Safe v2 (Iterations: 1000)

Speed.#1.........:  1119.0 kH/s (46.33ms) @ Accel:512 Loops:250 Thr:8 Vec:1

Hashmode: 9100 - Lotus Notes/Domino 8 (Iterations: 5000)

Speed.#1.........:  1306.5 kH/s (49.02ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 9200 - Cisco-IOS $8$ (PBKDF2-SHA256) (Iterations: 20000)

Speed.#1.........:   144.5 kH/s (57.43ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 9300 - Cisco-IOS $9$ (scrypt) (Iterations: 1)

Speed.#1.........:    55680 H/s (129.88ms) @ Accel:16 Loops:1 Thr:8 Vec:1

Hashmode: 9400 - MS Office 2007 (Iterations: 50000)

Speed.#1.........:   267.1 kH/s (49.78ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 9500 - MS Office 2010 (Iterations: 100000)

Speed.#1.........:   133.5 kH/s (49.78ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 9600 - MS Office 2013 (Iterations: 100000)

Speed.#1.........:    21124 H/s (78.63ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 9700 - MS Office <= 2003 $0/$1, MD5 + RC4

Speed.#1.........:   833.9 MH/s (50.08ms) @ Accel:128 Loops:64 Thr:64 Vec:1

Hashmode: 9710 - MS Office <= 2003 $0/$1, MD5 + RC4, collider #1

Speed.#1.........:  1155.3 MH/s (68.02ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 9720 - MS Office <= 2003 $0/$1, MD5 + RC4, collider #2

Speed.#1.........:  4487.1 MH/s (74.15ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 9800 - MS Office <= 2003 $3/$4, SHA1 + RC4

Speed.#1.........:  1031.3 MH/s (80.93ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 9810 - MS Office <= 2003 $3, SHA1 + RC4, collider #1

Speed.#1.........:  1225.3 MH/s (63.83ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 9820 - MS Office <= 2003 $3, SHA1 + RC4, collider #2

Speed.#1.........:  6773.6 MH/s (49.06ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 9900 - Radmin2

Speed.#1.........: 19579.9 MH/s (67.85ms) @ Accel:128 Loops:512 Thr:256 Vec:4

Hashmode: 10000 - Django (PBKDF2-SHA256) (Iterations: 20000)

Speed.#1.........:   144.6 kH/s (57.40ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 10100 - SipHash

Speed.#1.........: 60675.1 MH/s (43.74ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 10200 - CRAM-MD5

Speed.#1.........:  8709.9 MH/s (76.25ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 10300 - SAP CODVN H (PWDSALTEDHASH) iSSHA-1 (Iterations: 1023)

Speed.#1.........: 10208.4 kH/s (44.22ms) @ Accel:128 Loops:255 Thr:256 Vec:1

Hashmode: 10400 - PDF 1.1 - 1.3 (Acrobat 2 - 4)

Speed.#1.........:  1285.9 MH/s (64.80ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 10410 - PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #1

Speed.#1.........:  1325.6 MH/s (58.70ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 10420 - PDF 1.1 - 1.3 (Acrobat 2 - 4), collider #2

Speed.#1.........: 16631.2 MH/s (79.86ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 10500 - PDF 1.4 - 1.6 (Acrobat 5 - 8) (Iterations: 70)

Speed.#1.........: 33604.0 kH/s (42.84ms) @ Accel:512 Loops:70 Thr:64 Vec:1

Hashmode: 10600 - PDF 1.7 Level 3 (Acrobat 9)

Speed.#1.........:  7628.1 MH/s (87.28ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 10700 - PDF 1.7 Level 8 (Acrobat 10 - 11) (Iterations: 64)

Speed.#1.........:    75446 H/s (135.51ms) @ Accel:16 Loops:2 Thr:256 Vec:1

Hashmode: 10800 - SHA2-384

Speed.#1.........:  2300.2 MH/s (72.17ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 10900 - PBKDF2-HMAC-SHA256 (Iterations: 999)

Speed.#1.........:  2792.8 kH/s (52.81ms) @ Accel:128 Loops:62 Thr:256 Vec:1

Hashmode: 11000 - PrestaShop

Speed.#1.........: 19349.4 MH/s (68.65ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 11100 - PostgreSQL CRAM (MD5)

Speed.#1.........: 15540.0 MH/s (85.51ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 11200 - MySQL CRAM (SHA1)

Speed.#1.........:  4359.4 MH/s (76.18ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 11300 - Bitcoin/Litecoin wallet.dat (Iterations: 199999)

Speed.#1.........:    10557 H/s (78.61ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 11400 - SIP digest authentication (MD5)

Speed.#1.........:  7493.8 MH/s (88.65ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 11500 - CRC32

Speed.#1.........: 13358.5 MH/s (49.67ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 11600 - 7-Zip (Iterations: 524288)

Speed.#1.........:    20552 H/s (61.51ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 11700 - GOST R 34.11-2012 (Streebog) 256-bit, big-endian

Speed.#1.........:   165.6 MH/s (63.07ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 11750 - HMAC-Streebog-256 (key = $pass), big-endian

Speed.#1.........: 56250.5 kH/s (92.86ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 11760 - HMAC-Streebog-256 (key = $salt), big-endian

Speed.#1.........: 78082.4 kH/s (66.86ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 11800 - GOST R 34.11-2012 (Streebog) 512-bit, big-endian

Speed.#1.........:   165.5 MH/s (63.08ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 11850 - HMAC-Streebog-512 (key = $pass), big-endian

Speed.#1.........: 48179.0 kH/s (54.21ms) @ Accel:16 Loops:8 Thr:256 Vec:1

Hashmode: 11860 - HMAC-Streebog-512 (key = $salt), big-endian

Speed.#1.........: 65156.9 kH/s (80.14ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 11900 - PBKDF2-HMAC-MD5 (Iterations: 999)

Speed.#1.........: 14577.4 kH/s (47.44ms) @ Accel:128 Loops:499 Thr:256 Vec:1

Hashmode: 12000 - PBKDF2-HMAC-SHA1 (Iterations: 999)

Speed.#1.........:  6031.6 kH/s (43.80ms) @ Accel:128 Loops:124 Thr:256 Vec:1

Hashmode: 12001 - Atlassian (PBKDF2-HMAC-SHA1) (Iterations: 9999)

Speed.#1.........:   660.6 kH/s (49.66ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 12100 - PBKDF2-HMAC-SHA512 (Iterations: 999)

Speed.#1.........:   933.0 kH/s (81.15ms) @ Accel:64 Loops:62 Thr:256 Vec:1

Hashmode: 12200 - eCryptfs (Iterations: 65535)

Speed.#1.........:    32227 H/s (78.60ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 12300 - Oracle T: Type (Oracle 12+) (Iterations: 4095)

Speed.#1.........:   248.6 kH/s (80.91ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 12400 - BSDi Crypt, Extended DES (Iterations: 2899)

Speed.#1.........:  4688.3 kH/s (84.98ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 12500 - RAR3-hp (Iterations: 262144)

Speed.#1.........:    82415 H/s (61.93ms) @ Accel:4 Loops:16384 Thr:256 Vec:1

Hashmode: 12600 - ColdFusion 10+

Speed.#1.........:  4136.1 MH/s (80.30ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 12700 - Blockchain, My Wallet (Iterations: 10)

Speed.#1.........: 52369.1 kH/s (7.91ms) @ Accel:128 Loops:10 Thr:256 Vec:1

Hashmode: 12800 - MS-AzureSync PBKDF2-HMAC-SHA256 (Iterations: 99)

Speed.#1.........: 20093.4 kH/s (88.61ms) @ Accel:128 Loops:99 Thr:256 Vec:1

Hashmode: 12900 - Android FDE (Samsung DEK) (Iterations: 4095)

Speed.#1.........:   705.0 kH/s (57.40ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 13000 - RAR5 (Iterations: 32767)

Speed.#1.........:    88209 H/s (57.42ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 13100 - Kerberos 5 TGS-REP etype 23

Speed.#1.........:   996.0 MH/s (83.71ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 13200 - AxCrypt (Iterations: 10000)

Speed.#1.........:   259.3 kH/s (64.08ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 13300 - AxCrypt in-memory SHA1

Speed.#1.........: 15460.2 MH/s (85.94ms) @ Accel:128 Loops:512 Thr:256 Vec:4

Hashmode: 13400 - KeePass 1 (AES/Twofish) and KeePass 2 (AES) (Iterations: 6000)

Speed.#1.........:   355.5 kH/s (77.86ms) @ Accel:512 Loops:128 Thr:32 Vec:1

Hashmode: 13500 - PeopleSoft PS_TOKEN

Speed.#1.........:  6181.9 MH/s (53.78ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 13600 - WinZip (Iterations: 1000)

Speed.#1.........:  2134.8 kH/s (69.40ms) @ Accel:128 Loops:62 Thr:256 Vec:1

Hashmode: 13711 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit (Iterations: 655331)

Speed.#1.........:     1890 H/s (66.39ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13712 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit (Iterations: 655331)

Speed.#1.........:     1060 H/s (59.62ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13713 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit (Iterations: 655331)

Speed.#1.........:      734 H/s (84.57ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13721 - VeraCrypt PBKDF2-HMAC-SHA512 + XTS 512 bit (Iterations: 500000)

Speed.#1.........:     1875 H/s (88.23ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13722 - VeraCrypt PBKDF2-HMAC-SHA512 + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:     1050 H/s (79.23ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13723 - VeraCrypt PBKDF2-HMAC-SHA512 + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:      697 H/s (59.57ms) @ Accel:64 Loops:16 Thr:256 Vec:1

Hashmode: 13731 - VeraCrypt PBKDF2-HMAC-Whirlpool + XTS 512 bit (Iterations: 500000)

Speed.#1.........:      236 H/s (176.18ms) @ Accel:64 Loops:16 Thr:256 Vec:1

Hashmode: 13732 - VeraCrypt PBKDF2-HMAC-Whirlpool + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:      118 H/s (177.16ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 13733 - VeraCrypt PBKDF2-HMAC-Whirlpool + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:       78 H/s (133.43ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 13741 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 512 bit + boot-mode (Iterations: 327661)

Speed.#1.........:     3783 H/s (66.35ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13742 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1024 bit + boot-mode (Iterations: 327661)

Speed.#1.........:     2119 H/s (59.63ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13743 - VeraCrypt PBKDF2-HMAC-RIPEMD160 + XTS 1536 bit + boot-mode (Iterations: 327661)

Speed.#1.........:     1468 H/s (84.53ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13751 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 512 bit (Iterations: 500000)

Speed.#1.........:     2728 H/s (60.67ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13752 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:     1355 H/s (61.24ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13753 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:      895 H/s (91.66ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13761 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 512 bit + boot-mode (Iterations: 200000)

Speed.#1.........:     6819 H/s (60.68ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 13762 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1024 bit + boot-mode (Iterations: 200000)

Speed.#1.........:     3389 H/s (61.23ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 13763 - VeraCrypt PBKDF2-HMAC-SHA256 + XTS 1536 bit + boot-mode (Iterations: 200000)

Speed.#1.........:     2235 H/s (91.68ms) @ Accel:128 Loops:16 Thr:256 Vec:1

Hashmode: 13771 - VeraCrypt PBKDF2-HMAC-Streebog-512 + XTS 512 bit (Iterations: 500000)

Speed.#1.........:      103 H/s (201.36ms) @ Accel:32 Loops:16 Thr:256 Vec:1

Hashmode: 13772 - VeraCrypt PBKDF2-HMAC-Streebog-512 + XTS 1024 bit (Iterations: 500000)

Speed.#1.........:       49 H/s (211.82ms) @ Accel:32 Loops:8 Thr:256 Vec:1

Hashmode: 13773 - VeraCrypt PBKDF2-HMAC-Streebog-512 + XTS 1536 bit (Iterations: 500000)

Speed.#1.........:       33 H/s (159.75ms) @ Accel:16 Loops:8 Thr:256 Vec:1

Hashmode: 13800 - Windows Phone 8+ PIN/password

Speed.#1.........:  1871.9 MH/s (44.36ms) @ Accel:128 Loops:32 Thr:256 Vec:2

Hashmode: 13900 - OpenCart

Speed.#1.........:  4003.5 MH/s (82.95ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 14000 - DES (PT = $salt, key = $pass)

Speed.#1.........: 42806.7 MH/s (62.01ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 14100 - 3DES (PT = $salt, key = $pass)

Speed.#1.........:  2249.0 MH/s (74.40ms) @ Accel:8 Loops:1024 Thr:256 Vec:1

Hashmode: 14400 - sha1(CX)

Speed.#1.........:   728.8 MH/s (57.15ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 14600 - LUKS (Iterations: 163044)

Speed.#1.........:    19236 H/s (12.66ms) @ Accel:2 Loops:1024 Thr:256 Vec:1

Hashmode: 14700 - iTunes backup < 10.0 (Iterations: 9999)

Speed.#1.........:   331.6 kH/s (50.02ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 14800 - iTunes backup >= 10.0 (Iterations: 9999999)

Speed.#1.........:      285 H/s (3.53ms) @ Accel:2 Loops:250 Thr:256 Vec:1

Hashmode: 14900 - Skip32 (PT = $salt, key = $pass)

Speed.#1.........: 15579.0 MH/s (2.06ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 15000 - FileZilla Server >= 0.9.55

Speed.#1.........:  2469.5 MH/s (67.21ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15100 - Juniper/NetBSD sha1crypt (Iterations: 19999)

Speed.#1.........:   335.7 kH/s (49.50ms) @ Accel:128 Loops:128 Thr:256 Vec:1

Hashmode: 15200 - Blockchain, My Wallet, V2 (Iterations: 5000)

Speed.#1.........:   663.4 kH/s (49.41ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15300 - DPAPI masterkey file v1 (Iterations: 23999)

Speed.#1.........:   137.9 kH/s (50.09ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15400 - ChaCha20

Speed.#1.........:  8299.9 MH/s (80.03ms) @ Accel:128 Loops:256 Thr:256 Vec:1

Hashmode: 15500 - JKS Java Key Store Private Keys (SHA1)

Speed.#1.........: 16249.5 MH/s (81.51ms) @ Accel:128 Loops:512 Thr:256 Vec:1

Hashmode: 15600 - Ethereum Wallet, PBKDF2-HMAC-SHA256 (Iterations: 262143)

Speed.#1.........:    11038 H/s (57.35ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 15700 - Ethereum Wallet, SCRYPT (Iterations: 1)

Speed.#1.........:        6 H/s (8191.29ms) @ Accel:1 Loops:1 Thr:1 Vec:1

Hashmode: 15900 - DPAPI masterkey file v2 (Iterations: 7999)

Speed.#1.........:   119.2 kH/s (87.52ms) @ Accel:256 Loops:128 Thr:32 Vec:1

Hashmode: 16000 - Tripcode

Speed.#1.........:   570.4 MH/s (73.06ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 16100 - TACACS+

Speed.#1.........: 30655.7 MH/s (86.68ms) @ Accel:128 Loops:1024 Thr:256 Vec:1

Hashmode: 16200 - Apple Secure Notes (Iterations: 19999)

Speed.#1.........:   144.1 kH/s (57.57ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16300 - Ethereum Pre-Sale Wallet, PBKDF2-HMAC-SHA256 (Iterations: 1999)

Speed.#1.........:  1417.4 kH/s (55.99ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16400 - CRAM-MD5 Dovecot

Speed.#1.........: 55057.8 MH/s (48.20ms) @ Accel:128 Loops:1024 Thr:256 Vec:4

Hashmode: 16500 - JWT (JSON Web Token)

Speed.#1.........:  1286.0 MH/s (64.53ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 16600 - Electrum Wallet (Salt-Type 1-3)

Speed.#1.........:   562.8 MH/s (74.06ms) @ Accel:64 Loops:32 Thr:256 Vec:1

Hashmode: 16700 - FileVault 2 (Iterations: 19999)

Speed.#1.........:   144.1 kH/s (57.56ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16800 - WPA-PMKID-PBKDF2 (Iterations: 4096)

Speed.#1.........:   807.6 kH/s (50.00ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 16801 - WPA-PMKID-PMK (Iterations: 1)

Speed.#1.........: 54824.0 kH/s (0.02ms) @ Accel:128 Loops:1 Thr:256 Vec:1

Hashmode: 16900 - Ansible Vault (Iterations: 9999)

Speed.#1.........:   289.2 kH/s (57.39ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 17300 - SHA3-224

Speed.#1.........:  1717.7 MH/s (48.28ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17400 - SHA3-256

Speed.#1.........:  1712.5 MH/s (48.43ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17500 - SHA3-384

Speed.#1.........:  1712.9 MH/s (48.41ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17600 - SHA3-512

Speed.#1.........:  1714.0 MH/s (48.39ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17700 - Keccak-224

Speed.#1.........:  1718.1 MH/s (48.28ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17800 - Keccak-256

Speed.#1.........:  1712.6 MH/s (48.43ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 17900 - Keccak-384

Speed.#1.........:  1713.5 MH/s (48.40ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 18000 - Keccak-512

Speed.#1.........:  1714.3 MH/s (48.38ms) @ Accel:128 Loops:32 Thr:256 Vec:1

Hashmode: 18100 - TOTP (HMAC-SHA1)

Speed.#1.........:  2783.4 MH/s (59.63ms) @ Accel:128 Loops:64 Thr:256 Vec:1

Hashmode: 18200 - Kerberos 5 AS-REP etype 23

Speed.#1.........:   989.5 MH/s (84.27ms) @ Accel:256 Loops:64 Thr:64 Vec:1

Hashmode: 18300 - Apple File System (APFS) (Iterations: 19999)

Speed.#1.........:   144.2 kH/s (57.53ms) @ Accel:128 Loops:64 Thr:256 Vec:1
