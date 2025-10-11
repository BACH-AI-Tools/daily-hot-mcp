# Daily Hot MCP - 快速开始

## 🚀 快速使用（推荐）

使用 `uvx` 无需安装，直接运行：

```bash
uvx daily-hot-mcp
```

服务将在 `http://0.0.0.0:8000/mcp/` 启动。

## 📦 安装使用

```bash
# 使用 pip 安装
pip install daily-hot-mcp

# 启动服务
daily-hot-mcp
```

## 🔧 带参数启动

```bash
# 查看所有可用参数
daily-hot-mcp --help

# 启用 FireCrawl 网页爬取功能
daily-hot-mcp --firecrawl-api-key your_api_key

# 启用自定义 RSS 源
daily-hot-mcp --custom-rss-url https://your-feed.com/rss

# 同时启用多个功能
daily-hot-mcp \
  --firecrawl-api-key your_api_key \
  --custom-rss-url https://your-feed.com/rss
```

## 🔌 MCP 客户端配置

在您的 MCP 客户端配置中添加：

```json
{
  "mcpServers": {
    "daily-hot": {
      "type": "http",
      "url": "http://localhost:8000/mcp/"
    }
  }
}
```

## 🛠️ 可用工具

服务提供 30+ 个热点数据工具：

- 📰 新闻资讯：百度、今日头条、IT 之家、BBC、36 氪等
- 📱 社交媒体：微博、知乎、抖音、小红书等
- 🎮 娱乐内容：bilibili、豆瓣、微信读书等
- 🛒 生活消费：什么值得买、少数派等
- 🌐 其他：网页爬取、自定义 RSS 等

## 💡 使用示例

启动服务后，在 MCP 客户端中可以调用工具：

```python
# 获取百度热搜
get-baidu-trending()

# 获取知乎热榜
get-zhihu-trending()

# 爬取网页内容（需要配置 FireCrawl API Key）
crawl_website(url="https://example.com")
```

## 📚 更多信息

- 详细文档：查看 [README.md](README.md)
- 发布指南：查看 [PUBLISH.md](PUBLISH.md)
- 发布总结：查看 [RELEASE_SUMMARY.md](RELEASE_SUMMARY.md)
