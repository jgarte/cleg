#!/usr/bin/perl

# This file is part of cleg.

# cleg is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# cleg is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with cleg.  If not, see <https://www.gnu.org/licenses/>.

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
