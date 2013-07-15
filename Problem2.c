#include<stdio.h>

long fibonacci(long);

int main(void){
	long n = 1, sum = 0, f;
	while((f = fibonacci(n))<4000000){
		if(f%2 == 0) sum += f;
		n++;
	}
	printf("sum = %ld\n", sum);

	return 0;
}

long fibonacci(long n){
	if(n == 1)	return 1;
	else if(n == 2)	return 2;
	else	return fibonacci(n-1) + fibonacci(n-2);
}