#include <iostream>
using namespace std;
int main()
{
    int a[2000];
    int n;
    cout<<"Nhap so giai thua: ";cin>>n;
    a[0]=1;
    int i=0,carry=0,k=0;
    for(int j=2;j<=n;j++)
    {
        for(int i=0;i<=k;i++)
        {
            a[i]=a[i]*j+carry;
            carry=a[i]/10;
            a[i]=a[i]%10;            
        }
        while(carry) { //Propogate the remaining carry to higher order digits
            k++;
            a[k] = carry % 10;
            carry /= 10;
        }   
    }
    for(int i=k;i>=0;i--) cout<<a[i];
}