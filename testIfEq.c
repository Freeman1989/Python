//测试相同的宏定义判断时是否相等

#include <stdio.h>

#define RETURN_OK 1
#define CCDB_OK 1

int main(void)
{
    if (RETURN_OK == CCDB_OK)
	printf("It is equal.\n");
    else
	printf("It is not equal.\n");

    return 0;
}
