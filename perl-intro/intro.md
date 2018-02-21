# Introduction to Perl
{id: introduction-to-perl}

## First script
{id: first-perl-script}

![](examples/hello_world.pl)

* #!/usr/bin/env perl  - Path to perl interpreter
* use v5.10;           - Minimal version number of Perl, turn on new features.
* use strict;          - Require variable declarations, avoid stupid mistakes.
* use warnigs;         - Ask for warnings. Avoid further stupid mistakes. 

* say                  - print with newline at the end

## print vs. say
{id: print-vs-say}

* say   - (since perl 5.10) newline at the end
* print - (always)
* print "...\n";    - add the newline

## Scalar values
{id: scalar-values}

"A string"

'Another string'

23

23.45

## Lists
{id: perl-lists}

('string', 42, 2.3)

## Hash
{id: perl-hash}

(
    'name'  => 'Foo Bar',
    'email' => 'foo@bar.com',
) 


## Functions
{id: perl-functions}

sub greeting {
    say 'Hello World';
}


## Variable declaration
{id: variable-declaration}

my $name;
$name = 'Foo Bar';

my $email = 'foo@bar.com';

## Sigils
{id: sigils}

* $ - scalars
* @ - arrays
* % - hashes
* & - functions

## Arrays
{id: arrays}

my @names = ('Foo', 'Bar', 'Moo');
say $names[0];

scalar @names;      # number of elements in the array
$#names;            # the largest index (one less than number of elements)

push @names, 'Minimacko';
pop @names;
shift @names;
unshift @names, 'Malacka';

## Hashes
{id: hashes}

my %phone = (
    'Foo' => '01-23456',
    'Bar' => '98-76543',
);
say $phone{'Foo'};
$phone{'Zorg'} = '999'

for (my $name keys %phone) {
    say "$name $phone{$name}";
}


## IO
{id: io}

## Control structures (if, else, elsif)
{id: control-structures}


## Loops (for, foreach, while)
{id: loops}


## C-style for loop
{id: c-style-for-loop}

Possible, but not recommended in Perl.


## CPAN
{id: cpan}

* [CPAN](https://www.cpan.org/)
* [sco](http://search.cpan.org/) old, but well indexed by Google
* [Meta::CPAN](https://metacpan.org/) new, maintaned, open source
* mcpan - search.mcpan.org

## Database access
{id: database-access}

* [DBI](https://metacpan.org/pod/DBI)
* [DBD::SQLite]
