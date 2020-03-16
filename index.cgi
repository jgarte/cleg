#!/usr/bin/perl

use CGI;
use Text::Markdown 'markdown';

use strict;
use warnings;

my $q = CGI->new;
my $Article = $q->param("article");


print "Content-type: text/html\n\n";
print "<!DOCTYPE html>\n\n<html lang=\"en\">\n<head> <meta charset='utf-8'>\n<title>qorg1b1 clag</title>\n</head>\n<body>\n";

# Prototypes

sub MarkdownToHtml();

if(defined $Article) {
    print &MarkdownToHtml("markdowns/$Article");
    exit;
}


my @Contents;

opendir(DIRECTORY,"markdowns");

while(readdir(DIRECTORY)) {

    push @Contents, $_;

}
closedir(DIRECTORY);

@Contents = sort(@Contents);
@Contents = reverse(@Contents);
pop @Contents; pop @Contents;

my $Date;

foreach(@Contents) {
    $Date = $_;
    $Date =~ s/\.md//;
    print "Date: $Date";

    print &MarkdownToHtml("markdowns/$_");
    print "<a href='?article=$Date.md'>permalink</a>";
    print "<hr>";
}

print "\n</body>\n</html>\n";

sub MarkdownToHtml() {
    my $MDFile = shift;
    my @FileContents;
    open(FILE,$MDFile);
    while(<FILE>) {
        push @FileContents, markdown($_);
    }
    return @FileContents;
}
