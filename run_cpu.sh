#!/bin/bash

# 获取当前时间
current_time=$(date +"%Y%m%d%H%M%S")

# 遍历 abacus 文件夹中的所有文件
for file in abacus-stru/*
do
    # 检查是否为文件
    if [ -f "$file" ]; then
        # 获取文件名（不包括路径）
        filename=$(basename "$file")
        
        # 在 result 文件夹下创建以当前时间命名的文件夹
        mkdir -p "result/$current_time/$filename"
        
        # 将文件拷贝到新创建的文件夹中，并重命名为 "STRU"
        cp "$file" "result/$current_time/$filename/STRU"
        cp INPUT_cpu "result/$current_time/$filename/INPUT"

        # 进入新创建的文件夹
        pushd "result/$current_time/$filename"
        echo "Running $filename"

        # 运行可执行文件（假设可执行文件名为 "executable"）
        /mnt/abacus-develop/build/abacus
        
        # 返回到原始目录
        popd
    fi
done