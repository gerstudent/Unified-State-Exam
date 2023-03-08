##
Assign(input, '27-2022b.txt');
var N := ReadINteger;
var K := 43;
var tailSum := |0bi| + |-1bi|*(K-1);
var tailLen := |0|*K;
var (maxSum, minLen) := (0bi, 10**10);
var totalSum := 0bi;
for var i:=0 to N-1 do begin
  var x := ReadInteger;
  totalSum += x;
  if totalSum < 0 then
    Println( totalSum );
  var r := integer(totalSum mod K);
  if tailSum[r] <> -1 then begin
    var curSum := totalSum - tailSum[r];
    var curLen := i - tailLen[r] + 1;
    if (curSum > maxSum) or 
       ((curSum = maxSum) and (curLen < minLen)) then begin
      maxSum := curSum;
      minLen := curLen;
    end
  end else begin
    tailSum[r] := totalSum;
    tailLen[r] := i+1;
  end
end;
print( minLen );
