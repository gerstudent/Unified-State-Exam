#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
using namespace std;

int main()
{
	int N, K, V;
	vector<int> pos;
	vector<int> vol;
	ifstream F;
	F.open("27-123b.txt");
	F >> N >> K >> V;
	for( int i=0; i<N; i++ ) {
	  int p, v;	
	  F >> p >> v;
	  if ( v % V == 0 ) 
	       v = v / V;  	
	  else v = v / V + 1;   
	  pos.push_back(p);
	  vol.push_back(v);
	  }
	F.close();
	  
	long long bestPos, minCost = -1;
	for( int i=0; i<N; i++ ) {
	  int pos1 = pos[i];
	  long long cost = 0;
	  for( int j=0; j<N; j++ ) {
	  	int pos2 = pos[j];
		int v = vol[j];
		int dist = min( abs(pos1-pos2), K-abs(pos1-pos2) );   
		cost += dist*v;
	    }
	  if( minCost < 0 or cost < minCost ) {
	  	minCost = cost;
	  	bestPos = pos1;
	  	// cout << bestPos << " " << minCost << endl;
	    }
	} 
	
   cout << bestPos << " " << minCost; 	
}
