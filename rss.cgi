#!/usr/bin/perl

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
