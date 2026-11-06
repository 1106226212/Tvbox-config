# TVBox 通用合集配置

本目录包含 TVBox 通用合集配置文件，支持「接口配置」和「完整配置」两种方式。

## 📁 文件说明

| 文件 | 用途 |
|------|------|
| `box.json` | 核心配置文件（含 sites / lives / parses） |
| `tvbox-interface.json` | 接口配置直链文件（内容与 box.json 一致） |
| `tvbox-config.jar` | 完整配置 JAR 包（内含 box.json） |
| `build.py` | 构建脚本（可选保留） |

## 📊 配置内容

- **影视站点**: 27 个 CMS 接口
- **直播源**: 3 个直播频道
- **解析接口**: 0 个

## 🚀 上传 GitHub 获取 URL

### 方式一：GitHub 仓库（推荐）

1. 登录 [GitHub](https://github.com)，点击 **+ → New repository**
2. 仓库名建议填 `tvbox-config`，选 **Public**
3. 进入仓库，点击 **Add file → Upload files**
4. 把本目录下的 **全部文件** 拖进去上传
5. 上传完成后，你的文件直链格式如下（替换 `your-username`）：

   **接口配置 JSON URL：**
   ```
   https://raw.githubusercontent.com/your-username/tvbox-config/main/tvbox-interface.json
   ```

   **完整配置 JAR URL：**
   ```
   https://raw.githubusercontent.com/your-username/tvbox-config/main/tvbox-config.jar
   ```

   > 如果仓库默认分支是 `master`，把上面 URL 中的 `main` 改成 `master`

### 方式二：GitHub Gist（更简单）

1. 访问 [Gist](https://gist.github.com)，点击 **Create new gist**
2. 文件名填 `box.json`，粘贴 JSON 内容
3. 再点 **Add file** 添加第二个文件 `tvbox-config.jar`（需要二进制上传）
4. 创建后点文件名旁的 **raw** 按钮获取直链

## 📱 TVBox 配置方法

### 接口配置（用 JSON URL）

1. 打开 TVBox → **我的** → **设置** → **配置地址**
2. 配置类型选 **接口**
3. 粘贴 JSON URL：
   ```
   https://raw.githubusercontent.com/your-username/tvbox-config/main/tvbox-interface.json
   ```
4. 点确定保存

### 完整配置（用 JAR URL）

1. 打开 TVBox → **我的** → **设置** → **配置地址**
2. 配置类型选 **完整**
3. 粘贴 JAR URL：
   ```
   https://raw.githubusercontent.com/your-username/tvbox-config/main/tvbox-config.jar
   ```
4. 点确定保存

## 🌐 国内加速（GitHub 代理）

如果 TVBox 直接访问 GitHub 较慢，可在 URL 前加代理前缀：

| 代理服务 | 前缀 |
|----------|------|
| gh-proxy | `https://gh-proxy.com/` |
| ghproxy.net | `https://ghproxy.net/` |
| 99988866 | `https://gh.api.99988866.xyz/` |

例如加代理后的 JAR URL：
```
https://gh-proxy.com/https://raw.githubusercontent.com/your-username/tvbox-config/main/tvbox-config.jar
```

## 🔄 更新配置

修改 `box.json` 后，重新运行 `python build.py` 即可重新生成 JAR 文件，再上传更新即可。
