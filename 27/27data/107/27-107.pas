##
Assign( input, '27-107b.txt' );
var N := ReadInteger;
var pairs := 
  N.Range.Select( n->(ReadInteger, ReadInteger) ).ToArray
         .OrderBy( \(s,f)->f );

var lastPos := -1;
var count := 0;

foreach var p in pairs do
  if p[0] > lastPos then begin
    lastPos := p[1];
    count += 1
  end;

Println( count )