## uses school;

{Вычисление попарных сум из двух списков} 
function CombineLists(L1, L2: list<integer>): List<integer>;
begin
  var Res := new List<integer>; 
  foreach var i in L1 do 
    foreach var j in L2 do 
      Res.Add(i + j); 
  Result := Res; 
end;

Assign(input, '27-77b.txt'); 
var N := ReadlnInteger; 

var base := 35; 
var D := new Dictionary<integer, integer>; 

var L := new List<integer>; 
L.Add(0); 

var HOK := new List<integer>; 

for var i := 1 to N do begin
  var data := ReadlnString.ToIntegers[1:]; 

  HOK.Clear; 
  for var j := 0 to data.Length - 2 do 
    for var k := j + 1 to data.Length - 1 do 
      HOK.Add( LCM(data[j], data[k]) );   

  L := CombineLists( L, HOK );
  L.Sort;

  D.Clear;
  foreach var x in L do D[x mod base] := x;

  L.Clear; 
  foreach var p in D do L.Add( p.Value ); 

end; 

L.Where( x -> (x mod 5 = 0) xor (x mod 7 = 0) ).Max.Println;
