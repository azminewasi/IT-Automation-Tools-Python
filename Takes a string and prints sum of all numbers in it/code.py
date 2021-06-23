#include <stdio.h>
#include <iostream>


using namespace std;


int findSum(string str)
{

	string temp = "";


	long long int sum = 0;


	for (char ch: str)
	{

		if (isdigit(ch))
			temp += ch;

		else
		{

			sum += atoi(temp.c_str());
			temp = "";
		}
	}

	return sum + atoi(temp.c_str());
}

int main()
{
	char str [100000];

scanf(" %[^\n]s",str);
	cout << findSum(str);

	return 0;
}
