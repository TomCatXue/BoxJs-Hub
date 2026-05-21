# BoxJs Hub

## 📖 简介

**BoxJs Hub** 是一个聚合多个 BoxJs 脚本订阅源的开源仓库，旨在为 Quantumult X、Surge、Loon 等代理工具用户提供一站式脚本订阅管理方案。

## 🎯 用途

本仓库通过 `store.json` 文件集中管理来自不同作者的 BoxJs 订阅源，方便用户：

- **快速浏览**：按作者分类查看各类脚本订阅
- **一键订阅**：每个条目包含可直接使用的 `boxjs_url`
- **分类筛选**：支持按 `category`（日常工具、签到挂机、影视音影、系统优化等）和 `tags` 筛选
- **保持更新**：记录各订阅源的 `update_time`，便于追踪最新状态

## 📂 仓库结构

```
BoxJs-Hub/
├── README.md      # 本说明文档
├── store.json     # 脚本订阅源索引文件（按作者首字母排序）
└── index.html     # 可选的可视化浏览页面
```

## 📋 数据格式

`store.json` 中每个订阅源条目包含以下字段：

| 字段 | 说明 |
|------|------|
| `id` | 唯一标识符 |
| `name` | 订阅源名称 |
| `author` | 作者名称 |
| `icon` | 作者头像/图标 URL |
| `description` | 订阅源功能描述 |
| `category` | 分类（日常工具/签到挂机/影视音影/系统优化等） |
| `tags` | 标签数组，便于筛选 |
| `boxjs_url` | BoxJs 订阅地址（可直接导入使用） |
| `update_time` | 最后更新时间 |

## 🚀 使用方法

1. 在支持 BoxJs 的应用（如 Quantumult X、Surge）中打开设置
2. 找到 BoxJs 订阅管理页面
3. 添加 `boxjs_url` 对应的订阅地址即可使用

## 🤝 贡献

欢迎提交 Issue 或 Pull Request 添加新的订阅源或更新现有条目。

## 📄 许可

本仓库遵循开源精神，仅供学习交流使用。
