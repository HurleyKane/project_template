#!/usr/bin/env bash
set -e

# 默认值
SOURCES_INPUT=""
DEST_ROOT=""
TYPE_INPUT="auto"

# 帮助信息
show_help() {
  echo "用法: $0 [选项...]"
  echo
  echo "选项:"
  echo "  -s, --sources SOURCES    要下载的资源URL列表，多个URL用逗号分隔，或者以JSON数组形式提供"
  echo "  -d, --dest DEST          下载内容存放的目标目录"
  echo "  -t, --type TYPE          指定处理类型，可以是 'git', 'zip', 'tar' 或 'auto'（默认）"
  echo "  -h, --help               显示此帮助信息"
  echo
  echo "示例:"
  echo "  $0 -s 'https://github.com/libeigen/eigen.git,https://example.com/file.zip' -d third_party -t auto"
  echo "  $0 --sources '[\"https://github.com/libeigen/eigen.git\", \"https://example.com/file.zip\"]' --dest deps --type auto"
  echo
  echo "支持的资源类型:"
  echo "  - git 仓库 (.git 结尾)"
  echo "  - ZIP 压缩包 (.zip 结尾)"
  echo "  - TAR 压缩包 (.tar.gz 或 .tgz 结尾)"
}

# 解析命令行参数
while [[ $# -gt 0 ]]; do
  case $1 in
    -s|--sources)
      SOURCES_INPUT="$2"
      shift 2
      ;;
    -d|--dest)
      DEST_ROOT="$2"
      shift 2
      ;;
    -t|--type)
      TYPE_INPUT="$2"
      shift 2
      ;;
    -h|--help)
      show_help
      exit 0
      ;;
    *)
      echo "未知选项: $1"
      show_help
      exit 1
      ;;
  esac
done

# 检查必需参数
if [ -z "$SOURCES_INPUT" ] || [ -z "$DEST_ROOT" ]; then
  echo "错误: 缺少必需的参数"
  show_help
  exit 1
fi

# -----------------------------
# 参数：sources dest type
# -----------------------------

# -----------------------------
# 解析输入为列表（不依赖 jq）
# -----------------------------
parse_sources() {
  local input="$1"
  
  # 检查是否为 JSON 数组格式
  if echo "$input" | grep -q '^\['; then
    # 处理 JSON 数组格式: ["url1", "url2", ...]
    echo "$input" | \
      sed 's/\[//g; s/\]//g; s/"//g' | \
      tr ',' '\n' | \
      sed 's/^[[:space:]]*//; s/[[:space:]]*$//' | \
      grep -v '^$' > sources_list.txt
  else
    # 处理逗号分隔格式
    echo "$input" | tr ', ' '\n' > sources_list.txt
  fi
}

# 调用解析函数
parse_sources "$SOURCES_INPUT"

echo "Parsed sources:"
cat sources_list.txt
echo

# -----------------------------
# 处理每个 source
# -----------------------------
while IFS= read -r src; do
  if [ -z "$src" ]; then
    continue
  fi
  echo "Processing source: $src"

  if [ "$TYPE_INPUT" != "auto" ]; then
    type="$TYPE_INPUT"
  elif [[ "$src" == *.git ]]; then
    type="git"
  elif [[ "$src" == *.zip ]]; then
    type="zip"
  elif [[ "$src" == *.tar.gz || "$src" == *.tgz ]]; then
    type="tar"
  else
    type="unknown"
  fi

  echo "Detected type: $type"

  mkdir -p "$DEST_ROOT"

  if [ "$type" = "git" ]; then
    repo_name=$(basename "$src" .git)
    echo "Cloning $src into $DEST_ROOT/$repo_name"
    git clone --depth=1 "$src" "$DEST_ROOT/$repo_name"

  elif [ "$type" = "zip" ]; then
    echo "Downloading ZIP: $src"
    wget -q "$src" -O tmp_archive.zip
    unzip -q tmp_archive.zip -d "$DEST_ROOT"
    rm tmp_archive.zip

  elif [ "$type" = "tar" ]; then
    echo "Downloading TAR: $src"
    wget -q "$src" -O tmp_archive.tar.gz
    tar -xf tmp_archive.tar.gz -C "$DEST_ROOT" --strip-components=1
    rm tmp_archive.tar.gz

  else
    echo "Skipping unsupported source type for $src"
  fi

done < sources_list.txt

echo "✅ All sources processed successfully!"