# PyPI 发布指南

本文档说明如何将 daily-hot-mcp 发布到 PyPI。

## 前置要求

1. 安装构建工具：

```bash
pip install build twine
```

2. 获取 PyPI API Token：
   - 访问 https://pypi.org/manage/account/token/
   - 创建新的 API token
   - 保存 token（格式：`pypi-...`）

## 发布步骤

### 1. 更新版本号

编辑 `pyproject.toml`，更新版本号：

```toml
version = "1.6.4"  # 根据语义化版本规范更新
```

### 2. 清理旧的构建文件

```bash
rm -rf dist/ build/ *.egg-info
```

### 3. 构建包

```bash
python -m build
```

这将在 `dist/` 目录下生成两个文件：

- `daily_hot_mcp-x.x.x.tar.gz` (源码分发)
- `daily_hot_mcp-x.x.x-py3-none-any.whl` (wheel 分发)

### 4. 本地测试（可选但推荐）

```bash
# 在虚拟环境中测试安装
python -m venv test_env
source test_env/bin/activate  # Windows: test_env\Scripts\activate

# 安装构建的包
pip install dist/daily_hot_mcp-*.whl

# 测试命令
daily-hot-mcp --help

# 测试运行（按 Ctrl+C 停止）
daily-hot-mcp --firecrawl-api-key test_key

# 清理
deactivate
rm -rf test_env
```

### 5. 上传到 TestPyPI（可选，用于测试）

```bash
python -m twine upload --repository testpypi dist/*
```

然后测试安装：

```bash
pip install --index-url https://test.pypi.org/simple/ daily-hot-mcp
```

### 6. 上传到 PyPI

```bash
python -m twine upload dist/*
```

系统会提示输入：

- Username: `__token__`
- Password: 你的 PyPI API token（`pypi-...`）

或者配置 `~/.pypirc` 文件避免每次输入：

```ini
[pypi]
username = __token__
password = pypi-你的token
```

### 7. 验证发布

访问 https://pypi.org/project/daily-hot-mcp/ 确认包已发布。

### 8. 测试安装

```bash
# 使用 uvx（推荐）
uvx daily-hot-mcp --help

# 或使用 pip
pip install daily-hot-mcp
daily-hot-mcp --help
```

## 常见问题

### Q: 上传失败，提示 "File already exists"

A: 你不能覆盖已发布的版本。需要更新版本号后重新构建和上传。

### Q: 如何撤回已发布的版本？

A: PyPI 不支持删除版本，但你可以"yank"它（标记为不推荐）：

```bash
pip install pkginfo
python -m twine upload --skip-existing dist/*
```

### Q: 如何更新项目描述？

A: 更新 `README.md` 或 `pyproject.toml` 中的 `description`，然后发布新版本。

## 版本号规范

遵循语义化版本 (SemVer)：

- **MAJOR.MINOR.PATCH** (例如：1.6.3)
- MAJOR: 不兼容的 API 变更
- MINOR: 向后兼容的功能新增
- PATCH: 向后兼容的问题修正

## 发布清单

- [ ] 更新版本号
- [ ] 更新 CHANGELOG（如果有）
- [ ] 运行测试
- [ ] 清理构建文件
- [ ] 构建包
- [ ] 本地测试安装
- [ ] 上传到 PyPI
- [ ] 验证 PyPI 页面
- [ ] 测试 uvx 安装
- [ ] 创建 Git tag
- [ ] 推送到 GitHub

## Git 标签

发布后建议创建 Git 标签：

```bash
git tag -a v1.6.3 -m "Release version 1.6.3"
git push origin v1.6.3
```
