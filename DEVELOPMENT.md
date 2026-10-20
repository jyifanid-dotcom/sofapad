> Source paths and workflows described here refer to the complete source ZIP. Online code directories are not yet expanded.

# 开发、测试与构建

## 实际技术栈

- Mac：Python3标准库、ctypes调用CoreGraphics/CoreFoundation、WebSocket/HTTP接收与配对。
- Android：Java17、BluetoothHidDevice、WebView本地共享资产、Camera及ZXing离线扫码。
- 共享前端：HTML/CSS/JavaScript；同一app-ui.js用于网页、APK局域网和蓝牙界面。
- 工业图：独立ReportLab矢量脚本，仅用于概念设计，不是运行时依赖。

当前不是Rust实现。普通用户下载预编译包即可，不需Android开发环境。

## 同步共享页面

修改trackpad.py中的PAGE或共享脚本后，从仓库根目录运行：

```bash
python3 -B android-apk/tools/sync_page.py
python3 -B android-apk/tools/check_project.py
node android-apk/tools/check_page.cjs
node android-apk/tools/check_reconnect.cjs
```

sync_page使用AST提取页面，不导入/执行Mac接收端；可在其他系统做静态页面整理。完整输入接收仅在Mac运行。

## Android构建

需要JDK17、Android SDK35和Gradle8.11.1，Android源码目录为android-apk/。仓库保留纯Java/模拟框架检查，mock不发送真实Mac输入。

```bash
cd android-apk
gradle --no-daemon :app:assembleDebug :app:lintDebug
```

仓库根目录的.github/workflows/android.yml提供手动GitHub Actions构建；它安装官方工具、检查、构建/签名验证并返回Artifacts。**只有真实运行成功才生成cloud_receipt；仓库首次发布不代表云构建已经通过。**

云构建使用runner的临时debug签名，不含本地发行测试私钥，不能保证直接覆盖releases内同签名测试包。需稳定分发时自行配置受保护签名流程；不要提交keystore、令牌或密码。

测试程序中的地址、触点及文本均为合成样例，不含个人设备记录。

## 测试层级

- check_project.py：权限、页面来源/哈希、资源与打包范围。
- check_page.cjs / check_reconnect.cjs：实际脚本在模拟DOM/输出下的触点、输入、状态清理与重连。
- EngineCheck.java：手势/HID报告/相对运动/输入镜像等纯Java检查。
- check_bluetooth_lifecycle.py、check_remote_input.py：fake framework生命周期/输入测试，不代表真实蓝牙已通。
- check_receiver.py、check_native_magnify.py、check_lan_transport.py、check_connection_recovery.py等有各自范围；需要的OS/工具见参数与源码。不要在不清楚输出隔离的情况下对正在使用的电脑发真实输入。

仓库保留测试程序，不附带本地运行日志、设备信息或输入记录。请在自己的环境运行相关检查；模拟测试不能代替实机验证。

## 复现媒体

`docs/demo/index.html`是从实际PAGE与共享UI生成的隔离演示，WebSocket替换为内存收集，CSP禁止连接。可用本地静态服务器打开；不用于配对或控制电脑。数字键1/2/3/4切换主界面、输入、手感、连接，g播放一次示例触点。不要把演示页直接当生产入口。

README的GIF由这些实际界面状态的浏览器截图编码为动图，不是AI生成的软件截图，也不是端到端性能录像。媒体来源见docs/assets/README.md。
