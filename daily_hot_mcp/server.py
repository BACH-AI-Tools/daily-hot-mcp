import argparse
import os
from fastmcp import FastMCP
from daily_hot_mcp.utils.logger import logger

def main():
    """主入口函数，解析命令行参数并启动服务器"""
    parser = argparse.ArgumentParser(
        description="Daily Hot MCP - 全网热点趋势一站式聚合服务",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 基本启动（stdio 模式，用于 MCP 客户端）
  daily-hot-mcp
  
  # 带 API 密钥启动
  daily-hot-mcp --firecrawl-api-key your_api_key
  
  # 带自定义 RSS 源启动
  daily-hot-mcp --custom-rss-url https://your-rss-feed.com/feed
  
  # HTTP 模式启动
  daily-hot-mcp --transport http --host 0.0.0.0 --port 8000
        """
    )
    
    parser.add_argument(
        "--firecrawl-api-key",
        type=str,
        help="FireCrawl API 密钥，用于爬取网站内容获取热点详细信息"
    )
    
    parser.add_argument(
        "--custom-rss-url",
        type=str,
        help="自定义 RSS 订阅源 URL，配置后将自动添加 custom-rss 工具"
    )
    
    parser.add_argument(
        "--transport",
        type=str,
        default="stdio",
        choices=["stdio", "http"],
        help="传输模式：stdio (用于 MCP 客户端) 或 http (手动启动服务器)"
    )
    
    parser.add_argument(
        "--host",
        type=str,
        default="0.0.0.0",
        help="HTTP 模式的主机地址 (默认: 0.0.0.0)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="HTTP 模式的端口 (默认: 8000)"
    )
    
    parser.add_argument(
        "--path",
        type=str,
        default="/mcp",
        help="HTTP 模式的路径 (默认: /mcp)"
    )
    
    args = parser.parse_args()
    
    # 将命令行参数设置为环境变量，供工具使用
    if args.firecrawl_api_key:
        os.environ["FIRECRAWL_API_KEY"] = args.firecrawl_api_key
    
    if args.custom_rss_url:
        os.environ["TRENDS_HUB_CUSTOM_RSS_URL"] = args.custom_rss_url
    
    # 在参数解析后导入工具（确保环境变量已设置）
    from daily_hot_mcp.tools import all_tools
    
    # 创建 MCP 服务器实例
    server = FastMCP(name="daily-hot-mcp")
    
    # 注册所有工具
    for tool in all_tools:
        server.add_tool(tool)
    
    # 根据传输模式启动服务器
    if args.transport == "stdio":
        # stdio 模式：用于 MCP 客户端（Claude Desktop 等）
        server.run(transport="stdio")
    else:
        # HTTP 模式：用于手动启动服务器
        logger.info(f"Starting Daily Hot MCP server with HTTP transport (http://{args.host}:{args.port}{args.path})")
        try:
            server.run(
                transport="http",
                host=args.host,
                port=args.port,
                path=args.path,
                log_level="INFO"
            )
        except KeyboardInterrupt:
            logger.info("Server stopped by user")

if __name__ == "__main__":
    main()