const { app, BrowserWindow } = require("electron");
const path = require("path");

function createWindow() {
  const win = new BrowserWindow({
    icon: path.join(__dirname, "UTH.png"),
    show: false, // Ẩn lúc khởi tạo để tránh nhấp nháy
    webPreferences: {
      nodeIntegration: true,
    },
  });

  win.maximize(); // Mở full màn hình theo độ phân giải hiện tại
  win.show(); // Hiển thị sau khi đã maximize
  win.setMenuBarVisibility(false);

  win.loadFile("index.html");
}

app.whenReady().then(createWindow);
