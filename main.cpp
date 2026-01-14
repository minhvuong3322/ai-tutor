#define UNICODE
#include <iostream>
#include <windows.h>
#include <io.h>
#include <fcntl.h>

using namespace std;

int main() {
    // Xuất nhập tiếng Việt
    _setmode(_fileno(stdin), _O_U16TEXT);
    _setmode(_fileno(stdout), _O_U16TEXT);

    // 1. Khởi động Flask server ngầm
    wcout << L"Đang khởi chạy Flask server...\n";
    ShellExecute(NULL, L"open", L"cmd.exe", L"/c cd Server && python api.py", NULL, SW_SHOW);

    // 2. Đợi 3 giây để server khởi động
    Sleep(3000);

    // 3. Chạy Electron ngầm
    wcout << L"Đang khởi chạy Electron app...\n";
    ShellExecute(NULL, L"open", L"cmd.exe", L"/c cd Client && npm run start", NULL, SW_HIDE);

    wcout << L"✅ Tất cả đã khởi động.\n";
    cin.get();
    return 0;
}
