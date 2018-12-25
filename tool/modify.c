#include <windows.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    if(argc == 1) {
        puts("filename can't be null");
        return 1;
    }
    char *filename = argv[1];
    printf("filename=%s\n", filename);
    LARGE_INTEGER size;
    DWORD error;
    HANDLE handle;
    handle = CreateFileA(
        filename,
        GENERIC_READ | GENERIC_WRITE, 0, NULL,
        OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, NULL);
    if (!handle)
    {
        printf("open file failed, %d\n", GetLastError());
        return 1;
    }
    GetFileSizeEx(handle, &size);
    HANDLE mapping = CreateFileMappingA(handle, NULL, PAGE_READWRITE, 0, 0, NULL);
    if (!mapping)
    {
        printf("create mapping failed, %d\n", GetLastError());
        return 1;
    }
    // MapViewOfFile()
    char *p = (char *)MapViewOfFile(mapping, FILE_MAP_ALL_ACCESS, 0, 0, 0);
    for (int i = 0; i < size.QuadPart; i++)
    {
        p[i] = ~p[i]; 
    }
    UnmapViewOfFile(mapping);
    CloseHandle(handle);
    return 0;
}