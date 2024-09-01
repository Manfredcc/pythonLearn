#include <windows.h>  
  
int WINAPI WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, PSTR szCmdLine, int iCmdShow) {  
    // 调用MessageBox函数来显示一个消息框  
    MessageBox(NULL, "It's time to take a rest", "Olivia:", MB_OK | MB_ICONINFORMATION);  
  
    // 实际上，对于仅显示一个消息框的程序，这里不需要创建主窗口或消息循环  
    // 但为了符合WinMain的标准结构，你可以简单地返回0  
    return 0;  
}