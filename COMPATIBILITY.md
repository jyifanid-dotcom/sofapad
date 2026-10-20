# 兼容性与测试边界

以下为平台要求和已知限制，具体型号仍需实机验证。

| 平台 / 设备 | 当前路径 | 状态与限制 |
|---|---|---|
| Android平板/手机 | APK局域网、浏览器；有条件支持APK蓝牙 | APK最低API28/Android9；蓝牙还依赖ROM开放HID Device |
| 华为兼容Android应用的平板 | APK及网页测试目标 | 需系统兼容Android应用并开放所需接口；蓝牙自动重连和长期稳定仍待验证 |
| iPhone | Safari或主屏幕网页 | 没有iOS原生App；输入、权限、全屏受浏览器限制 |
| iPad | Safari或主屏幕网页 | 包含旧版Safari兼容处理；老设备会话、重连、手感仍待验证 |
| Mac mini / MacBook /其他Mac | Python接收端 | 需Python3及辅助功能权限；macOS版本、外接显示器和目标应用会影响行为 |
| Kindle电子墨水阅读器 | 实验性设想 | 未进行本项目真机验证，不承诺网页API、多点触摸、刷新和手感 |
| Fire平板 | 可尝试Android/浏览器路径 | 与Kindle阅读器不是同类系统；本项目未逐型号验证 |
| Windows / Linux作为被控端 | 未提供 | 当前接收端绑定macOS系统框架 |

## 浏览器最低能力

实际页面使用JavaScript、WebSocket、Pointer Events或Touch Events、CSS自定义属性及相应布局能力；旧浏览器还可能缺少其他语法/样式能力。仅支持基础HTML、仅能打开一个网页、只有一个触点，不能推导出完整兼容。

- 单指输入至少需要可靠的坐标与按下/抬起事件。
- 双指以上手势需要真实多触点上报；电子墨水刷新还会影响视觉反馈。
- 浏览器软键盘、Cookie、主屏幕会话和后台挂起受系统控制。
- HTTP页面的一些可选浏览器能力可能因安全上下文要求受限，核心触控不依赖这些可选能力。

## 演示与使用范围

README中的GIF来自实际页面的模拟连接演示，不是实机延迟测试。客厅图和硬件外观图为AI生成，工业设计图为参数化概念图。

重连、蓝牙和连续缩放的实际效果受系统、设备与网络影响。Windows和Linux接收端目前未提供。

## 参考资料

- [MDN WebSocket API](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)：网页连接API的一般能力，不能替代具体Kindle型号验证。
- [Amazon Fire平板Web调试资料](https://developer.amazon.com/docs/fire-tablets/webapp-debug-app.html)：Fire是独立的平台路径，不能直接当作Kindle阅读器结论。
- [Apple Magic Trackpad](https://www.apple.com/shop/product/mxk93am/a/magic-trackpad-usb%E2%80%91c-white-multi-touch-surface)：原生设备包含Force Touch等硬件能力，本项目没有复制这些硬件。
