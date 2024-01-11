#include<iostream>
using namespace std;
int main()
{
    int num,rem,num2=0;
    string arr[10]={"zero","one","two","three","four","five","six","seven","eight","nine"};
    cout<<"ENTER THE NUMBER:";
    cin>>num;
    while(num!=0){
        rem=num%10;
        num2=num2*10+rem;
        num=num/10;
    }
    while(num2!=0){
        rem=num2%10;
        num2=num2/10;
        cout<<arr[rem]<<" ";

    }
}

