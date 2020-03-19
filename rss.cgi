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

my @Files;
@Files = glob("markdowns/*.md");

print "Content-type: application/rss+xml\n\n";
@Files = reverse @Files;

print "<rss xmlns:atom='http://www.w3.org/2005/Atom' version='2.0'>\n";
print "<channel>
    <title>your blog</title>
    <link>https://your url</link>
    <description>blog</description>\n";

foreach(@Files) {
    my $Title = &GetTitle($_);
    my $Description = &GetDescription($_);
    my $Link = $_;
   
    $Link =~ s/markdowns\///g;
    my $Date = $Link; $Date =~ s/.md//g;
    print "<item>";
    
    print "<title>".$Title."</title>\n";
    print "<author>you</author>";
    print "<link>"."https:/yourwebsite/cleg/?article=$Link"."</link>\n";
    print "<description>".&GetDescription($_) . "</description>\n";
    print "</item>\n\n";
}

print "</channel>\n\n</rss>";

# Subroutines

sub GetDescription {
    my $File = shift;
    my @Lines = &ReadLines($File);
    
    return $Lines[2] . $Lines[4];  
}

sub GetTitle {
    my $File = shift;
    my @Lines = &ReadLines($File);
    my $Title;
    
    foreach(@Lines) {
        if($_ =~ /^# /) {
            $Title = $_;
	    $Title =~ s/# //;
        }
    }
    return $Title;
}

sub ReadLines {
    my $File = shift;
    my $Content;
    open (FILE, "<:encoding(utf8)", $File);
    local $/ = undef;
    $Content = <FILE>;
    close FILE;
    return split /\n/, $Content;
}
